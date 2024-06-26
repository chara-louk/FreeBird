from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"K:\CEID\TL\CODE\TourPackets\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class TourPackets:
    
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
        196.0,
        16.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        398.0,
        1069.0,
        image=image_image_2
    )

    canvas.create_rectangle(
        14.0,
        84.0,
        347.0,
        85.0,
        fill="#522A27",
        outline="")

    canvas.create_text(
        102.0,
        113.0,
        anchor="nw",
        text="Name Surname",
        fill="#000000",
        font=("Inter Bold", 25 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        196.0,
        16.0,
        image=image_image_3
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
        x=206.0,
        y=739.0,
        width=177.0,
        height=64.0
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
        x=6.0,
        y=41.0,
        width=341.0,
        height=44.0
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        194.0,
        193.0,
        image=image_image_4
    )

    canvas.create_text(
        102.0,
        113.0,
        anchor="nw",
        text="Name Surname",
        fill="#000000",
        font=("Inter Bold", 25 * -1)
    )

    canvas.create_rectangle(
        28.0,
        248.0,
        361.0,
        249.0,
        fill="#522A27",
        outline="")

    canvas.create_text(
        33.0,
        337.0,
        anchor="nw",
        text="Tour Packets",
        fill="#000000",
        font=("RobotoRoman Bold", 30 * -1)
    )

    canvas.create_rectangle(
        30.0,
        370.0,
        363.0,
        371.0,
        fill="#522A27",
        outline="")

    canvas.create_text(
        40.0,
        381.0,
        anchor="nw",
        text="Explore the nature of Iceland",
        fill="#41521F",
        font=("RobotoRoman Bold", 20 * -1)
    )

    canvas.create_text(
        40.0,
        516.0,
        anchor="nw",
        text="Visit the museums",
        fill="#41521F",
        font=("RobotoRoman Bold", 20 * -1)
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
        x=31.0,
        y=415.0,
        width=328.0,
        height=100.0
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
        x=29.0,
        y=547.0,
        width=328.0,
        height=109.0
    )

    canvas.create_text(
        70.0,
        249.0,
        anchor="nw",
        text="Email: name.username@gmaiil.com\nPhone: 69888888\nLanguages: English, German\nHours available: 10:00 pm - 17:00 am\n",
        fill="#000000",
        font=("RobotoRoman Bold", 15 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
