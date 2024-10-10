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

key_values = list(student_data.keys())

window = tk.Tk()
window.geometry(f'{consts.WINDOW_WIDTH}x{consts.WINDOW_HEIGHT}')
window.configure(background='lightblue')


def on_submit(input_name,input_gender,input_age,input_subject,input_short_explanation):
    list=[input_name,input_gender,input_age,input_subject,input_short_explanation]
    for i in range(len(student_data)):
        student_data[key_values[i]]=list[i]
    window.destroy()


gender_str = tk.StringVar()
age = tk.IntVar()
subject = tk.StringVar()
short_version = tk.StringVar()

name_str = tk.StringVar()
tk.Label(text=f"Enter {key_values[0]}").pack()
input_name = tk.Entry(window, textvariable=name_str)
input_name.pack()

gender_str = tk.StringVar()
tk.Label(text=f"Enter {key_values[1]}").pack()
input_gender = tk.Entry(window, textvariable=gender_str)
input_gender.pack()

age_str = tk.StringVar()
tk.Label(text=f"Enter {key_values[2]}").pack()
input_age = tk.Entry(window, textvariable=age_str)
input_age.pack()

subject_str = tk.StringVar()
tk.Label(text=f"Enter {key_values[3]}").pack()
input_subject = tk.Entry(window, textvariable=subject_str)
input_subject.pack()

short_explanation_str = tk.StringVar()
tk.Label(text=f"Enter {key_values[3]}").pack()
input_short_explanation = tk.Entry(window, textvariable=short_explanation_str)
input_short_explanation.pack()

exit_button = tk.Button(window, text="Submit", command=(lambda: on_submit(input_name.get(), input_gender.get(), input_age.get(),
                                                                          input_subject.get(), input_short_explanation.get())))
exit_button.pack(pady=20)
window.mainloop()

print(student_data)
