from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, StringVar


from Login import Login
from Vocab import Vocab


window = Tk()
window.title("K-Learning")

window_width = 1400
window_height = 800
window.geometry(f"{window_width}x{window_height}")
window.configure(bg = "#FFFFFF")

def exit():
    print("button_3 Clicked")
    window.destroy()


Vocab(window, window_width, window_height)

window.resizable(False, False)
window.mainloop()