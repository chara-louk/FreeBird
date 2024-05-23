import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="freebird"
)


def display_destinations_page(filtered_destinations, window):
    destinations_window = tk.Toplevel(window)
    destinations_window.title("Select Destination")

    bg_image = Image.open("C:/ceid7/software-eng/project/iphone2destinations.png")
    bg_photo = ImageTk.PhotoImage(bg_image)

    destinations_window.geometry(f"{bg_photo.width()}x{bg_photo.height()}")

    bg_canvas = tk.Canvas(destinations_window, width=bg_photo.width(), height=bg_photo.height())
    bg_canvas.pack(fill="both", expand=True)
    bg_canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    bg_canvas.image = bg_photo

    frame = ttk.Frame(bg_canvas, padding=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    ttk.Label(frame, text="Select a destination:", font=("Helvetica", 16, "bold")).pack(anchor="center")

    listbox = tk.Listbox(frame, selectmode="single", width=30, height=15, font=("Helvetica", 12))
    listbox.pack(padx=4, pady=4, fill="both", expand=True)

    for dest, missing_needs in filtered_destinations:
        display_text = dest.location
        if missing_needs:
            display_text += f" (doesn't have: {', '.join(missing_needs)})"
        listbox.insert(tk.END, display_text)

    def on_select(event=None):
        selected_index = listbox.curselection()
        if selected_index:
            selected_dest = filtered_destinations[selected_index[0]][0]
            dest_id = selected_dest.destination_id
            start = None
            finish = None
            type = None
            cost = None
            transportation_instance = Transportation(dest_id, start, finish, type, cost, destination_id=dest_id)
            transportation_instance.display_flights(selected_dest)
    listbox.bind('<<ListboxSelect>>', on_select)

    select_button = ttk.Button(frame, text="Select", command=on_select)
    select_button.pack(pady=10)


class Destination:
    def __init__(self, destination_id, location, museums, nature, beach, hiking, art, history, science, wild_life, clubs, sports, food,
                 shopping, mountains, forest, night_life, ratings, additional_needs):
        self.destination_id = destination_id
        self.location = location
        self.museums = museums
        self.nature = nature
        self.beach = beach
        self.hiking = hiking
        self.art = art
        self.history = history
        self.science = science
        self.wild_life = wild_life
        self.clubs = clubs
        self.sports = sports
        self.food = food
        self.shopping = shopping
        self.mountains = mountains
        self.forest = forest
        self.night_life = night_life
        self.ratings = ratings
        self.additional_needs = additional_needs

    @staticmethod
    def find_destinations(characteristic_vars, characteristics, rating_entry, filter_additional_needs, start_date_entry,
                          finish_date_entry, travelers_entry, budget_entry, destinations, save_filter_to_db,
                          display_destinations_page):
        selected_characteristics = [c.get() for c in characteristic_vars]
        selected_characteristics = [characteristics[i] for i, v in enumerate(selected_characteristics) if v == 1]

        user_rating = float(rating_entry.get())
        additional_needs = filter_additional_needs.get().split(',')

        start_date = start_date_entry.get()
        finish_date = finish_date_entry.get()
        travelers = int(travelers_entry.get())
        budget = float(budget_entry.get())

        user_filter = Filter(
            ratings=user_rating,
            start=start_date,
            finish=finish_date,
            travelers=travelers,
            additional_needs=filter_additional_needs.get(),
            budget=budget
        )
        save_filter_to_db(user_filter)

        filtered_destinations = []
        for dest in destinations:
            if all(getattr(dest, char) for char in selected_characteristics) and dest.ratings >= user_rating:
                # Handle None case for dest.additional_needs
                dest_additional_needs = dest.additional_needs.lower() if dest.additional_needs else ""
                missing_needs = [need.strip() for need in additional_needs if
                                 need.strip().lower() not in dest_additional_needs]
                filtered_destinations.append((dest, missing_needs))

        # Display filtered destinations
        if filtered_destinations:
            display_destinations_page(filtered_destinations,window)
        else:
            messagebox.showinfo("Destinations",
                                "No destinations found matching the selected characteristics and rating.")

    @classmethod
    def fetch_destinations_from_db(cls):
        cursor = db.cursor()
        cursor.execute(
            "SELECT destination_id, location, museums, nature, beach, hiking, art, history, science,"
            " wild_life, clubs, sports, food, shopping, mountains, forest, "
            "night_life, ratings, additional_needs FROM destinations")
        rows = cursor.fetchall()
        destinations = []
        for row in rows:
            destinations.append(cls(*row))
        return destinations

    @staticmethod
    def show_destination_info(location, destinations):
        info = [dest for dest in destinations if dest.location == location][0]
        info_str = (
            f"Location: {info.location}\n"
            f"Ratings: {info.ratings}\n"
            f"Additional Needs: {info.additional_needs}\n"
        )
        characteristics = ['museums', 'nature', 'beach', 'hiking', 'art', 'history', 'science', 'wild_life', 'clubs',
                           'sports', 'food', 'shopping', 'mountains', 'forest', 'night_life']
        for char in characteristics:
            if getattr(info, char):
                info_str += f"{char.capitalize()}: Yes\n"
            else:
                info_str += f"{char.capitalize()}: No\n"
        messagebox.showinfo("Destination Information", info_str)


class Filter:
    def __init__(self, ratings=None, start=None, finish=None, travelers=None, additional_needs=None, budget=None):
        self.ratings = ratings
        self.start = start
        self.finish = finish
        self.travelers = travelers
        self.additional_needs = additional_needs
        self.budget = budget

    def save_filter_to_db(self):
        cursor = db.cursor()
        insert_query = ("INSERT INTO filters (ratings, start, finish, travelers, budget,"
                        " additional_needs) VALUES (%s, %s, %s, %s, %s, %s)")
        cursor.execute(insert_query, (self.ratings, self.start, self.finish, self.travelers, self.budget, self.additional_needs))
        db.commit()
        cursor.close()


class Transportation:
    transportations = []

    def __init__(self, dest_id, start, finish, type, cost, destination_id):
        self.window = None
        self.trip_id = dest_id
        self.start = start
        self.finish = finish
        self.type = type
        self.cost = cost
        self.destination_id = destination_id

    def save_transp(self):
        Transportation.transportations.append(self)
        print("Transportation saved:", self)

    @staticmethod
    def retrieve_flights_from_db(selected_dest):
        cursor = db.cursor()
        query = "SELECT start, finish, type, cost FROM transportation WHERE dest_id = %s"
        cursor.execute(query, (selected_dest.destination_id,))
        rows = cursor.fetchall()

        flights = []
        for row in rows:
            flights.append({
                'start': row[0],
                'finish': row[1],
                'type': row[2],
                'cost': row[3]
            })
        cursor.close()
        return flights

    @staticmethod
    def display_flights(selected_dest):
        flights = Transportation.retrieve_flights_from_db(selected_dest)

        flights_window = tk.Toplevel()
        flights_window.title("Flights for " + selected_dest.location)

        if flights:
            for flight in flights:
                flight_info = f"Start: {flight['start']}, Finish: {flight['finish']}, Type: {flight['type']}, Cost: {flight['cost']}"
                ttk.Label(flights_window, text=flight_info).pack()
        else:
            ttk.Label(flights_window, text="No flights available for this destination.").pack()

class FreeBirdApp:

    def __init__(self, window):
        self.destination_instance = Destination('destination_id', 'location', 'museums', 'nature', 'beach', 'hiking', 'art', 'history', 'science', 'wild_life', 'clubs', 'sports', 'food', 'shopping',
                                                'mountains', 'forest', 'night_life', 'ratings','additional_needs')
        self.window = window
        self.characteristics = ['museums', 'nature', 'beach', 'hiking', 'art', 'history',
                                'science', 'wild_life', 'clubs', 'sports', 'food', 'shopping', 'mountains', 'forest', 'night_life']
        self.destinations = Destination.fetch_destinations_from_db()
        self.create_trip(self.characteristics,Destination.find_destinations)
        self.characteristic_vars = [tk.IntVar() for _ in self.characteristics]
        self.rating_entry = None
        self.filter_additional_needs = None
        self.start_date_entry = None
        self.finish_date_entry = None
        self.travelers_entry = None
        self.budget_entry = None

    def create_trip(self,characteristics,find_destinations):

        self.window.title("FreeBird")
        self.window.geometry("800x600")

        background_image = Image.open("C:/ceid7/software-eng/project/iphone.png")
        background_photo = ImageTk.PhotoImage(background_image)

        self.window.geometry(f"{background_photo.width()}x{background_photo.height()}")

        canvas = tk.Canvas(self.window, width=background_photo.width(), height=background_photo.height())
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=background_photo, anchor="nw")

        style = ttk.Style()
        style.configure("My.TFrame", background="#FFEBD6")

        frame = ttk.Frame(canvas, style="My.TFrame")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        self.characteristic_vars = [tk.IntVar() for _ in self.characteristics]

        style.configure("TCheckbutton", background="#FFEBD6", foreground="black", font=("Helvetica", 12))

        cols = 3
        frame = ttk.Frame(canvas, style="My.TFrame")
        frame.place(relx=0.5, rely=0.4, anchor="center")

        title_label = ttk.Label(frame, text="Interests", font=("Helvetica", 16))
        title_label.grid(row=0, columnspan=cols, pady=10)

        for i, characteristic in enumerate(self.characteristics):
            row, col = divmod(i + 3, cols)
            ttk.Checkbutton(frame, text=characteristic, variable=self.characteristic_vars[i], style="TCheckbutton").grid(row=row,
                                                                                                                        column=col,
                                                                                                                        sticky='w',
                                                                                                                        padx=5,
                                                                                                                        pady=5)

        self.rating_label = ttk.Label(frame, text="Rating:")
        self.rating_label.grid(row=len(self.characteristics) // cols + 1, column=0, padx=5, pady=5)
        self.rating_entry = ttk.Entry(frame)
        self.rating_entry.grid(row=len(self.characteristics) // cols + 1, column=1, padx=5, pady=5)

        self.additional_needs_label = ttk.Label(frame, text="Additional Needs:")
        self.additional_needs_label.grid(row=len(self.characteristics) // cols + 2, column=0, padx=5, pady=5)
        self.filter_additional_needs = ttk.Entry(frame)
        self.filter_additional_needs.grid(row=len(self.characteristics) // cols + 2, column=1, padx=5, pady=5)

        self.start_date_label = ttk.Label(frame, text="Start Date (YYYY-MM-DD):")
        self.start_date_label.grid(row=len(self.characteristics) // cols + 3, column=0, padx=5, pady=5)
        self.start_date_entry = ttk.Entry(frame)
        self.start_date_entry.grid(row=len(self.characteristics) // cols + 3, column=1, padx=5, pady=5)

        self.finish_date_label = ttk.Label(frame, text="Finish Date (YYYY-MM-DD):")
        self.finish_date_label.grid(row=len(self.characteristics) // cols + 4, column=0, padx=5, pady=5)
        self.finish_date_entry = ttk.Entry(frame)
        self.finish_date_entry.grid(row=len(self.characteristics) // cols + 4, column=1, padx=5, pady=5)

        self.travelers_label = ttk.Label(frame, text="Number of Travelers:")
        self.travelers_label.grid(row=len(self.characteristics) // cols + 5, column=0, padx=5, pady=5)
        self.travelers_entry = ttk.Entry(frame)
        self.travelers_entry.grid(row=len(self.characteristics) // cols + 5, column=1, padx=5, pady=5)

        self.budget_label = ttk.Label(frame, text="Budget:")
        self.budget_label.grid(row=len(characteristics) // cols + 6, column=0, padx=5, pady=5)
        self.budget_entry = ttk.Entry(frame)
        self.budget_entry.grid(row=len(characteristics) // cols + 6, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Find Destinations", command=lambda: Destination.find_destinations(
            self.characteristic_vars, self.characteristics, self.rating_entry, self.filter_additional_needs,
            self.start_date_entry, self.finish_date_entry, self.travelers_entry, self.budget_entry,
            self.destinations, Filter.save_filter_to_db, display_destinations_page
        )).grid(row=len(self.characteristics), column=0, columnspan=2)

        rating_label = ttk.Label
        self.window.mainloop()


if __name__ == "__main__":
    window = tk.Tk()
    FreeBirdApp(window)
    window.mainloop()
