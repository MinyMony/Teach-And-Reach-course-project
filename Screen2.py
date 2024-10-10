import consts
import tkinter as tk

student_data = {
    'Full Name': 0,
    'Gender': 0,
    'Age': 0,
    'Subject': 0,
    'Short Explanation': 0
}





def on_submit(window, input):
    print(input.get())
    window.destroy()



def text_box(dict):
    window = tk.Tk()
    window.geometry(f'{consts.WINDOW_WIDTH}x{consts.WINDOW_HEIGHT}')
    window.configure(background='lightblue')

    for key in dict:
        tk.Label(text=f"Enter {key}", font=('Calibri',25),bg='lightblue').pack()
        input = tk.Entry(window)
        input.pack()
    exit_button = tk.Button(window, text="Submit", command=(lambda :on_submit(window, input)))
    exit_button.pack(pady=20)
    window.mainloop()


#
# window = tk.Tk()
# window.geometry("300x300")
#
# tk.Label(text=f"Enter Full Name").pack()
# input = tk.Entry(window)
# input.grid_bbox(row=1,column=0)
# exit_button = tk.Button(window, text="Submit", command=on_submit(window, input))
# exit_button.pack(pady=20)
# print(input.get())
#
# window.mainloop()
text_box(student_data)