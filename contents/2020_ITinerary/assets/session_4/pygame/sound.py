import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
color = (0, 0, 0)

bg = pygame.mixer.Sound("bensound-cute.mp3")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        print(pygame.mouse.get_pressed(3))

    screen.fill(color)
    pygame.display.flip()
    clock.tick(60)




