import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Accommodation Booking")

        background_image = tk.PhotoImage(file="image.png")
        self.background_label = tk.Label(self.root, image=background_image)
        self.background_label.image = background_image
        self.background_label.place(relwidth=1, relheight=1)

        self.setup_starting_window()
        self.root.mainloop()

    def setup_starting_window(self):
        self.clear_window()
        label = tk.Label(self.root, text="Would you like to reserve an accommodation?", font=('Arial', 14), bg='beige')
        label.pack(pady=20)

        yes_button = tk.Button(self.root, text="Yes", command=self.select_date, font=('Arial', 12))
        yes_button.pack(side=tk.LEFT, padx=20, pady=20)

        no_button = tk.Button(self.root, text="No", command=self.root.quit, font=('Arial', 12))
        no_button.pack(side=tk.RIGHT, padx=20, pady=20)

    def select_date(self):
        self.clear_window()
        self.select_date_window = tk.Frame(self.root)
        self.select_date_window.place(relwidth=1, relheight=1)

        label = tk.Label(self.select_date_window, text="Please select a date", font=('Arial', 14), bg='beige')
        label.pack(pady=20)

        self.calendar = DateEntry(self.select_date_window, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.calendar.pack(pady=20)

        submit_button = tk.Button(self.select_date_window, text="Submit", command=self.submit_and_show_filters, font=('Arial', 12))
        submit_button.pack(pady=20)

    def submit_and_show_filters(self):
        self.RegisterDate()
        self.show_filters()

    def RegisterDate(self):
        selected_date = self.calendar.get_date()
        messagebox.showinfo("Selected Date", f"You selected: {selected_date}")

    def show_filters(self):
        self.clear_window()
        self.filters_window = tk.Frame(self.root)
        self.filters_window.place(relwidth=1, relheight=1)

        label = tk.Label(self.filters_window, text="Filters", font=('Arial', 14), bg='beige')
        label.pack(pady=20)
        # Add your filters UI components here

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    MyApp()
