import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

color = (0, 0, 0)

mouse_toggle = False
last_mouse_pos = (0, 0)
my_rect = pygame.Rect(300, 300, 200, 200)
my_enemy = pygame.Rect(0, 0, 200, 200)
img = pygame.image.load("cat.png")
print(type(img))

my_font_1 = pygame.font.Font(None, 24)
my_font_2 = pygame.font.SysFont("Arial", 24)
print(type(my_font_1))


to_move = [0, 0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_move[0] += -10
            if event.key == pygame.K_RIGHT:
                to_move[0] += 10
            if event.key == pygame.K_UP:
                to_move[1] += -10
            if event.key == pygame.K_DOWN:
                to_move[1] += 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_move[0] -= -10
            if event.key == pygame.K_RIGHT:
                to_move[0] -= 10
            if event.key == pygame.K_UP:
                to_move[1] -= -10
            if event.key == pygame.K_DOWN:
                to_move[1] -= 10

    my_rect = my_rect.move(to_move[0], to_move[1])

    screen.blit(img, (200, 200, 300, 300))

    screen.fill(color)

    text1 = my_font_1.render("Hello, Pygame!", True, (0,255,0))
    screen.blit(text1, (0, 0, 1, 1))

    pygame.display.flip()
    clock.tick(60)



