import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

color = (0, 0, 0)

mouse_toggle = False
last_mouse_pos = (0, 0)

screen.fill(color)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not mouse_toggle:
                mouse_toggle = True
                last_mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if mouse_toggle:
                mouse_toggle = False
        if event.type == pygame.MOUSEMOTION and mouse_toggle:
            pygame.draw.aaline(screen,
                              (255, 255, 255),
                              last_mouse_pos,
                              pygame.mouse.get_pos(), True)
            last_mouse_pos = pygame.mouse.get_pos()

    pygame.display.flip()
    clock.tick(60)



