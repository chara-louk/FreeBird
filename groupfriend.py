import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="26vir02",
            database="freebird"
        )
        self.cursor = self.connection.cursor()

    def user_exists(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        return self.cursor.fetchone() is not None

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

class Chat:
    def __init__(self, db):
        self.db = db

    def store_team_info(self, team_name, emails):
        try:
            members = ", ".join(emails)
            self.db.cursor.execute("INSERT INTO chat (members, name) VALUES (%s, %s)", (members, team_name))
            self.db.commit()
            print("Team information stored:", members, team_name)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.db.rollback()

class FreeBirdApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FreeBird")

        # Load background image
        try:
            self.background_image = Image.open("C:/Apps/iphonefriends.jpg")
            self.background_photo = ImageTk.PhotoImage(self.background_image)

            # Create a canvas for the background image
            self.canvas = tk.Canvas(self.root, width=self.background_photo.width(), height=self.background_photo.height())
            self.canvas.pack(fill="both", expand=True)
            self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

            # List to hold all text entries
            self.text_entries = []

            # Create the first text box
            self.create_text_entry("Enter the 1st email", 150)
            # Create the second text box
            self.create_text_entry("Enter the 2nd email", 230)

            # Create a button to submit the text
            self.submit_button = tk.Button(self.root, text="Create", command=self.submit_text)
            self.submit_button.place(x=150, y=310, anchor="nw")  # Place at specific coordinates

            # Create a label to add a friend
            self.add_friend_label = tk.Label(self.root, text="Add Friends", fg="blue", cursor="hand2")
            self.add_friend_label.place(x=150, y=125, anchor="nw")  # Place at specific coordinates
            self.add_friend_label.bind("<Button-1>", self.add_friend)  # Bind click event

            print("Image loaded successfully.")
        except Exception as e:
            print("Error loading image:", e)

        self.database = Database()
        self.chat = Chat(self.database)
        self.emails = []  # Initialize the list to store emails

    def create_text_entry(self, default_text, y_position):
        text_entry = tk.Text(self.root, height=2, width=25)
        text_entry.place(x=20, y=y_position, anchor="nw")  # Place at specific coordinates
        text_entry.insert("1.0", default_text)
        text_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, text_entry, default_text))  # Bind focus event
        self.text_entries.append(text_entry)

    def on_entry_click(self, event, entry, default_text):
        if entry.get("1.0", "end-1c") == default_text:
            entry.delete("1.0", "end-1c")
            entry.config(fg='black')

    def submit_text(self):
        self.emails.clear()  # Clear any previous emails
        for entry in self.text_entries:
            email = entry.get("1.0", "end-1c")
            if not self.database.user_exists(email):
                messagebox.showerror("Error", f"User with email {email} does not exist.")
                return
            self.emails.append(email)

        # If all users exist, open the new window to enter the team name
        self.open_new_window()

    def add_friend(self, event=None):
        y_position = 150 + len(self.text_entries) * 80  # Adjust position based on number of text boxes
        new_text_entry = tk.Text(self.root, height=2, width=25)
        new_text_entry.place(x=20, y=y_position, anchor="nw")
        new_text_entry.insert("1.0", "Enter an email")
        new_text_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, new_text_entry, "Enter an email"))
        self.text_entries.append(new_text_entry)

        # Move the submit button down
        self.submit_button.place_configure(y=y_position + 80)

    def open_new_window(self):
        self.root.withdraw()  # Hide the main window
        new_window = tk.Toplevel()
        new_window.title("Add Names")
        new_window.geometry(f"{self.background_photo.width()}x{self.background_photo.height()}")

        # Create a canvas for the background image in the new window
        new_canvas = tk.Canvas(new_window, width=self.background_photo.width(), height=self.background_photo.height())
        new_canvas.pack(fill="both", expand=True)
        new_canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        def on_close_new_window():
            new_window.destroy()  # Close the new window
            self.root.deiconify()  # Show the main window again

        new_window.protocol("WM_DELETE_WINDOW", on_close_new_window)

        name_entry = tk.Text(new_canvas, height=2, width=25)
        name_entry.place(x=20, y=200, anchor="nw")
        name_entry.insert("1.0", "Enter a name")
        name_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, name_entry, "Enter a name"))

        submit_name_button = tk.Button(new_canvas, text="Submit Name", command=lambda: self.submit_name(name_entry, new_window))
        submit_name_button.place(x=140, y=280, anchor="nw")

        # Create an "Add Photo" label
        add_photo_label = tk.Label(new_canvas, text="Add Photo", fg="blue", cursor="hand2")
        add_photo_label.place(x=20, y=250, anchor="nw")
        add_photo_label.bind("<Button-1>", self.add_photo)  # Bind click event

        # Create a back button to return to the main window
        back_button = tk.Button(new_canvas, text="Back", command=on_close_new_window)
        back_button.place(x=20, y=280, anchor="nw")

    def submit_name(self, name_entry, new_window):
        team_name = name_entry.get("1.0", "end-1c")
        self.chat.store_team_info(team_name, self.emails)
        new_window.destroy()  # Close the new window
        self.root.deiconify()  # Show the main window again

    def add_photo(self, event):
        # Placeholder function for add photo functionality
        print("Add photo functionality is not implemented yet.")

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    app = FreeBirdApp(root)
    root.mainloop()
