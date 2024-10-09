import pygame
import consts

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def create_opening_screen():
    pygame.display.set_caption('Teach an Reach')
    screen.fill(consts.BORDER_COLOR)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



