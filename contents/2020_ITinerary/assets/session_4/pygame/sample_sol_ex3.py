import pygame

class Wall:
    # rect is just 4 tuple, not Rect
    def __init__(self, rect, color=(0,0,255)):
        # rect
        self.rect = pygame.Rect(rect)
        self.color = color

class Coin:
    def __init__(self, rect, color=(255,255,0)):
        self.rect = pygame.Rect(rect)
        self.color = color

# single line coin generator
# 2-tuple, 2-tuple, int
def CoinGenerator(start, end, num):
    if start[0] == end[0]: # x-direction
        dist_unit = (end[1] - start[1]) // num
        return [Coin((start[0], start[1] + dist_unit * k, 5, 5))
                for k in range(num)]

    elif start[1] == end[1]:
        dist_unit = (end[0] - start[0]) // num
        return [Coin((start[0] + dist_unit * l, start[1], 5, 5))
                for l in range(num)]
    else:
        print("invalid")

# Some initialization
pygame.init()
screen = pygame.display.set_mode((320, 240))
clock = pygame.time.Clock()

ball = pygame.Rect(10, 10, 40, 40)
to_move = [0, 0]
CONST_GRAVITY = 1

# list for Walls. (for easy managing)
wall_list = [Wall((0, 0, 10, 240)),
             Wall((0, 0, 320, 10)),
             Wall((0, 230, 320, 10)),
             Wall((310, 0, 10, 240)),
             Wall((260, 50, 10, 140)),
             Wall((50, 50, 10, 140)),
             Wall((50, 50, 220, 10)),
             Wall((50, 100, 10, 140)),
             Wall((210, 100, 10, 140)),
             Wall((160, 100, 10, 90)),
             Wall((100, 100, 10, 90)),
             Wall((100, 100, 60, 10)),
             Wall((100, 180, 60, 10))]

coin_list = CoinGenerator((30, 30), (310, 30), 14) +\
            CoinGenerator((30, 30), (30, 230), 10) +\
            CoinGenerator((290, 30), (290, 230), 10) +\
            CoinGenerator((240, 210), (290, 210), 3) +\
            CoinGenerator((240, 210), (240, 70), 7)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()  # almost (not entirely) same with sys.exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and to_move[1] == 0:
                to_move[0] = -10
            if event.key == pygame.K_RIGHT and to_move[1] == 0:
                to_move[0] = 10
            if event.key == pygame.K_UP and to_move[0] == 0:
                to_move[1] = -10
            if event.key == pygame.K_DOWN and to_move[0] == 0:
                to_move[1] = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_move[0] = 0
            if event.key == pygame.K_RIGHT:
                to_move[0] = 0
            if event.key == pygame.K_UP:
                to_move[1] = 0
            if event.key == pygame.K_DOWN:
                to_move[1] = 0

    for i in wall_list:
        if i.rect.colliderect([ball.x + to_move[0],
                               ball.y + to_move[1],
                               40, 40]):
            to_move = [0, 0]
    for j in coin_list:
        if j.rect.colliderect([ball.x + to_move[0],
                               ball.y + to_move[1],
                               40, 40]):
            coin_list.remove(j)
            if len(coin_list) == 0:
                print("Congratulations!")
                pygame.quit()
                quit()


    ball.x += to_move[0]
    ball.y += to_move[1]

    screen.fill((0, 0, 0))
    for i in wall_list:
        pygame.draw.rect(screen, i.color, i.rect, width=0)
    for i in coin_list:
        pygame.draw.rect(screen, i.color, i.rect, width=0)

    pygame.draw.circle(screen,
                       (255, 255, 0),
                       (ball.x + 20, ball.y + 20),
                       20, width=0)
    pygame.display.flip()
    clock.tick(30)
