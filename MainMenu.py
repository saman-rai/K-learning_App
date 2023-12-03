

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, StringVar
from DB import connection,cursor
import ttkbootstrap as tb
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
        font=("Ubuntu Bold", 40 * -1, 'bold')
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



def Vocab(window, window_width, window_height, user_info):
    # username = user_info[2]
    userid = user_info[0]
    # print(userid)
    
    kr = StringVar()
    en = StringVar()

    def goto_MainMenu():
        main_frame.destroy()
        MainMenu(window, window_width, window_height, user_info)
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
    def get_vocab(userid):
        insert_query = '''
             SELECT * FROM Vocab WHERE userid = ?
        '''
        insert_values = (str(userid))
        cursor.execute(insert_query, insert_values)
        return cursor.fetchall()

    def update_vocab(vocabid,new_en, new_kr):
        print(new_en,new_kr)
        insert_query = '''
            UPDATE Vocab
            SET en = ?,
                kr = ?
            WHERE
                id=?
        '''
        insert_values = (new_en,new_kr,vocabid)
        try:
            cursor.execute(insert_query, insert_values)
            connection.commit()
            return True
        except:
            print("not updated")
            return False
    def delete_vocab(vocabid):
        print(vocabid)
        insert_query = f'''
            DELETE FROM Vocab
            WHERE
                id={vocabid}
        '''
       
        try:
            cursor.execute(insert_query)
            connection.commit()
            return True
        except:
            print("not deleted")
            return False
    def add_clicked():
        row_selected = False if select_row()=="" else True
        if not (kr.get()=="" and en.get()==""):
            if not row_selected:
            
                if add_vocab(kr.get(), en.get(), userid):
                    entry_1.delete(0, 'end')
                    entry_2.delete(0, 'end')
                    
                    update_tree()
           
            else:
                if update_vocab(select_row()[0],en.get(), kr.get()):
                    entry_1.delete(0, 'end')
                    entry_2.delete(0, 'end')
                    update_tree()
        else:
                print("empty")


    def select_row():
        return (my_tree.item(my_tree.focus()))['values']
 

    def update_row():
        row = select_row()
        if not row=="":
            kr.set(row[3])
            en.set(row[2])
          
    def delete_row():
        row = select_row()
        if not row=="":
            if delete_vocab(row[0]):
                update_tree()
            
    
    def update_tree():
        for i in my_tree.get_children():
           my_tree.delete(i)
        data = get_vocab(userid)
        print(data)
        for vocab in data:
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
        command=lambda: goto_MainMenu(),
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
    columns = ("id","userid",  "en", "kr")
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
        command=lambda: delete_row(),
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
