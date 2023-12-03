


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage





def Quiz():
    
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 800,
        width = 1400,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file="assets/Quiz/image_1.png")
    image_1 = canvas.create_image(
        700.0,
        400.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        45.0,
        71.0,
        1354.0,
        730.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        524.0,
        157.0,
        anchor="nw",
        text="What is the meaning of ",
        fill="#000000",
        font=("Ubuntu Bold", 32 * -1)
    )

    canvas.create_text(
        676.0,
        232.0,
        anchor="nw",
        text="우유",
        fill="#000000",
        font=("Ubuntu Bold", 32 * -1)
    )

    button_image_1 = PhotoImage(
        file="assets/Quiz/button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=125.0,
        y=432.0,
        width=503.0,
        height=60.0
    )

    button_image_2 = PhotoImage(
        file="assets/Quiz/button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=125.0,
        y=531.0,
        width=503.0,
        height=60.0
    )

    button_image_3 = PhotoImage(
        file="assets/Quiz/button_3.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=771.0,
        y=432.0,
        width=503.0,
        height=60.0
    )

    button_image_4 = PhotoImage(
        file="assets/Quiz/button_4.png")
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=771.0,
        y=531.0,
        width=503.0,
        height=60.0
    )
