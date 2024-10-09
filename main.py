import Screen1
import consts
from tkinter import *

root = Tk()

root.title('Teach and Reach')
root.geometry(f'{consts.WINDOW_WIDTH}x{consts.WINDOW_HEIGHT}')
root.configure(background='lightblue')

Screen1.create_student_button(root)
Screen1.create_teacher_button(root)

# הערהאחרת


root.mainloop()
