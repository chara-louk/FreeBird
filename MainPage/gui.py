from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"K:\CEID\TL\CODE\MainPage\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainPage:

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
        318.0,
        738.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        506.0,
        731.0,
        image=image_image_2
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
        x=204.0,
        y=311.0,
        width=177.0,
        height=48.0
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
        x=16.0,
        y=311.0,
        width=177.0,
        height=48.0
    )

    canvas.create_text(
        8.0,
        119.0,
        anchor="nw",
        text="Ready to organize ",
        fill="#000000",
        font=("RobotoRoman Bold", 25 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        193.0,
        75.0,
        image=image_image_3
    )

    canvas.create_text(
        60.0,
        818.0,
        anchor="nw",
        text="home",
        fill="#000000",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        131.0,
        818.0,
        anchor="nw",
        text="chat",
        fill="#000000",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        186.0,
        818.0,
        anchor="nw",
        text="your trips",
        fill="#000000",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        277.0,
        818.0,
        anchor="nw",
        text="more",
        fill="#000000",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_rectangle(
        17.0,
        199.0,
        350.0,
        200.0,
        fill="#522A27",
        outline="")

    canvas.create_rectangle(
        26.0,
        434.0,
        359.0,
        435.0,
        fill="#522A27",
        outline="")

    canvas.create_text(
        27.0,
        395.0,
        anchor="nw",
        text="Popular",
        fill="#000000",
        font=("RobotoRoman Bold", 38 * -1)
    )

    canvas.create_rectangle(
        34.0,
        448.0,
        359.0,
        600.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        33.0,
        607.0,
        358.0,
        753.0,
        fill="#D9D9D9",
        outline="")

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        154.0,
        788.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        223.0,
        791.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        84.0,
        784.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        298.0,
        787.0,
        image=image_image_7
    )

    canvas.create_text(
        8.0,
        148.0,
        anchor="nw",
        text="your next trip?",
        fill="#000000",
        font=("RobotoRoman Bold", 25 * -1)
    )

    canvas.create_text(
        35.0,
        207.0,
        anchor="nw",
        text="Search\n",
        fill="#000000",
        font=("RobotoRoman Bold", 15 * -1)
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        195.0,
        16.0,
        image=image_image_8
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
        x=21.0,
        y=274.0,
        width=171.0,
        height=33.0
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
        x=200.0,
        y=274.0,
        width=174.0,
        height=33.0
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
        x=316.0,
        y=233.0,
        width=58.0,
        height=37.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        164.0,
        252.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#41521F",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=37.5,
        y=236.0,
        width=253.0,
        height=31.0
    )
    window.resizable(False, False)
    window.mainloop()
