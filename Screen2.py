import consts
import tkinter as tk
import teachers


def text_box(dict):
    window = tk.Tk()
    window.geometry("300x300")
    for key in dict:
        tk.Label(text=f"Enter {key}").pack()
        tk.Entry().pack()
    exit_button = tk.Button(window, text="Submit", command=window.destroy)
    exit_button.pack(pady=20)
    window.mainloop()







text_box(teachers.student_data)



