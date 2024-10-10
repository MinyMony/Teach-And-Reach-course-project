import consts
from tkinter import *
import Screen2
import Screen3


def teacher_clicked(root):
    root.destroy()
    Screen3.create_teacher_screen()


def student_clicked(root):
    root.destroy()
    Screen2.create_student_screen()


def create_teacher_button(root):
    button = Button(root,
                    text='Teacher',
                    command=lambda: teacher_clicked(root),
                    activebackground='blue',
                    activeforeground="white",
                    anchor="center",
                    bd=3,
                    bg="royalblue",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Calibri", 16),
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

    button.pack(padx=100, pady=10)


def create_student_button(root):
    button = Button(root,
                    text='Student',
                    command=lambda: student_clicked(root),
                    activebackground='blue',
                    activeforeground="white",
                    anchor="center",
                    bd=3,
                    bg="royalblue",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Calibri", 16),
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

    button.pack(padx=100, pady=10)


def create_welcome_text(root):
    text_var = StringVar()
    text_var.set("Welcome to Teach and Reach!")
    label = Label(root,
                  textvariable=text_var,
                  height=5,
                  width=80,
                  bd=1,
                  background='lightblue',
                  font=("Calibri", 32, "bold"),
                  fg="black",
                  padx=2,
                  pady=2,
                  wraplength=400
                  )

    label.pack(pady=0)


def create_screen_1():
    root = Tk()

    root.title('Teach and Reach')
    root.geometry(f'{consts.WINDOW_WIDTH}x{consts.WINDOW_HEIGHT}')
    root.configure(background='lightblue')
    create_welcome_text(root)
    create_student_button(root)
    create_teacher_button(root)

    root.mainloop()