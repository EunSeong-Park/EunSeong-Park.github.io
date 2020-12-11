import pygame
import random

class Poop:
    def __init__(self, x):
        self.rect = [x, -30, 30, 30]

    def fall(self, speed):
        self.rect[1] += speed


pygame.init()

bg = pygame.image.load("../background.png")
temp = pygame.image.load("../character.png")
temp2 = pygame.image.load("../poop.png")
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
            quit()  # almost (not entirely) same with sys.exit
        '''
        keyboard event handling (for move)
        '''

    '''
    character move
    '''

    '''
    generate poop
    '''

    '''
    show background / character
    '''


    '''
    Falling Poop
    '''

    '''
    Score increase/show + update screen
    '''

    '''
    clock tick
    '''

