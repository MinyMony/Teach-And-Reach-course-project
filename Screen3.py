from tkinter import ttk
import consts
import tkinter as tk
import teachers

teachers_data = ['Full Name','Gender','Subject','Age Range', 'Phone Number','Short Explanation']

def on_submit(input_name, input_gender, input_subject, input_age_range, input_phone_number,input_short_explanation, window):
    teachers.addTeacher(input_name,input_gender,input_subject,input_age_range,input_phone_number,input_short_explanation)
    window.destroy()


def create_teacher_screen():
    window = tk.Tk()
    window.geometry(f'{consts.WINDOW_WIDTH}x{consts.WINDOW_HEIGHT}')
    window.configure(background='lightblue')
    window.title("Teachers Window")

    name_str = tk.StringVar()
    tk.Label(text=f"Enter {teachers_data[0]}", font=('Calibri', 20), background='lightblue').pack()
    input_name = tk.Entry(window, textvariable=name_str)
    input_name.pack()

    gender_str = tk.StringVar()
    input_gender = ttk.Combobox(window, textvariable=gender_str)
    input_gender['values'] = ('Female',
                              'Male', 'Non-Binary')
    tk.Label(text=f"Enter {teachers_data[1]}", font=('Calibri', 20), background='lightblue').pack()
    input_gender.pack()

    subject_str = tk.StringVar()
    input_subject = ttk.Combobox(window, textvariable=subject_str)
    input_subject['values'] = ('Math',
                               'Science', 'Literature', 'History', 'Geography', 'Art', 'Music', 'Physics', 'Chemistry',
                               'Geography')
    tk.Label(text=f"Enter {teachers_data[2]}", font=('Calibri', 20), background='lightblue').pack()
    # input_subject = tk.Entry(window, textvariable=subject_str)
    input_subject.pack()
    # input_subject.pack()

    age_range = tk.StringVar()
    tk.Label(text=f"Enter {teachers_data[3]}", font=('Calibri', 20), background='lightblue').pack()
    input_age_range = tk.Entry(window, textvariable=age_range)
    input_age_range.pack()

    phone_number = tk.StringVar()
    tk.Label(text=f"Enter {teachers_data[4]}", font=('Calibri', 20), background='lightblue').pack()
    input_phone_number = tk.Entry(window, textvariable=phone_number)
    input_phone_number.pack()

    short_explanation_str = tk.StringVar()
    tk.Label(text=f"Enter {teachers_data[5]}", font=('Calibri', 20), background='lightblue', ).pack()
    input_short_explanation = tk.Entry(window, textvariable=short_explanation_str)
    input_short_explanation.pack()

    exit_button = tk.Button(window, text="Submit",
                            command=(lambda: on_submit(input_name.get(), input_gender.get(), input_subject.get(),
                                                       input_age_range.get(), input_phone_number.get(),input_short_explanation.get(),
                                                       window)))
    exit_button.pack(pady=20)
    window.mainloop()

create_teacher_screen()





