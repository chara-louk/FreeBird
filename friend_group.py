import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# Διαχείριση βάσης
class Database:
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
        self.cursor = self.connection.cursor(buffered=True)

    def user_exists(self, email):  # έλεγχος εγγεγραμμένου χρήστη
        self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        return self.cursor.fetchone() is not None

    def commit(self):  # ενημέρωση βάσης
        self.connection.commit()

    def close(self):  # κλείσιμο σύνδεσης με τη βάση
        self.cursor.close()
        self.connection.close()

class Chat:  # Διαχείριση συνομιλιών
    def __init__(self, db):
        self.db = db
        self.team_name = ""
        self.emails = []

    def create(self, team_name, emails):
        self.team_name = team_name
        self.emails = emails
        # Ενημέρωση βάσης
        members = ", ".join(emails)
        # Εισαγωγή νέας εγγραφής στον πίνακα groups
        self.db.cursor.execute("INSERT INTO groups (members, team_name) VALUES (%s, %s)", (members, team_name))
        self.db.commit()

    def add_chat_textbox(self, chat_canvas):  # προσθήκη textbox για να γράψει ο χρήστης το μήνυμα (εμφάνιση σελίδας)
        self.chat_textbox = tk.Text(chat_canvas, height=1, width=15)
        self.chat_textbox.place(x=80, y=495, anchor="nw")

    def submit_name(self, name_entry, new_window, emails, app):  # καταχώρηση ονόματος ομάδας
        team_name = name_entry.get("1.0", "end-1c")
        self.create(team_name, emails)
        app.root.withdraw()
        # εμφάνιση σελίδας
        chat_window = tk.Toplevel(app.root)  # Χρησιμοποιήστε app.root αντί για self.root
        chat_window.title("Chat ")

        self.background_chat_image = Image.open("C:/Apps/chat.jpg")
        self.background_chat_photo = ImageTk.PhotoImage(self.background_chat_image)

        chat_canvas = tk.Canvas(chat_window, width=self.background_chat_photo.width(),
                                height=self.background_chat_photo.height())
        chat_canvas.pack(fill="both", expand=True)
        chat_canvas.create_image(0, 0, image=self.background_chat_photo, anchor="nw")

        self.add_chat_textbox(chat_canvas)
        # εμφάνιση ονόματος ομάδας
        team_name_label = tk.Label(chat_canvas, text=team_name, font=("Times New Roman", 10, "bold"))
        team_name_label.place(x=30, y=30)

        # Booking button
        booking_button = tk.Button(chat_canvas, text="Booking",
                                   command=lambda: self.show_booking_info_window_ui("user_id_example"))
        booking_button.place(x=180, y=30, anchor="nw")

    def show_booking_info_window_ui(self, user_id):
        booking = Booking(self.db)
        booking_info = booking.show_bookings(user_id)
        if not booking_info:
            return

        new_windows = tk.Toplevel(self.root)
        new_windows.title("Booking Information")

        self.background_booking_image = Image.open("C:/Apps/bookings.jpg")
        self.background_booking_photo = ImageTk.PhotoImage(self.background_booking_image)

        new_canvas = tk.Canvas(new_windows, width=self.background_booking_photo.width(),
                               height=self.background_booking_photo.height())
        new_canvas.pack(fill="both", expand=True)
        new_canvas.create_image(0, 0, image=self.background_booking_photo, anchor="nw")

        for i, booking_data in enumerate(booking_info):
            user_id, booking_id, start_date, finish_date, event, destination = booking_data
            text = f"Your {booking_id} booking:\nDestination: {destination} \nStart Date: {start_date}\nFinish Date: {finish_date}\nEvent: {event}"
            new_canvas.create_text(20, 20 + i * 80, text=text, anchor="nw", fill="black")



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

class newChat:  # Κύρια κλάση εφαρμογής (βασική ροή)
    def __init__(self, root):
        self.root = root
        self.database = Database()
        self.chat = Chat(self.database)
        self.ui = UI(root, self)
        self.background_images()

    def background_images(self):
        self.background_image = Image.open("C:/Apps/iphonefriends.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

    def add_name_image(self, emails):
        new_window = tk.Toplevel()
        new_window.title("Add Name")

        chat_b_image = Image.open("C:/Apps/iphone.jpg")
        self.chat_b_photo = ImageTk.PhotoImage(chat_b_image)

        new_canvas = tk.Canvas(new_window, width=self.chat_b_photo.width(), height=self.chat_b_photo.height())
        new_canvas.pack(fill="both", expand=True)
        new_canvas.create_image(0, 0, image=self.chat_b_photo, anchor="nw")

        name_entry = tk.Text(new_canvas, height=2, width=25)
        name_entry.place(x=20, y=200, anchor="nw")
        name_entry.insert("1.0", "Enter a name")
        name_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, name_entry, "Enter a name"))

        submit_name_button = tk.Button(new_canvas, text="Submit Name", command=lambda: self.chat.submit_name(name_entry, new_window, emails, self))
        submit_name_button.place(x=140, y=280, anchor="nw")

        add_photo_label = tk.Label(new_canvas, text="Add Photo", fg="blue", cursor="hand2")
        add_photo_label.place(x=20, y=250, anchor="nw")

    def on_entry_click(self, event, entry, placeholder):
        # Function to clear the placeholder text on focus
        if entry.get("1.0", "end-1c") == placeholder:
            entry.delete("1.0", "end")

    def show_booking_info_window_ui(self, user_id):
        # Function to handle the booking button action
        booking = Booking(self.database)
        booking_info = booking.show_bookings(user_id)
        if not booking_info:
            return

        new_windows = tk.Toplevel(self.root)
        new_windows.title("Booking Information")

        new_canvas = tk.Canvas(new_windows, width=self.background_booking_photo.width(),
                               height=self.background_booking_photo.height())
        new_canvas.pack(fill="both", expand=True)
        new_canvas.create_image(0, 0, image=self.background_booking_photo, anchor="nw")

        for i, booking_data in enumerate(booking_info):
            user_id, booking_id, start_date, finish_date, event, destination = booking_data
            text = f"Your {booking_id} booking:\nDestination: {destination} \nStart Date: {start_date}\nFinish Date: {finish_date}\nEvent: {event}"
            new_canvas.create_text(20, 20 + i * 80, text=text, anchor="nw", fill="black")

# διαμόρφωση UI
class UI:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.text_entries = []
        self.emails = []
        self.setup_ui()

    def setup_ui(self):
        self.root.title("FreeBird")
        self.background_image = Image.open("C:/Apps/iphonefriends.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = tk.Canvas(self.root, width=self.background_photo.width(), height=self.background_photo.height())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        # εισαγωγή των email για δημιουργία ομάδας
        self.create_text_entry("Enter the 1st email", 150)
        self.create_text_entry("Enter the 2nd email", 230)

        # Δημιουργία κουμπιού
        self.submit_button = tk.Button(self.root, text="Create", command=self.submit_text)
        self.submit_button.place(x=150, y=310, anchor="nw")

        # Δημιουργία ετικέτας για την προσθήκη φίλου
        self.add_friend_label = tk.Label(self.root, text="Add Friends", fg="black", cursor="hand2")
        self.add_friend_label.place(x=150, y=125, anchor="nw")
        self.add_friend_label.bind("<Button-1>", self.add_member)

    def create_text_entry(self, default_text, y_position):  # δημιουργία texbox
        text_entry = tk.Text(self.root, height=2, width=25)
        text_entry.place(x=20, y=y_position, anchor="nw")
        text_entry.insert("1.0", default_text)
        text_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, text_entry, default_text))
        self.text_entries.append(text_entry)

    def on_entry_click(self, event, entry, default_text):  # απόκρυψη της πρότασης μέσα στο textbox
        if entry.get("1.0", "end-1c") == default_text:
            entry.delete("1.0", "end-1c")
            entry.config(fg='black')

    def submit_text(self):  # εμφάνιση μηνυμάτων σφάλματος και την λειτουργία της εφαρμογής
        self.emails.clear()
        for entry in self.text_entries:
            email = entry.get("1.0", "end-1c")
            if not self.app.database.user_exists(email):
                messagebox.showerror("Error", f"User with email {email} does not exist.")
                return
            self.emails.append(email)
        self.app.add_name_image(self.emails)

    def add_member(self, event=None):
        y_position = 150 + len(self.text_entries) * 80
        new_text_entry = tk.Text(self.root, height=2, width=25)
        new_text_entry.place(x=20, y=y_position, anchor="nw")
        new_text_entry.insert("1.0", "Enter an email")
        new_text_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, new_text_entry, "Enter an email"))
        self.text_entries.append(new_text_entry)
        self.submit_button.place_configure(y=y_position + 80)

if __name__ == "__main__":
    root = tk.Tk()
    app = newChat(root)
    root.mainloop()
