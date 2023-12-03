

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, StringVar

from Vocab import Vocab

def MainMenu(window, window_width, window_height, user_info):
    username = user_info[2]
    def goto_vocab():
        main_frame.destroy()
        Vocab(window, window_width, window_height, user_info)
    main_frame = Frame(window, width=f"{window_width}", height=f"{window_height}",bg = "#3d3d3d")

    main_frame.pack()
    canvas = Canvas(
        main_frame,
        bg = "#FFFFFF",
        height = 800,
        width = 1400,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    window.image_image_1 = image_image_1 = PhotoImage(
        file="assets/MainMenu/image_1.png")
    image_1 = canvas.create_image(
        700.0,
        400.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        303.0,
        82.0,
        1098.0,
        718.0,
        fill="#FFFFFF",
        outline="")

    window.button_image_1 = button_image_1 = PhotoImage(
        file="assets/MainMenu/button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=452.0,
        y=421.0,
        width=503.0,
        height=72.0
    )

    window.button_image_2 =button_image_2 = PhotoImage(
        file="assets/MainMenu/button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=452.0,
        y=537.0,
        width=503.0,
        height=72.0
    )

    window.button_image_3 = button_image_3 = PhotoImage(
        file="assets/MainMenu/button_3.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: goto_vocab(),
        relief="flat"
    )
    button_3.place(
        x=452.0,
        y=294.0,
        width=503.0,
        height=72.0
    )

    canvas.create_text(
        545.0,
        168.0,
        anchor="nw",
        text=f"Welcome {username}",
        fill="#009788",
        font=("Ubuntu Bold", 40 * -1)
    )

    window.button_image_4 = button_image_4 = PhotoImage(
        file="assets/MainMenu/button_4.png")
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: exit(),
        relief="flat"
    )
    button_4.place(
        x=47.0,
        y=9.0,
        width=120.0,
        height=40.0
    )
