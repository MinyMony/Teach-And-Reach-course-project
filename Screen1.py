import consts
from tkinter import *
import Screen2


def teacher_clicked():
    pass


def student_clicked(root):
    root.destroy()
    Screen2.Screen2()



def create_teacher_button(root):
    button = Button(root,
                    text='Teacher',
                    command=lambda: teacher_clicked(),
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

    button.pack(padx=100, pady=10)


def create_screen_1():
    root = Tk()

    root.title('Teach and Reach')
    root.geometry(f'{consts.WINDOW_WIDTH}x{consts.WINDOW_HEIGHT}')
    root.configure(background='lightblue')
    create_welcome_text(root)
    create_student_button(root)
    create_teacher_button(root)

    root.mainloop()


def create_welcome_text(root):
    text_var = StringVar()
    text_var.set("Welcome to Teach and Reach!")
    label = Label(root,
                  textvariable=text_var,
                  height=5,
                  width=80,
                  bd=1,
                  background='lightblue',
                  font=("calibri", 30, "bold"),
                  fg="black",
                  padx=2,
                  pady=2,
                  wraplength=300
                  )

    label.pack(pady=0)



