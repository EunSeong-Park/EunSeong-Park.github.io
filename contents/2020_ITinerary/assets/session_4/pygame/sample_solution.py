import pygame
import random

class Poop:
    def __init__(self, x):
        self.rect = [x, -30, 30, 30]

    def fall(self, speed):
        self.rect[1] += speed


pygame.init()

bg = pygame.image.load("background.png")
temp = pygame.image.load("character.png")
temp2 = pygame.image.load("poop.png")

character = pygame.transform.scale(temp, (40, 40))
poop_img = pygame.transform.scale(temp2, (30, 30))
default_font = pygame.font.Font(None, 24)

screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

to_move = [0, 0]
my_rect = pygame.Rect(200, 560, 40, 40)
score = 0
poop_list = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_move[0] = to_move[0] - 3
            if event.key == pygame.K_RIGHT:
                to_move[0] = to_move[0] + 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_move[0] = to_move[0] + 3
            if event.key == pygame.K_RIGHT:
                to_move[0] = to_move[0] - 3

    if 0 < my_rect.x + to_move[0] + my_rect.w // 2 < screen.get_width():
        my_rect = my_rect.move(to_move[0], 0)

    if random.randint(1, 100) > 97:
        poop_list.append(Poop(random.randint(0, 400)))

    screen.blit(bg, [0, 0, 400, 600])
    screen.blit(character, my_rect)

    for i in poop_list:
        i.fall(random.randint(10, 15))
        screen.blit(poop_img, i.rect)
        if my_rect.colliderect(i.rect):
            pygame.quit()
            print("GAME OVER! Your total score is...", score)
            exit()
        if i.rect[1] > 600:
            poop_list.remove(i)
            del i

    score = score + 1
    score_txt = default_font.render("Score: " + str(score), True, (0,0,0))
    screen.blit(score_txt, (0,0,1,1))

    pygame.display.flip()
    clock.tick(60)

