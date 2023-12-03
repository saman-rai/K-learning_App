from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, StringVar

from DB import connection,cursor
import ttkbootstrap as tb
def add_vocab(kr, en, userid):
    insert_query = '''
            INSERT INTO Vocab(
                kr,
                en,
                userid
            )
            VALUES(
                ?,
                ?,
                ?
            )
        '''
    insert_values = (kr,en,userid)
    try:
        cursor.execute(insert_query, insert_values)
        connection.commit()
        print("data inserted")
        return True
    except:
        print("registered")
        return False
def Vocab(window, window_width, window_height, user_info):
    # username = user_info[2]
    userid = user_info[0]
    # print(userid)
    update_btn_clicked = False
    kr = StringVar()
    en = StringVar()


    vocab_data = [
        ("1", "a", "b"),
        ("1", "a", "b"),
        ("1", "a", "b"),
    ]




    def add_clicked():
       
        if not (kr.get()=="" and en.get()==""):
            if add_vocab(kr.get(), en.get(), userid):
                entry_1.delete(0, 'end')
                entry_2.delete(0, 'end')
                vocab_data.append(("1", "a", "b"))
                update_tree()
        else:
            print("empty")
    def select_row():
        return (my_tree.item(my_tree.focus()))['values']
 

    def update_row():
        update_btn_clicked = True if False else True
        row = select_row()
        if not row=="":
            # change_kr_en(row)
            kr.set(row[1])
            en.set(row[2])
            
    
    def update_tree():
        for i in my_tree.get_children():
           my_tree.delete(i)
        for vocab in vocab_data:
            my_tree.insert('', tb.END, values=vocab)

    
    # 
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
        file="assets/Vocab/image_1.png")
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

    window.button_image_1 = button_image_1 = PhotoImage(
        file="assets/Vocab/button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=53.0,
        y=9.0,
        width=120.0,
        height=40.0
    )

    window.button_image_2 = button_image_2 = PhotoImage(
        file="assets/Vocab/button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_clicked(),
        relief="flat"
    )
    button_2.place(
        x=1200.0,
        y=98.0,
        width=117.0,
        height=40.0
    )
# tree view
    # canvas.create_rectangle(
    #     81.0,
    #     163.0,
    #     1320.0,
    #     637.0,
    #     fill="#ff0000",
    #     outline="")
    columns = ("id", "kr", "en")
    my_tree = tb.Treeview(
        main_frame,
        bootstyle="success",
        columns=columns,
       
    )
    my_tree.place(
        x=81.0,
        y=163.0,
        width=1239.0,
        height=474.0,
    )
    my_tree["displaycolumns"]=("kr", "en")
    update_tree()
    

    # 
    window.button_image_3 = button_image_3 = PhotoImage(
        file="assets/Vocab/button_3.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3"),
        relief="flat"
    )
    button_3.place(
        x=81.0,
        y=658.0,
        width=503.0,
        height=45.0
    )

    window.entry_image_1 = entry_image_1 = PhotoImage(
        file="assets/Vocab/entry_1.png")
    entry_bg_1 = canvas.create_image(
        417.0,
        117.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Calibri",18),
        textvariable=kr
    )
    entry_1.place(
        x=254.0,
        y=99.0,
        width=323.0,
        height=40.0
    )

    canvas.create_text(
        179.0,
        104.0,
        anchor="nw",
        text="한글",
        fill="#000000",
        font=("Ubuntu Bold", 26 * -1)
    )

    window.entry_image_2 = entry_image_2 = PhotoImage(
        file="assets/Vocab/entry_2.png")
    entry_bg_2 = canvas.create_image(
        992.0,
        117.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Calibri",18),
        textvariable=en
    )
    entry_2.place(
        x=828.0,
        y=99.0,
        width=323.0,
        height=40.0
    )

    canvas.create_text(
        719.0,
        104.0,
        anchor="nw",
        text="English",
        fill="#000000",
        font=("Ubuntu Bold", 26 * -1)
    )

    window.button_image_4 = button_image_4 = PhotoImage(
        file="assets/Vocab/button_4.png")
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: update_row(),
        relief="flat"
    )
    button_4.place(
        x=814.0,
        y=658.0,
        width=503.0,
        height=45.0
    )
