import consts
from Screen1 import screen
import tkinter as tk


window = tk.Tk()
window.geometry("300x300")
tk.Label(text="Enter Name").pack()
tk.Entry().pack()
window.mainloop()