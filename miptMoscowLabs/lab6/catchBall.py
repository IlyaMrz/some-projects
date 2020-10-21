import pygame
from pygame.draw import *
from random import randint
import askname
playerName = askname.main()
# pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


points = 0


def new_ball():
    global x, y, r
    x = randint(100, 1050)
    y = randint(100, 800)
    r = randint(99, 130)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def new_rect():  # points for rect not implemented
    global x2, y2, x3, y3
    x2 = randint(50, 1050)
    y2 = randint(100, 800)
    x3 = randint(50, 1050)
    y3 = randint(100, 800)
    color = COLORS[randint(0, 5)]
    rect(screen, color, (x2, y2, x3, y3))


def click(event):
    global points
    ex, ey = event.pos
    if (ey - y)**2 + (ex - x)**2 <= r**2:
        print('YES!')
        points += 1
        print(points)
    else:
        print(event.pos)
        print('Missed')


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
            print('Click!')
    new_ball()
    new_ball()
    new_rect()
    pygame.display.update()
    screen.fill(BLACK)


print(f'Player name: {playerName}. Score: {points}')
pygame.quit()
