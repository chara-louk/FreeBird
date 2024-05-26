from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"K:\CEID\TL\CODE\TripBooked\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class TripBooked:
    
    window = Tk()

    window.geometry("390x844")
    window.configure(bg = "#FFEBD6")


    canvas = Canvas(
        window,
        bg = "#FFEBD6",
        height = 844,
        width = 390,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        426.0,
        1078.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=288.0,
        y=39.0,
        width=52.0,
        height=67.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        167.0,
        78.0,
        image=image_image_2
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=129.0,
        y=760.0,
        width=44.0,
        height=64.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=184.0,
        y=758.0,
        width=83.0,
        height=66.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=58.0,
        y=752.0,
        width=51.0,
        height=72.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=270.0,
        y=762.0,
        width=52.0,
        height=62.0
    )

    canvas.create_text(
        43.0,
        133.0,
        anchor="nw",
        text="Your trip has been booked ! ",
        fill="#000000",
        font=("RobotoRoman Bold", 24 * -1)
    )

    canvas.create_text(
        36.0,
        432.0,
        anchor="nw",
        text="Would you like to book a tour? ",
        fill="#000000",
        font=("RobotoRoman Bold", 30 * -1)
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=36.0,
        y=565.0,
        width=323.0,
        height=80.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=36.0,
        y=650.0,
        width=314.0,
        height=80.0
    )

    canvas.create_text(
        29.0,
        215.0,
        anchor="nw",
        text="check your profile to see your personalised calendar",
        fill="#000000",
        font=("RobotoRoman Regular", 17 * -1)
    )

    canvas.create_text(
        123.0,
        181.0,
        anchor="nw",
        text="download receipt",
        fill="#000000",
        font=("RobotoRoman Regular", 17 * -1)
    )

    canvas.create_rectangle(
        35.0,
        555.0,
        368.0,
        556.0,
        fill="#522A27",
        outline="")

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        x=173.0,
        y=469.0,
        width=177.0,
        height=63.0
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        195.0,
        16.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        193.0,
        341.0,
        image=image_image_4
    )
    window.resizable(False, False)
    window.mainloop()
