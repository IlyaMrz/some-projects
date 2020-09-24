import pygame
from pygame.draw import *

# После импорта библиотеки, необходимо её инициализировать:
pygame.init()
x1, y1, x2, y2 = 220, 325, 480, 390

# И создать окно:
screen = pygame.display.set_mode((700, 500))
circle(screen, (213, 255, 0), (350, 250), 230)
circle(screen, (250, 245, 245), (200, 200), 100)
circle(screen, (250, 245, 245), (200, 200), 100)
circle(screen, (205, 0, 5), (230, 200), 47)
circle(screen, (0, 0, 0), (235, 200), 7)
circle(screen, (250, 245, 245), (500, 200), 100)
circle(screen, (205, 0, 5), (530, 200), 47)
circle(screen, (0, 0, 0), (535, 200), 7)
rect(screen, (0, 0, 0), (x1, y1, x2-x1, y2-y1))
# здесь будут рисоваться фигуры
# ...

# после чего, чтобы они отобразились на экране, экран нужно обновить:
pygame.display.update()
clock = pygame.time.Clock()
clock.tick(30)
# Эту же команду нужно будет повторять, если на экране происходят изменения.

# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
# Пока единственное событие, которое нас интересует - выход из программы.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
