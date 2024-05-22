import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("FreeBird")
        
        # Load and set the background image
        self.background_image = Image.open("image.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        
        # Set window size to match the background image
        self.root.geometry(f"{self.background_photo.width()}x{self.background_photo.height()}")
        
        # Create a canvas for the background image
        self.canvas = tk.Canvas(self.root, width=self.background_photo.width(), height=self.background_photo.height())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        self.ShowAskUser()

        self.root.mainloop()

    def ShowAskUser(self):
        label = tk.Label(self.root, text="Do you want to see Events?", font=('Arial', 14), bg='#FFEBED')
        yes_button = tk.Button(self.root, text="Yes", command=self.ShowQuestions)
        no_button = tk.Button(self.root, text="No", command=self.root.quit)

        # Add widgets to the canvas
        self.canvas.create_window(150, 150, window=label)
        self.canvas.create_window(50, 250, window=yes_button)
        self.canvas.create_window(150, 250, window=no_button)

    def ShowQuestions(self):
        self.root.withdraw()
        self.questionnaire_window = tk.Toplevel()
        self.questionnaire_window.title("Questionnaire")
        self.questionnaire_window.geometry("800x600")

        self.questionnaire_canvas = tk.Canvas(self.questionnaire_window, width=self.background_photo.width(), height=self.background_photo.height())
        self.questionnaire_canvas.pack(fill="both", expand=True)
        self.questionnaire_canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        label = tk.Label(self.questionnaire_window, text="Please fill out the questionnaire", font=('Arial', 14), bg='#FFEBED')
        self.questionnaire_canvas.create_window(200, 125, window=label)

        self.create_questionnaire()

    def create_questionnaire(self):
        categories = {
            "Music": ["Rock", "Pop", "Jazz", "Classical"],
            "Sports": ["Basketball", "Tennis", "Football", "Swimming"],
            "Art": ["Painting", "Sculpture", "Photography", "Drawing"]
        }

        self.check_vars = {}
        
        y_position = 150  # Starting y position for categories

        for category, items in categories.items():
            category_label = tk.Label(self.questionnaire_window, text=category, font=('Arial', 12), bg='#FFEBED')
            self.questionnaire_canvas.create_window(100, y_position, window=category_label)
            y_position += 30

            for item in items:
                var = tk.BooleanVar()
                self.check_vars[item] = var
                checkbutton = tk.Checkbutton(self.questionnaire_window, text=item, variable=var, bg='#FFEBED')
                self.questionnaire_canvas.create_window(100, y_position, window=checkbutton)
                y_position += 30

        submit_button = tk.Button(self.questionnaire_window, text="Submit", command=self.Register)
        self.questionnaire_canvas.create_window(100, y_position + 20, window=submit_button)

    def Register(self):
        questionpaper = [item for item, var in self.check_vars.items() if var.get()]
        messagebox.showinfo("Selected Items", f"You selected: {', '.join(questionpaper)}")
        self.questionnaire_window.destroy()
        self.root.quit()
        return questionpaper

if __name__ == "__main__":
    MyApp()
