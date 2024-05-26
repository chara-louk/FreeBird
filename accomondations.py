import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

class accomodations:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("FreeBird")

        self.SetupStartingWindow()
        self.root.mainloop()

    def SetupStartingWindow(self):
        self.clear_window()
        self.starting_window = tk.Frame(self.root)
        self.starting_window.place(relwidth=1, relheight=1)

        label = tk.Label(self.starting_window, text="Do you want to proceed?", font=('Arial', 14))
        label.pack(pady=20)

        yes_button = tk.Button(self.starting_window, text="Yes", command=self.ShowDates)
        yes_button.pack(side=tk.LEFT, padx=20, pady=20)

        no_button = tk.Button(self.starting_window, text="No", command=self.root.quit)
        no_button.pack(side=tk.RIGHT, padx=20, pady=20)

    def ShowDates(self):
        self.clear_window()
        self.select_date_window = tk.Frame(self.root)
        self.select_date_window.place(relwidth=1, relheight=1)

        label = tk.Label(self.select_date_window, text="Select Date", font=('Arial', 14))
        label.pack(pady=20)

        self.date_entry = DateEntry(self.select_date_window, font=('Arial', 12), date_pattern='y-mm-dd')
        self.date_entry.pack(pady=20)

        submit_button = tk.Button(self.select_date_window, text="Submit", command=self.ShowFilters)
        submit_button.pack(pady=20)

    def ShowFilters(self):
        self.selected_date = self.date_entry.get()
        self.clear_window()
        self.filters_window = tk.Frame(self.root, bg='beige')
        self.filters_window.place(relwidth=1, relheight=1)

        label = tk.Label(self.filters_window, text="Filters", font=('Arial', 14), bg='beige')
        label.pack(pady=20)

        # Price Filter
        price_label = tk.Label(self.filters_window, text="Maximum Price ($):", font=('Arial', 12), bg='beige')
        price_label.pack(pady=10)
        self.price_entry = tk.Entry(self.filters_window, font=('Arial', 12))
        self.price_entry.pack(pady=10)

        # Accommodation Type Filter
        type_label = tk.Label(self.filters_window, text="Accommodation Type:", font=('Arial', 12), bg='beige')
        type_label.pack(pady=10)

        self.accommodation_type_vars = {
            "Airbnb": tk.BooleanVar(),
            "Hotel": tk.BooleanVar(),
            "Hostel": tk.BooleanVar(),
            "Motel": tk.BooleanVar(),
            "Bed & Breakfast": tk.BooleanVar()
        }

        for type_name, var in self.accommodation_type_vars.items():
            chk = tk.Checkbutton(self.filters_window, text=type_name, variable=var, font=('Arial', 12), bg='beige')
            chk.pack(anchor='w', padx=20)

        # Submit Button
        submit_button = tk.Button(self.filters_window, text="Apply Filters", font=('Arial', 12), command=self.ApplyFilers)
        submit_button.pack(pady=20)

    def ApplyFilers(self):
        max_price = self.price_entry.get()
        selected_types = [type_name for type_name, var in self.accommodation_type_vars.items() if var.get()]
        
        filters_summary = f"Selected Date: {self.selected_date}\nMax Price: {max_price}\nSelected Types: {', '.join(selected_types)}"
        
        messagebox.showinfo("Selected Filters", filters_summary)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    accomodations()
