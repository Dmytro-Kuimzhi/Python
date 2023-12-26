import pygame
import sys
import random

FPS = 10
W = 1000
H = 800

WHITE = (255, 255, 255)
BLUE = (0, 0, 225)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

next_x = 100
next_y = 100
moment_x = 95
moment_y = 100
past_x = 90
past_y = 100
x_rect = random.randint(0, 990)
y_rect = random.randint(0, 790)
r = 2.5
c = 0

def worm_tail(next_x, next_y, moment_x, moment_y, past_x, past_y):
    pygame.draw.rect(sc, BLUE, (next_x, next_y, 5, 5))
    pygame.draw.rect(sc, RED, (moment_x, moment_y, 5, 5))
    pygame.draw.rect(sc, GREEN, (past_x, past_y, 5, 5))

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT and c != "right" and c != "left":
                c = "left"
            elif i.key == pygame.K_RIGHT and c != "left" and c != "right":
                c = "right"
            elif i.key == pygame.K_UP and c != "down" and c != "up":
                c = "up"
            elif i.key == pygame.K_DOWN and c != "up" and c != "down":
                c = "down"
            elif i.key == pygame.K_SPACE:
                c = 0

    if c != 0:
        past_x = moment_x
        past_y = moment_y
        moment_x = next_x
        moment_y = next_y

    if c == "left":
        next_x -= 5
    if c == "right":
        next_x += 5
    if c == "up":
        next_y -= 5
    if c == "down":
        next_y += 5

    if next_x - 1 < x_rect < next_x + 6 and next_y - 1 < y_rect < next_y + 6:
        x_rect = random.randint(10, 990)
        y_rect = random.randint(10, 790)

    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x_rect, y_rect), r)
    worm_tail(next_x, next_y, moment_x, moment_y, past_x, past_y)


    pygame.display.update()
    clock.tick(FPS)