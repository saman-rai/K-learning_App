
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, StringVar
def Register(window, window_width, window_height):
    # getting values
    email = StringVar()
    username = StringVar()
    password = StringVar()
    
    
    def submit(*args):
        print("button_2 clicked")
        print (email.get())
        print (username.get())
        print (password.get())
        
        # error
        # errorMsg = "it is error"
        # canvas.itemconfig(error_canvas, text=errorMsg)


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
        file="assets/Register/image_1.png")
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

    window.button_image_1 =button_image_1 = PhotoImage(
        file="assets/Register/button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=863.0,
        y=637.0,
        width=85.0,
        height=37.0
    )
    # error msg
    error_canvas=canvas.create_text(
            460.0,
            525.0,
            anchor="nw",
            text="error",
            fill="#FF0000",
            font=("Ubuntu Bold", 22 * -1),
        )
    window.button_image_2 =button_image_2 = PhotoImage(
        file="assets/Register/button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: submit(),
        relief="flat"
    
    )
    button_2.place(
        x=452.0,
        y=555.0,
        width=503.0,
        height=72.0
    )
    

    window.entry_image_1 =entry_image_1 = PhotoImage(
        file="assets/Register/entry_1.png")
    entry_bg_1 = canvas.create_image(
        703.5,
        268.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Calibri",24),
        textvariable=email
    )
    entry_1.place(
        x=458.0,
        y=239.0,
        width=491.0,
        height=58.0
    )

    canvas.create_text(
        457.0,
        202.0,
        anchor="nw",
        text="Email",
        fill="#000000",
        font=("Ubuntu Bold", 26 * -1)
    )

    window.entry_image_2 =entry_image_2 = PhotoImage(
        file="assets/Register/entry_2.png")
    entry_bg_2 = canvas.create_image(
        703.5,
        378.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Calibri",24),
        textvariable=username
    )
    entry_2.place(
        x=458.0,
        y=349.0,
        width=491.0,
        height=58.0
    )

    canvas.create_text(
        457.0,
        312.0,
        anchor="nw",
        text="Username",
        fill="#000000",
        font=("Ubuntu Bold", 26 * -1)
    )

    window.entry_image_3 =entry_image_3 = PhotoImage(
        file="assets/Register/entry_3.png")
    entry_bg_3 = canvas.create_image(
        703.5,
        488.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Calibri",24),
        show="*",
        textvariable=password
    )
    entry_3.place(
        x=458.0,
        y=459.0,
        width=491.0,
        height=58.0
    )

    canvas.create_text(
        457.0,
        422.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Ubuntu Bold", 26 * -1)
    )

    window.image_image_2 = image_image_2 = PhotoImage(
        file="assets/Register/image_2.png")
    image_2 = canvas.create_image(
        700.0,
        143.0,
        image=image_image_2
    )

    window.button_image_3 = button_image_3 = PhotoImage(
        file="assets/Register/button_3.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: exit(),
        relief="flat"
    )
    button_3.place(
        x=47.0,
        y=9.0,
        width=120.0,
        height=40.0
    )
