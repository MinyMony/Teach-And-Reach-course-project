import consts
from Screen1 import screen
import tkinter as tk
list=[]

list=["name","subject","gender","age", "description"]


def text_box(text,ending_text):
    window = tk.Tk()
    window.geometry("300x300")
    tk.Label(text=f"Enter {text}").pack()
    tk.Entry().pack()
    exit_button = tk.Button(window, text=ending_text, command=window.destroy)
    exit_button.pack(pady=20)
    window.mainloop()




for i in range (5):
    text=list[i]
    if i!=4:
        text_box(text,"Next")
    else:
        text_box(text, "Exit")


