import Screen1
import consts
from tkinter import *

#create screen 1
root = Tk()

root.title('Teach and Reach')
root.geometry(f'{consts.WINDOW_WIDTH}x{consts.WINDOW_HEIGHT}')
root.configure(background='lightblue')

Screen1.create_student_button(root)
Screen1.create_teacher_button(root)

root.mainloop()
