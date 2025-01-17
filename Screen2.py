from tkinter import ttk
import consts
import tkinter as tk
import functions
import teachers

student_data = {
    'Full Name': 0,
    'Gender': 0,
    'Age': 0,
    'Subject': 0,
    'Short Explanation': 0
}

key_values = list(student_data.keys())


def create_student_text(window):
    text_var = tk.StringVar()
    text_var.set("Hello Student! Enter your information")
    label = tk.Label(window,
                     textvariable=text_var,
                     height=5,
                     width=90,
                     bd=1,
                     background='lightblue',
                     font=("Calibri", 30, "bold"),
                     fg="black",
                     padx=2,
                     pady=2,
                     wraplength=300
                     )

    label.pack(pady=0)


def on_submit(input_name, input_gender, input_age, input_subject, input_short_explanation, window):
    list = [input_name, input_gender, input_age, input_subject, input_short_explanation]
    for i in range(len(student_data)):
        student_data[key_values[i]] = list[i]
    window.destroy()
    teachers.create_matching_teacher_screen(functions.match_teacher(student_data))


def create_student_screen():
    window = tk.Tk()
    window.geometry(f'{consts.WINDOW_WIDTH}x{consts.WINDOW_HEIGHT}')
    window.configure(background='lightblue')
    window.title('Teach and Reach')
    create_student_text(window)

    name_str = tk.StringVar()
    tk.Label(text=f"Enter {key_values[0]}", font=('Calibri', 20), background='lightblue').pack()
    input_name = tk.Entry(window, textvariable=name_str)
    input_name.pack()

    gender_str = tk.StringVar()
    input_gender = ttk.Combobox(window, textvariable=gender_str)
    input_gender['values'] = ('Female',
                              'Male', 'Non-Binary')
    tk.Label(text=f"Enter {key_values[1]}", font=('Calibri', 20), background='lightblue').pack()
    # input_gender = tk.Entry(window, textvariable=gender_str)
    input_gender.pack()

    age_int = tk.IntVar()
    tk.Label(text=f"Enter {key_values[2]}", font=('Calibri', 20), background='lightblue').pack()
    input_age = tk.Entry(window, textvariable=age_int)
    input_age.pack()

    subject_str = tk.StringVar()
    input_subject = ttk.Combobox(window, textvariable=subject_str)
    input_subject['values'] = ('Math',
                               'Science', 'Literature', 'History', 'Geography', 'Art', 'Music', 'Physics', 'Chemistry',
                               'Geography')
    tk.Label(text=f"Enter {key_values[3]}", font=('Calibri', 20), background='lightblue').pack()
    # input_subject = tk.Entry(window, textvariable=subject_str)
    input_subject.pack()
    # input_subject.pack()

    short_explanation_str = tk.StringVar()
    tk.Label(text=f"Enter {key_values[4]}", font=('Calibri', 20), background='lightblue', ).pack()
    input_short_explanation = tk.Entry(window, textvariable=short_explanation_str)
    input_short_explanation.pack()

    exit_button = tk.Button(window, text="Submit",
                            command=(lambda: on_submit(input_name.get(), input_gender.get(), input_age.get(),
                                                       input_subject.get(), input_short_explanation.get(), window)))
    exit_button.pack(pady=20)
    window.mainloop()
