import consts
import gtts
import time
from tkinter import *


root = Tk()

root.title('Teach and Reach')
root.geometry(f'{consts.WINDOW_WIDTH}x{consts.WINDOW_HEIGHT}')


# def text_to_speech():
#     tts = gtts.gTTS("Welcome to Teach and Reach")
#     tts.save('Welcome.mp3')
#     playsound3.playsound("Welcome.mp3")


def button_clicked():
    print("Button clicked!")


def create_button():

    button = Button(root,
                    text="Student",
                    command=button_clicked,
                    activebackground='blue',
                    activeforeground="white",
                    anchor="center",
                    bd=3,
                    bg="lightgray",
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
                    pady=5,
                    width=15,
                    wraplength=100)

    button.pack(padx=20, pady=20)

create_button()

root.mainloop()

