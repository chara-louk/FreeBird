#Σχόλια για τον κώδικα:
#Για λόγους χρηστικότητας, επειδή δεν έχουμε φτιάξει login, το πρόγραμμα ζητά απο τον χρήστη να δόσει το user_id του
#αφού κανονικά θα το έπαιρνε αυτόματα κατά την είσοδο του χρήστη στην εφαρμογή



import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector


class Database:  # σύνδεση με τη βάση
    HOST = "localhost"
    USER = "root"
    PASSWORD = "26vir02"
    DATABASE = "freebird"

    def __init__(self):
        self.connection = mysql.connector.connect(
            host=self.HOST,
            user=self.USER,
            password=self.PASSWORD,
            database=self.DATABASE
        )
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):  # επειδή δεν έχουμε login βάζουμε χειροκίνητα το user_id
        query = "SELECT EXISTS(SELECT 1 FROM users WHERE user_id = %s)"
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchone()
        return result[0]

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()


class Points:  # κλάση εμφάνισης πόντων
    def __init__(self, db):
        self.db = db

    def show_points(self, user_id):  # σύνδεση με τη βάση για εμφάνιση πόντων
        query = "SELECT total_points FROM points WHERE user_id = %s"
        self.db.cursor.execute(query, (user_id,))
        result = self.db.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def get_all_points(self):
        query = "SELECT points, points_expiry FROM points"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()

class Booking:  # σύνδεση με τη βάση για εμφάνιση κρατήσεων
    def __init__(self, db):
        self.db = db

    def show_bookings(self, user_id):
        query = "SELECT * FROM booking WHERE user_id = %s"
        self.db.cursor.execute(query, (user_id,))
        result = self.db.cursor.fetchall()
        if result:
            return result
        else:
            messagebox.showerror("Info", "You don't have any bookings yet.")
            return None


class UI:  # εμφάνιση εφαρμογής
    def __init__(self, root, points, db):
        self.root = root
        self.points = points
        self.db = db
        self.booking = Booking(db)
        self.text_entries = []
        self.usersid = []
        self.setup_ui()

        self.submit_button = tk.Button(self.root, text="Next", command=self.submit_text)
        self.submit_button.place(x=150, y=310, anchor="nw")

    def setup_ui(self):  # περιβάλλον χρήστη
        self.root.title("FreeBird")
        self.background_image = Image.open("C:/Apps/points.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = tk.Canvas(self.root, width=self.background_photo.width(), height=self.background_photo.height())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        self.create_text_entry("Enter your id", 200)

    def create_text_entry(self, default_text, y_position):  # textbox για εισαγωγή User_id
        text_entry = tk.Text(self.root, height=2, width=25)
        text_entry.place(x=20, y=y_position, anchor="nw")
        text_entry.insert("1.0", default_text)
        text_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, text_entry, default_text))
        self.text_entries.append(text_entry)

    def on_entry_click(self, event, entry, default_text):  # για την απόκρυψη της πρότασης στο textbox όταν ο χρήστης επιλέγει να γράψει εκεί
        if entry.get("1.0", "end-1c") == default_text:
            entry.delete("1.0", "end-1c")
            entry.config(fg='black')

    def submit_text(self):  # εμφάνιση μηνυμάτων σφάλματος και τη λειτουργία της εφαρμογής
        self.usersid.clear()
        for entry in self.text_entries:
            userid = entry.get("1.0", "end-1c")
            if not self.db.user_exists(userid):
                messagebox.showerror("Error", f"User with id {userid} does not exist.")
                return
            self.usersid.append(userid)
        total_points = self.points.show_points(self.usersid[0])
        if total_points is not None:
            self.Show_Points(total_points)
        else:
            messagebox.showerror("Info", "No points found for this user.")

    def Show_Points(self, total_points):  # εμφάνιση αποτελεσμάτων
        new_window = tk.Toplevel(self.root)
        new_window.title("User Points")

        new_canvas = tk.Canvas(new_window, width=self.background_photo.width(), height=self.background_photo.height())
        new_canvas.pack(fill="both", expand=True)
        new_canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        points_message = f"Total Points:\n\n\n         {total_points}"
        new_canvas.create_text(40, 120, text=points_message, font=("Times New Roman", 16, "bold"), anchor="nw", fill="black")

        booking_button = tk.Button(new_window, text="Show Bookings", command=lambda: self.show_booking_info_window_ui(self.usersid[0]))
        booking_button.place(x=140, y=280, anchor="nw")

        analyze_button = tk.Button(new_window, text="Point Analysis", command=lambda: self.show_point_info_window_ui(self.usersid[0]))
        analyze_button.place(x=30, y=280, anchor="nw")

    def show_booking_info_window_ui(self, user_id): #εμφάνιση των κρατήσεων που έχει κάνει ο χρήστης
        booking_info = self.booking.show_bookings(user_id)
        if not booking_info:
            return

        new_window = tk.Toplevel(self.root)
        new_window.title("Booking Information")

        self.background_booking_image = Image.open("C:/Apps/bookings.jpg")
        self.background_booking_photo = ImageTk.PhotoImage(self.background_booking_image)

        new_canvas = tk.Canvas(new_window, width=self.background_booking_photo.width(), height=self.background_booking_photo.height())
        new_canvas.pack(fill="both", expand=True)
        new_canvas.create_image(0, 0, image=self.background_booking_photo, anchor="nw")

        for i, booking_data in enumerate(booking_info):
            user_id, booking_id, start_date, finish_date, event, destination = booking_data
            text = f"\n\n\n\n\n\n\n\nYour {booking_id} booking:\nStart Date: {start_date}\nFinish Date: {finish_date}\nEvent: {event}\nDestination: {destination}"
            new_canvas.create_text(20, 20 + i * 80, text=text, anchor="nw", fill="black")

        pay_button = tk.Button(new_window, text="Pay", command=lambda: self.show_point_info_window_ui(self.usersid[0]))
        pay_button.place(x=30, y=280, anchor="nw")

    def show_point_info_window_ui(self, user_id): #εμφάνιση της ανάλυσης των πόντων
        point_info = self.points.get_all_points()
        if point_info:
            new_window = tk.Toplevel(self.root)
            new_window.title("Point Information")

            self.background_analyze_image = Image.open("C:/Apps/points.jpg")
            self.background_analyze_photo = ImageTk.PhotoImage(self.background_analyze_image)

            new_canvas = tk.Canvas(new_window, width=self.background_analyze_photo.width(),
                                   height=self.background_analyze_photo.height())
            new_canvas.pack(fill="both", expand=True)
            new_canvas.create_image(0, 0, image=self.background_analyze_photo, anchor="nw")

            for i, points_data in enumerate(point_info):
                points, points_expiry = points_data
                text = f"\n\n\n\n\n\n\n\n Points                     Expiry:\n {points}                           {points_expiry}"
                new_canvas.create_text(20, 20 + i * 80, text=text, anchor="nw", fill="black")


if __name__ == "__main__":
    root = tk.Tk()
    db = Database()
    points = Points(db)
    app = UI(root, points, db)
    root.mainloop()
