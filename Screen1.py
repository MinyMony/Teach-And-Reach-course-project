import pygame
import consts
import gtts
import time

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def text_to_speech():
    tts = gtts.gTTS("Welcome to Teach and Reach")
    tts.save('Welcome.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load("Welcome.mp3")
    pygame.mixer.music.play()
    time.sleep(2)


def create_opening_screen():
    pygame.display.set_caption('Teach and Reach')
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()
    text_to_speech()




    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


create_opening_screen()
