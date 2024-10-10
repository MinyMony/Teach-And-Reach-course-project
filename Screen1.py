import consts
from tkinter import *

root = Tk()

root.title('Teach and Reach')
root.geometry(f'{consts.WINDOW_WIDTH}x{consts.WINDOW_HEIGHT}')
root.configure(background='lightblue')


def teacher_clicked():
    return 'Teacher'

def student_clicked():
    return 'Student'


def create_teacher_button(root):
    button = Button(root,
                    text='Teacher',
                    command=teacher_clicked(),
                    activebackground='blue',
                    activeforeground="white",
                    anchor="center",
                    bd=3,
                    bg="royalblue",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",
                    padx=20,
                    pady=30,
                    width=20,
                    wraplength=100)

    button.pack(padx=100, pady=70)


def create_student_button(root):
    button = Button(root,
                    text='Student',
                    command=student_clicked(),
                    activebackground='blue',
                    activeforeground="white",
                    anchor="center",
                    bd=3,
                    bg="royalblue",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",
                    padx=20,
                    pady=30,
                    width=20,
                    wraplength=100)

    button.pack(padx=100, pady=70)


def create_screen_1(root):
    create_student_button(root)
    create_teacher_button(root)
    root.mainloop()


def open_teacher():
    newWindow = Toplevel(root)
    newWindow.title('Teach and Reach')
    root.geometry(f'{consts.WINDOW_WIDTH}x{consts.WINDOW_HEIGHT}')
    root.configure(background='lightblue')
    Label(newWindow,
          text="Hello Student").pack()


def open_student():
    newWindow = Toplevel(root)
    newWindow.title('Teach and Reach')
    root.geometry(f'{consts.WINDOW_WIDTH}x{consts.WINDOW_HEIGHT}')
    root.configure(background='lightblue')
    Label(newWindow,
          text="Hello Student").pack()

