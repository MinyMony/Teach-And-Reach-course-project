from numpy.version import short_version

import consts
import tkinter as tk


student_data = {
    'Full Name': 0,
    'Gender': 0,
    'Age': 0,
    'Subject': 0,
    'Short Explanation': 0
}

window = tk.Tk()
window.geometry("300x300")

name_str = tk.StringVar()
gender_str=tk.StringVar()
age=tk.StringVar()
subject=tk.StringVar()
short_version=tk.StringVar()

str_list=[name_str,gender_str,age,subject,short_version]

def on_submit():
    print(name_str.get())
    window.destroy()


i=0

def text_box(dict):

        tk.Label(text=f"Enter {key}").pack()
        input = tk.Entry(window, textvariable=name_str)
        input.pack()
    exit_button = tk.Button(window, text="Submit", command=(lambda :on_submit()))
    exit_button.pack(pady=20)
    window.mainloop()


text_box(student_data)
