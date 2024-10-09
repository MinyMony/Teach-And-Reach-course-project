import consts
from Screen1 import screen
import tkinter as tk
list=[]

list=["name","subject","gender","age", "description"]


def text_box(text):
    window = tk.Tk()
    window.geometry("300x300")
    tk.Label(text=f"Enter {text}").pack()
    tk.Entry().pack()
    window.mainloop()




for i in range (5):
    text=list[i]
    m= text_box(text)


