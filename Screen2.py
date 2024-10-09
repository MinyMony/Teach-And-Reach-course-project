import pygame
import consts
import tkinter
from Screen1 import screen

screen.fill(consts.BACKGROUND_COLOR)


def teacher_screen():
    pass


def student_screen():
    pass


def create_second_screen():
    pygame.display.set_caption('Teach and Reach')
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False












