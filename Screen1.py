import consts
from tkinter import *
import time

is_Teacher = False


def teacher_clicked(is_Teacher):
    return True


def create_teacher_button(root):
    button = Button(root,
                    text='Teacher',
                    command=teacher_clicked,
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
                    command=teacher_clicked,
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
