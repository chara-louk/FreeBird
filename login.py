import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

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
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

class Login:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.text_entries = []

    def on_entry_click(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, "end")

    def setup_ui(self):
        self.root.title("FreeBird")
        self.background_image = Image.open("C:/Apps/login.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = tk.Canvas(self.root, width=self.background_photo.width(), height=self.background_photo.height())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        self.create_text_entry("Username", 310)
        self.create_text_entry("Password", 390)

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.place(x=180, y=470, anchor="nw")

    def login(self):
        username = self.text_entries[0].get()
        password = self.text_entries[1].get()

        if self.check_credentials(username, password):
            self.open_welcome_window()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def check_credentials(self, username, password):
        query = "SELECT EXISTS(SELECT 1 FROM users WHERE username = %s AND password = %s)"
        self.db.cursor.execute(query, (username, password))
        result = self.db.cursor.fetchone()
        return result[0] == 1

    def create_text_entry(self, default_text, y_position):
        text_entry = tk.Entry(self.root)
        text_entry.place(x=50, y=y_position, anchor="nw")
        text_entry.insert(0, default_text)
        text_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, text_entry, default_text))
        self.text_entries.append(text_entry)

    def open_welcome_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Welcome")

        self.background_welcome_image = Image.open("C:/Apps/welcome.jpg")
        self.background_welcome_photo = ImageTk.PhotoImage(self.background_welcome_image)

        new_canvas = tk.Canvas(new_window, width=self.background_welcome_photo.width(),
                               height=self.background_welcome_photo.height())
        new_canvas.pack(fill="both", expand=True)
        new_canvas.create_image(0, 0, image=self.background_welcome_photo, anchor="nw")

if __name__ == "__main__":
    root = tk.Tk()
    db = Database()
    app = Login(root, db)
    app.setup_ui()
    root.mainloop()
