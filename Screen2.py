import consts
import tkinter as tk
student_data = {
    'Full Name':0,
    'Gender': 0,
    'Age': 0,
    'Subject': 0,
    'Short Explanation': 0
}



def text_box(dict):
    window = tk.Tk()
    window.geometry("300x300")
    for key in dict:
        tk.Label(text=f"Enter {key}").pack()
        data= tk.StringVar()
        input=tk.Entry(window)
    exit_button = tk.Button(window, text="Submit", command=window.destroy)
    exit_button.pack(pady=20)
    window.mainloop()







text_box(student_data)



