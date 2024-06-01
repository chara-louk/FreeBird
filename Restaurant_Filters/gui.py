
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\CEID\TL\Restaurant_Filters\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    195.0,
    16.0,
    image=image_image_1
)

canvas.create_text(
    29.0,
    100.0,
    anchor="nw",
    text="Range of prices",
    fill="#522A27",
    font=("RobotoRoman Regular", 20 * -1)
)

canvas.create_text(
    29.0,
    160.0,
    anchor="nw",
    text="Food",
    fill="#522A27",
    font=("RobotoRoman Regular", 20 * -1)
)

canvas.create_text(
    42.0,
    401.0,
    anchor="nw",
    text="Ratings",
    fill="#522A27",
    font=("RobotoRoman Regular", 20 * -1)
)

canvas.create_rectangle(
    29.0,
    90.0,
    362.0,
    91.0,
    fill="#522A27",
    outline="")

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
    x=128.0,
    y=319.0,
    width=79.0,
    height=22.0
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
    x=43.0,
    y=286.0,
    width=59.0,
    height=22.0
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
    x=109.0,
    y=284.0,
    width=67.0,
    height=22.0
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
    x=120.0,
    y=351.0,
    width=67.0,
    height=22.0
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
    x=193.0,
    y=352.0,
    width=67.0,
    height=22.0
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
    x=111.0,
    y=251.0,
    width=52.0,
    height=22.0
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
    x=42.0,
    y=351.0,
    width=69.0,
    height=22.0
)

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
    x=217.0,
    y=319.0,
    width=51.0,
    height=22.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=278.0,
    y=319.0,
    width=50.0,
    height=22.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=42.0,
    y=317.0,
    width=73.0,
    height=22.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=282.0,
    y=216.0,
    width=49.0,
    height=22.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=187.0,
    y=284.0,
    width=59.0,
    height=22.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
)
button_13.place(
    x=42.0,
    y=216.0,
    width=75.0,
    height=22.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_14 clicked"),
    relief="flat"
)
button_14.place(
    x=121.0,
    y=216.0,
    width=76.0,
    height=22.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
)
button_15.place(
    x=201.0,
    y=216.0,
    width=72.0,
    height=22.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat"
)
button_16.place(
    x=43.0,
    y=182.0,
    width=59.0,
    height=22.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat"
)
button_17.place(
    x=121.0,
    y=182.0,
    width=59.0,
    height=22.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat"
)
button_18.place(
    x=191.0,
    y=182.0,
    width=71.0,
    height=22.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat"
)
button_19.place(
    x=272.0,
    y=182.0,
    width=59.0,
    height=22.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_20 clicked"),
    relief="flat"
)
button_20.place(
    x=249.0,
    y=283.0,
    width=89.0,
    height=22.0
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_21 clicked"),
    relief="flat"
)
button_21.place(
    x=43.0,
    y=251.0,
    width=59.0,
    height=22.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_22 clicked"),
    relief="flat"
)
button_22.place(
    x=176.0,
    y=251.0,
    width=73.0,
    height=22.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_23 clicked"),
    relief="flat"
)
button_23.place(
    x=262.0,
    y=251.0,
    width=69.0,
    height=22.0
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_24 clicked"),
    relief="flat"
)
button_24.place(
    x=151.0,
    y=508.0,
    width=115.0,
    height=22.0
)

button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_25 clicked"),
    relief="flat"
)
button_25.place(
    x=270.0,
    y=540.0,
    width=115.0,
    height=22.0
)

button_image_26 = PhotoImage(
    file=relative_to_assets("button_26.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_26 clicked"),
    relief="flat"
)
button_26.place(
    x=32.0,
    y=572.0,
    width=115.0,
    height=22.0
)

button_image_27 = PhotoImage(
    file=relative_to_assets("button_27.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_27 clicked"),
    relief="flat"
)
button_27.place(
    x=151.0,
    y=572.0,
    width=115.0,
    height=22.0
)

button_image_28 = PhotoImage(
    file=relative_to_assets("button_28.png"))
button_28 = Button(
    image=button_image_28,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_28 clicked"),
    relief="flat"
)
button_28.place(
    x=31.0,
    y=604.0,
    width=115.0,
    height=22.0
)

button_image_29 = PhotoImage(
    file=relative_to_assets("button_29.png"))
button_29 = Button(
    image=button_image_29,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_29 clicked"),
    relief="flat"
)
button_29.place(
    x=151.0,
    y=604.0,
    width=115.0,
    height=22.0
)

button_image_30 = PhotoImage(
    file=relative_to_assets("button_30.png"))
button_30 = Button(
    image=button_image_30,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_30 clicked"),
    relief="flat"
)
button_30.place(
    x=270.0,
    y=604.0,
    width=115.0,
    height=22.0
)

button_image_31 = PhotoImage(
    file=relative_to_assets("button_31.png"))
button_31 = Button(
    image=button_image_31,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_31 clicked"),
    relief="flat"
)
button_31.place(
    x=270.0,
    y=572.0,
    width=115.0,
    height=22.0
)

button_image_32 = PhotoImage(
    file=relative_to_assets("button_32.png"))
button_32 = Button(
    image=button_image_32,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_32 clicked"),
    relief="flat"
)
button_32.place(
    x=151.0,
    y=540.0,
    width=115.0,
    height=22.0
)

button_image_33 = PhotoImage(
    file=relative_to_assets("button_33.png"))
button_33 = Button(
    image=button_image_33,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_33 clicked"),
    relief="flat"
)
button_33.place(
    x=269.0,
    y=508.0,
    width=115.0,
    height=22.0
)

button_image_34 = PhotoImage(
    file=relative_to_assets("button_34.png"))
button_34 = Button(
    image=button_image_34,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_34 clicked"),
    relief="flat"
)
button_34.place(
    x=32.0,
    y=540.0,
    width=115.0,
    height=22.0
)

button_image_35 = PhotoImage(
    file=relative_to_assets("button_35.png"))
button_35 = Button(
    image=button_image_35,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_35 clicked"),
    relief="flat"
)
button_35.place(
    x=32.0,
    y=508.0,
    width=115.0,
    height=22.0
)

canvas.create_rectangle(
    29.0,
    90.0,
    362.0,
    91.0,
    fill="#522A27",
    outline="")

canvas.create_text(
    37.0,
    480.0,
    anchor="nw",
    text="Additional needs",
    fill="#522A27",
    font=("RobotoRoman Regular", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    151.5,
    137.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=121.0,
    y=121.0,
    width=61.0,
    height=30.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    319.5,
    133.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=289.0,
    y=117.0,
    width=61.0,
    height=30.0
)

canvas.create_text(
    63.0,
    132.0,
    anchor="nw",
    text="From:",
    fill="#000000",
    font=("RobotoRoman Bold", 14 * -1)
)

canvas.create_text(
    231.0,
    129.0,
    anchor="nw",
    text="To:",
    fill="#000000",
    font=("RobotoRoman Bold", 14 * -1)
)

button_image_36 = PhotoImage(
    file=relative_to_assets("button_36.png"))
button_36 = Button(
    image=button_image_36,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_36 clicked"),
    relief="flat"
)
button_36.place(
    x=19.0,
    y=46.0,
    width=111.92344665527344,
    height=44.0
)

button_image_37 = PhotoImage(
    file=relative_to_assets("button_37.png"))
button_37 = Button(
    image=button_image_37,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_37 clicked"),
    relief="flat"
)
button_37.place(
    x=174.0,
    y=420.0,
    width=59.0,
    height=31.0
)

button_image_38 = PhotoImage(
    file=relative_to_assets("button_38.png"))
button_38 = Button(
    image=button_image_38,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_38 clicked"),
    relief="flat"
)
button_38.place(
    x=36.0,
    y=421.0,
    width=59.0,
    height=31.0
)

button_image_39 = PhotoImage(
    file=relative_to_assets("button_39.png"))
button_39 = Button(
    image=button_image_39,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_39 clicked"),
    relief="flat"
)
button_39.place(
    x=105.0,
    y=420.0,
    width=59.0,
    height=31.0
)

button_image_40 = PhotoImage(
    file=relative_to_assets("button_40.png"))
button_40 = Button(
    image=button_image_40,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_40 clicked"),
    relief="flat"
)
button_40.place(
    x=243.0,
    y=420.0,
    width=59.0,
    height=31.0
)

button_image_41 = PhotoImage(
    file=relative_to_assets("button_41.png"))
button_41 = Button(
    image=button_image_41,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_41 clicked"),
    relief="flat"
)
button_41.place(
    x=312.0,
    y=420.0,
    width=59.0,
    height=31.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    416.0,
    1033.0,
    image=image_image_2
)

button_image_42 = PhotoImage(
    file=relative_to_assets("button_42.png"))
button_42 = Button(
    image=button_image_42,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_42 clicked"),
    relief="flat"
)
button_42.place(
    x=219.0,
    y=735.0,
    width=168.0,
    height=49.0
)
window.resizable(False, False)
window.mainloop()