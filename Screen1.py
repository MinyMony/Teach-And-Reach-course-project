import consts
from tkinter import *
import gtts
import time
import playsound3

# def text_to_speech():
#     tts = gtts.gTTS("Welcome to Teach and Reach")
#     tts.save('Welcome.mp3')
#     playsound3.playsound("Welcome.mp3")

isTeacher = False


def teacher_clicked():
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
                    padx=10,
                    pady=20,
                    width=15,
                    wraplength=100)

    button.pack(padx=100, pady=100)


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
                    padx=10,
                    pady=15,
                    width=15,
                    wraplength=100)

    button.pack(padx=100, pady=100)
