from numpy.version import short_version

import consts
import tkinter as tk



def on_submit(input_name, input_gender, input_age, input_subject, input_short_explanation,student_data,key_values,window):
    list = [input_name, input_gender, input_age, input_subject, input_short_explanation]
    for i in range(len(student_data)):
        student_data[key_values[i]] = list[i]
    window.destroy()


def Screen2():

    teachers_data= {'Full Name': 0,
        'Gender': 0,
        'Subject': 0,
        'Age Range':0,
        'Phone Number': 0,
        'Short Explanation': 0}


    key_values = list(teachers_data.keys())

    window = tk.Tk()
    window.geometry(f'{consts.WINDOW_WIDTH}x{consts.WINDOW_HEIGHT}')
    window.configure(background='lightblue')

    name_str = tk.StringVar()
    tk.Label(window,text=f"Enter {key_values[0]}").pack()
    input_name = tk.Entry(window, textvariable=name_str)
    input_name.pack()

    gender_str = tk.StringVar()
    tk.Label(window,text=f"Enter {key_values[1]}").pack()
    input_gender = tk.Entry(window, textvariable=gender_str)
    input_gender.pack()

    age_int = tk.IntVar()
    tk.Label(window,text=f"Enter {key_values[2]}").pack()
    input_age = tk.Entry(window, textvariable=age_int)
    input_age.pack()

    subject_str = tk.StringVar()
    tk.Label(window,text=f"Enter {key_values[3]}").pack()
    input_subject = tk.Entry(window, textvariable=subject_str)
    input_subject.pack()

    short_explanation_str = tk.StringVar()
    tk.Label(window,text=f"Enter {key_values[4]}").pack()
    input_short_explanation = tk.Entry(window, textvariable=short_explanation_str)
    input_short_explanation.pack()

    exit_button = tk.Button(window, text="Submit",
                            command=(lambda: on_submit(input_name.get(), input_gender.get(), input_age.get(),
                                                       input_subject.get(), input_short_explanation.get(),
                                                       student_data,key_values,window)))
    exit_button.pack(pady=20)
    window.mainloop()

    print(student_data)