import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector


class Database: #συνδεση με τη βάση
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

    def user_exists(self, user_id): #επειδή δεν έχουμε login βάζουμε χειροκίνητα το user_id
        query = "SELECT EXISTS(SELECT 1 FROM users WHERE user_id = %s)"
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchone()
        return result[0]

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()


class Points: #κλάση εμφάνισης πόντων
    def __init__(self, db):
        self.db = db

    def show_points(self, user_id): #συνδεση με τη βάση για εμφάνηση πόντων
        query = "SELECT total_points FROM points WHERE user_id = %s"
        self.db.cursor.execute(query, (user_id,))
        result = self.db.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None


class Booking: #συνδεση με τη βάση για εμφάνιση κρατήσεων
    def __init__(self, booking_id, start_date, finish_date, event, destination):
        self.booking_id = booking_id
        self.st_date = start_date
        self.f_date = finish_date
        self.event = event
        self.destination = destination


class UI: #εμφάνιση εφαρμογής
    def __init__(self, root, points, db):
        self.root = root
        self.points = points
        self.db = db
        self.text_entries = []
        self.usersid = []
        self.setup_ui()

        self.submit_button = tk.Button(self.root, text="Next", command=self.submit_text)
        self.submit_button.place(x=150, y=310, anchor="nw")

    def setup_ui(self): #περιβάλλον χρήστη
        self.root.title("FreeBird")
        self.background_image = Image.open("C:/Apps/points.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = tk.Canvas(self.root, width=self.background_photo.width(), height=self.background_photo.height())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        self.create_text_entry("Enter your id", 200)

    def create_text_entry(self, default_text, y_position):#textbox για εισαγωγή User_id
        text_entry = tk.Text(self.root, height=2, width=25)
        text_entry.place(x=20, y=y_position, anchor="nw")
        text_entry.insert("1.0", default_text)
        text_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, text_entry, default_text))
        self.text_entries.append(text_entry)

    def on_entry_click(self, event, entry, default_text): #για την απόκρυψη της προτασης στο textbox όταν ο χρήστης επιλέγει να γράψει εκεί
        if entry.get("1.0", "end-1c") == default_text:
            entry.delete("1.0", "end-1c")
            entry.config(fg='black')

    def submit_text(self): #εμφάνιση μηνυμάτων σφάλματος και την λειτουργία της εφαρμογής
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
            booking_info = self.showBookings()
            if booking_info:
                self.show_booking_info_window_ui(booking_info)
            else:
                messagebox.showinfo("Info", "No bookings for this user.")
        else:
            messagebox.showerror("Info", "No points found for this user.")

    def showBookings(self):#επικοινωνία με την βάση, εμφάνιση αποτελεσμάτων
        query = "SELECT * FROM booking WHERE user_id = %s"
        self.db.cursor.execute(query, (self.usersid[0],))
        return self.db.cursor.fetchall()

        new_window = tk.Toplevel(self.root)
        new_window.title("Booking Information")

        new_canvas = tk.Canvas(new_window, width=400, height=300)
        new_canvas.pack(fill="both", expand=True)

        for i, booking_data in enumerate(booking_info):
            user_id, booking_id, start_date, finish_date, event, destination = booking_data
            text = f"Booking ID: {booking_id}\nStart Date: {start_date}\nFinish Date: {finish_date}\nEvent: {event}\nDestination: {destination}"
            new_canvas.create_text(20, 20 + i * 80, text=text, anchor="nw", fill="black")

    def Show_Points(self, total_points):#εμφάνιση αποτελεσμάτων
        new_window = tk.Toplevel(self.root)
        new_window.title("User Points")

        new_canvas = tk.Canvas(new_window, width=self.background_photo.width(), height=self.background_photo.height())
        new_canvas.pack(fill="both", expand=True)
        new_canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        points_message = f"Total Points:\n\n\n\n\n{total_points}"
        new_canvas.create_text(40, 120, text=points_message, font=("Times New Roman", 16, "bold"), anchor="nw", fill="black")

    def show_booking_info_window_ui(self, booking_info):
        new_window = tk.Toplevel(self.root)
        new_window.title("Booking Information")

        new_canvas = tk.Canvas(new_window, width=400, height=300)
        new_canvas.pack(fill="both", expand=True)

        for i, booking_data in enumerate(booking_info):
            user_id, booking_id, start_date, finish_date, event, destination = booking_data
            text = f"Booking ID: {booking_id}\nStart Date: {start_date}\nFinish Date: {finish_date}\nEvent: {event}\nDestination: {destination}"
            new_canvas.create_text(20, 20 + i * 80, text=text, anchor="nw", fill="black")


if __name__ == "__main__":
    root = tk.Tk()
    db = Database()
    points = Points(db)
    app = UI(root, points, db)
    root.mainloop()
