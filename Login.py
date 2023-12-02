

from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, StringVar





window = Tk()
window.title("K-Learning")

window_width = 1400
window_height = 800
window.geometry(f"{window_width}x{window_height}")
window.configure(bg = "#FFFFFF")


def exit():
    print("button_3 Clicked")
    window.destroy()
def Login(window):
    username = StringVar()
    password = StringVar()
    def submit(*args):
        print("button_2 clicked")
        print (username.get())
        print (password.get())



        # entry_1.delete(0, 'end')

    # username.trace("w", mywarWritten)    
    main_frame = Frame(window, width=f"{window_width}", height=f"{window_height}",bg = "#3d3d3d")
    main_frame.pack()
    canvas = Canvas(
        main_frame,
        bg = "#000000",
        height = window_height,
        width = window_width,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    window.image_image_1 = image_image_1 = PhotoImage(
        file=r"assets\Login\image_1.png")
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
        file="assets/Login/button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=826.0,
        y=606.0,
        width=129.0,
        height=37.0
    )

    window.button_image_2 =button_image_2 = PhotoImage(
        file="assets/Login/button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: submit(),
        relief="flat"
    )
    button_2.place(
        x=452.0,
        y=521.0,
        width=503.0,
        height=72.0
    )

    window.entry_image_1 =entry_image_1 = PhotoImage(
        file="assets/Login/entry_1.png")
    entry_bg_1 = canvas.create_image(
        703.5,
        328.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Calibri",24),
        textvariable=username
    )
    entry_1.place(
        x=458.0,
        y=300.0,
        width=491.0,
        height=58.0
    )

    canvas.create_text(
        457.0,
        263.0,
        anchor="nw",
        text="Username",
        fill="#000000",
        font=("Ubuntu Bold", 26 * -1)
    )

    window.entry_image_2 =entry_image_2 = PhotoImage(
        file="assets/Login/entry_2.png")
    entry_bg_2 = canvas.create_image(
        703.5,
        439.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Calibri",24),
        show="*",
        textvariable=password
    )
    entry_2.place(
        x=458.0,
        y=410.0,
        width=491.0,
        height=58.0
    )

    canvas.create_text(
        457.0,
        373.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Ubuntu Bold", 26 * -1)
    )

    window.image_image_2 =image_image_2 = PhotoImage(
        file="assets/Login/image_2.png")
    image_2 = canvas.create_image(
        699.0,
        179.0,
        image=image_image_2
    )

    window.button_image_3 =button_image_3 = PhotoImage(
        file="assets/Login/button_3.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: exit(),
        relief="flat",
    )
    button_3.place(
        x=47.0,
        y=9.0,
        width=120.0,
        height=40.0
    )

Login(window)
window.resizable(False, False)
window.mainloop()
