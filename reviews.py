import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="freebird"
)

cursor = db.cursor()


class User:
    def __init__(self, user_id, username, password, email, surname, name):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.surname = surname
        self.name = name

    def choose_review_type(self, action):
        if action == "write":
            self.write_review()
        elif action == "view":
            self.view_reviews()
        elif action == "update":
            self.update_review()

    def write_review(self):
        review_window = tk.Toplevel()
        review_window.title("Write Review")

        bg_image = Image.open("C:/ceid7/software-eng/project/reviewspage.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        review_window.geometry(f"{bg_photo.width()}x{bg_photo.height()}")

        bg_canvas = tk.Canvas(review_window, width=bg_photo.width(), height=bg_photo.height())
        bg_canvas.pack(fill="both", expand=True)
        bg_canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        bg_canvas.image = bg_photo

        form_frame = tk.Frame(review_window, bg="#FFEBD6")
        form_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(form_frame, text="Review", font=("Helvetica", 14)).pack()
        review_text = tk.Entry(form_frame, font=("Helvetica", 12))
        review_text.pack(ipadx=50, ipady=10)

        tk.Label(form_frame, text="Rating", font=("Helvetica", 12)).pack()
        rating = tk.Entry(form_frame, font=("Helvetica", 12))
        rating.pack()

        tk.Label(form_frame, text="Destination (Optional)", font=("Arial", 12)).pack()
        dest_id = tk.Entry(form_frame, font=("Arial", 12))
        dest_id.pack()

        tk.Label(form_frame, text="Accommodation (Optional)", font=("Arial", 12)).pack()
        accommodation_id = tk.Entry(form_frame, font=("Arial", 12))
        accommodation_id.pack()

        tk.Label(form_frame, text="Event (Optional)", font=("Arial", 12)).pack()
        event_id = tk.Entry(form_frame, font=("Arial", 12))
        event_id.pack()

        tk.Label(form_frame, text="Attraction (Optional)", font=("Arial", 12)).pack()
        attraction_id = tk.Entry(form_frame, font=("Arial", 12))
        attraction_id.pack()

        def save():
            new_review = Reviews(
                user_id=self.user_id,
                dest_id=int(dest_id.get()) if dest_id.get() else None,
                accommodation_id=int(accommodation_id.get()) if accommodation_id.get() else None,
                review=review_text.get(),
                rating=int(rating.get()) if rating.get() else None,
                event_id=int(event_id.get()) if event_id.get() else None,
                attraction_id=int(attraction_id.get()) if attraction_id.get() else None,
                review_type="Write"
            )
            new_review.save_review()
            review_window.destroy()

        save_btn = tk.Button(form_frame, text="Save Review", command=save, font=("Arial", 12))
        save_btn.pack(pady=10)

    def view_reviews(self):
        Reviews.add_filters(self.user_id)

    def update_review(self):
        update_window = tk.Toplevel()
        update_window.title("Update Review")

        tk.Label(update_window, text="Review ID").pack()
        review_id = tk.Entry(update_window)
        review_id.pack()

        tk.Label(update_window, text="New Review").pack()
        new_review_text = tk.Entry(update_window)
        new_review_text.pack()

        tk.Label(update_window, text="New Rating").pack()
        new_rating = tk.Entry(update_window)
        new_rating.pack()

        def update():
            Reviews.update_review(int(review_id.get()), new_review_text.get(), int(new_rating.get()))
            update_window.destroy()

        update_btn = tk.Button(update_window, text="Update Review", command=update)
        update_btn.pack(pady=10)


class Reviews:
    def __init__(self, user_id, dest_id, accommodation_id, attraction_id, review, rating, event_id, review_type):
        self.user_id = user_id
        self.dest_id = dest_id
        self.accommodation_id = accommodation_id
        self.attraction_id = attraction_id
        self.review = review
        self.rating = rating
        self.event_id = event_id
        self.review_type = review_type

    def save_review(self):
        query = """
        INSERT INTO reviews (user_id, dest_id, accommodation_id, attraction_id, review, rating, event_id, review_type)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            self.user_id,
            self.dest_id if self.dest_id is not None else None,
            self.accommodation_id if self.accommodation_id is not None else None,
            self.attraction_id if self.attraction_id is not None else None,
            self.review,
            self.rating if self.rating is not None else None,
            self.event_id if self.event_id is not None else None,
            self.review_type
        )
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Review saved successfully")

    @staticmethod
    def view_reviews_from_db(user_id):
        query = "SELECT * FROM reviews WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        reviews = cursor.fetchall()
        print(f"Fetched reviews: {reviews}")
        return reviews

    @staticmethod
    def update_review(review_id, new_review, new_rating):
        query = "UPDATE reviews SET review = %s, rating = %s WHERE review_id = %s"
        cursor.execute(query, (new_review, new_rating, review_id))
        db.commit()
        messagebox.showinfo("Success", "Review updated successfully")

    def add_filters(self):
        filter_window = tk.Toplevel()
        filter_window.title("Add Filters")

        bg_image = Image.open("C:/ceid7/software-eng/project/filterspage.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        filter_window.geometry(f"{bg_photo.width()}x{bg_photo.height()}")

        bg_canvas = tk.Canvas(filter_window, width=bg_photo.width(), height=bg_photo.height())
        bg_canvas.pack(fill="both", expand=True)
        bg_canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        bg_canvas.image = bg_photo

        form_frame = tk.Frame(bg_canvas, bg="#FFEBD6")
        form_frame.place(relx=0.5, rely=0.3, anchor="center")

        tk.Label(form_frame, text="Location").grid(row=0, column=0)
        location = tk.Entry(form_frame, width=30)
        location.grid(row=0, column=1)
        tk.Label(form_frame, text="Type of Review").grid(row=1, column=0, padx=20, pady=10)
        review_type_var = tk.StringVar(value="Event")
        review_type_options = ["Event", "Accommodation", "Attraction"]
        review_type_menu = ttk.Combobox(form_frame, textvariable=review_type_var, values=review_type_options,
                                        width=20)
        review_type_menu.grid(row=1, column=1, padx=10, pady=5)

        def filter_reviews():
            location_val = location.get()
            review_type_val = review_type_var.get()

            if location_val.lower() == "all":
                query = "SELECT * FROM reviews WHERE review_type = %s"
                cursor.execute(query, (review_type_val,))
                reviews = cursor.fetchall()
            else:
                cursor.execute("SELECT destination_id FROM destinations WHERE location = %s", (location_val,))
                dest_id = cursor.fetchone()
                if dest_id:
                    dest_id = dest_id[0]

                    query = "SELECT * FROM reviews WHERE review_type = %s AND dest_id = %s"
                    values = [review_type_val, dest_id]
                    cursor.execute(query, values)
                    reviews = cursor.fetchall()
                else:
                    messagebox.showerror("Error", "Location not found")
                    return

            print(reviews)
            Reviews.display_filtered_reviews(reviews)

        filter_btn = tk.Button(form_frame, text="Apply Filters", command=filter_reviews)
        filter_btn.grid(row=2, columnspan=2, pady=10)

    @staticmethod
    def display_filtered_reviews(reviews):
        review_window = tk.Toplevel()
        review_window.title("Filtered Reviews")

        bg_image = Image.open("C:/ceid7/software-eng/project/reviewspage2.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        review_window.geometry(f"{bg_photo.width()}x{bg_photo.height()}")

        bg_canvas = tk.Canvas(review_window, width=bg_photo.width(), height=bg_photo.height())
        bg_canvas.pack(fill="both", expand=True)
        bg_canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        bg_canvas.image = bg_photo

        reviews_frame = tk.Frame(bg_canvas, bg="white")
        reviews_frame.place(relx=0.5, rely=0.5, anchor="center")

        for i, review in enumerate(reviews):
            review_text = f"Review ID: {review[0]}\nUser ID: {review[1]}\nDestination ID: {review[2]}\nAccommodation ID: {review[3]}\nReview: {review[4]}\nRating: {review[5]}\nEvent ID: {review[6]}\nReview Type: {review[7]}"
            tk.Label(reviews_frame, text=review_text, justify=tk.LEFT, bg="white").grid(row=i, column=0, sticky="w", pady=5)

        if not reviews:
            tk.Label(reviews_frame, text="No reviews found.", bg="white").pack()

        review_window.mainloop()


def main():
    window = tk.Tk()
    window.title("Reviews")

    # Επειδή δεν έχουμε συνδέσει κάποιον χρήστη για αυτό το use case και χρειάζεται να πάρει
    # το id του δημιουργούμε έναν νέο χρήστη με τα δεδομένα του πρώτου στη βάση
    def create_user():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        surname = surname_entry.get()
        name = name_entry.get()

        query = "INSERT INTO users (username, password, email, surname, name) VALUES (%s, %s, %s, %s, %s)"
        values = (username, password, email, surname, name)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "User created successfully")
        user_id = cursor.lastrowid
        current_user = User(user_id, username, password, email, surname, name)
        show_action_buttons(current_user, window)

    def choose_action(action, current_user):
        current_user.choose_review_type(action)

    def show_action_buttons(current_user, window):
        bg_image = Image.open("C:/ceid7/software-eng/project/reviewspage.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        window.geometry(f"{bg_photo.width()}x{bg_photo.height()}")

        bg_canvas = tk.Canvas(window, width=bg_photo.width(), height=bg_photo.height())
        bg_canvas.pack(fill="both", expand=True)
        bg_canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        bg_canvas.image = bg_photo

        btn_width = 20
        btn_height = 3

        write_btn = tk.Button(bg_canvas, text="Write Review", command=lambda: choose_action("write", current_user),
                              width=btn_width, height=btn_height)
        write_btn.place(relx=0.5, rely=0.4, anchor="center")

        view_btn = tk.Button(bg_canvas, text="View Reviews", command=lambda: choose_action("view", current_user),
                             width=btn_width, height=btn_height)
        view_btn.place(relx=0.5, rely=0.5, anchor="center")

        update_btn = tk.Button(bg_canvas, text="Update Review", command=lambda: choose_action("update", current_user),
                               width=btn_width, height=btn_height)
        update_btn.place(relx=0.5, rely=0.6, anchor="center")

    def show_user_creation_form(window):
        for widget in window.winfo_children():
            widget.destroy()

        tk.Label(window, text="Username").pack()
        global username_entry
        username_entry = tk.Entry(window)
        username_entry.pack()

        tk.Label(window, text="Password").pack()
        global password_entry
        password_entry = tk.Entry(window, show="*")
        password_entry.pack()

        tk.Label(window, text="Email").pack()
        global email_entry
        email_entry = tk.Entry(window)
        email_entry.pack()

        tk.Label(window, text="Surname").pack()
        global surname_entry
        surname_entry = tk.Entry(window)
        surname_entry.pack()

        tk.Label(window, text="Name").pack()
        global name_entry
        name_entry = tk.Entry(window)
        name_entry.pack()

        create_btn = tk.Button(window, text="Create User", command=create_user)
        create_btn.pack(pady=20)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    if not users:
        show_user_creation_form(window)
    else:
        user_id, name, surname, email, username, password = users[0]
        current_user = User(user_id, username, password, email, surname, name)
        show_action_buttons(current_user, window)

    window.mainloop()


if __name__ == "__main__":
    main()

