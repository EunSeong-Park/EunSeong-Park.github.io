import pygame

class Wall:
    # rect is just 4 tuple, not Rect
    def __init__(self, rect, color=(0,0,255)):
        # rect
        self.rect = pygame.Rect(rect)

        # if we step on the upper side, then it should jump
        # otherwise, just blocked..
        tmp = self.rect.copy()
        tmp.h = 5
        self.upperrect = tmp
        self.color = color

# Some initialization
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

ball = pygame.Rect(200, 200, 10, 10)
to_move = [0, 0]
CONST_GRAVITY = 1

# list for Walls. (for easy managing)
wall_list = [Wall((0, 300, 300, 180)), Wall((450, 300, 190, 180))]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()  # almost (not entirely) same with sys.exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_move[0] += -10
            if event.key == pygame.K_RIGHT:
                to_move[0] += 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_move[0] -= -10
            if event.key == pygame.K_RIGHT:
                to_move[0] -= 10

    # gravity applied, it works both for up / down situation.
    to_move[1] += CONST_GRAVITY

    for i in wall_list:
        if ball.colliderect(i.rect):
            # read comments in class Wall.
            if ball.colliderect(i.upperrect):
                to_move[1] -= 30 # jump!
            else:
                to_move[0] = 0 # you cannot pierce the wall

    # if you fall...
    if ball.y >= screen.get_height():
        print("Gameover")
        pygame.quit()
        quit()

    ball.x += to_move[0]
    ball.y += to_move[1]

    screen.fill((0, 0, 0))

    for i in wall_list:
        pygame.draw.rect(screen, i.color, i.rect, width=0)
    pygame.draw.circle(screen,
                       (255, 0, 0),
                       (ball.x + 5, ball.y + 5),
                       5, width=0)
    pygame.display.flip()
    clock.tick(30)
