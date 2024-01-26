import pygame
import time
import random
import sys


window_x = 377
window_y = 350

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption("Vier gewinnt")
game_window = pygame.display.set_mode((window_x, window_y))

size = (window_x, window_y)
screen = pygame.display.set_mode(size)


def draw_table():
    xVerschiebung = 10
    pygame.draw.rect(game_window, green, pygame.Rect(0, 0, 10, 350))
    pygame.draw.rect(game_window, green, pygame.Rect(367, 0, 10, 350))
    pygame.draw.rect(game_window, green, pygame.Rect(0, 0, 377, 10))
    pygame.draw.rect(game_window, green, pygame.Rect(0, 310, 377, 40))
    while xVerschiebung < 367:
        pygame.draw.rect(game_window, green, pygame.Rect(xVerschiebung, 10, 1, 300))
        xVerschiebung += 51


def newCircle(color, column):
    farb = red
    spalte = 0
    if not color:
        farb = blue
    match column:
        case 1:
            spalte = 25 + 10
        case 2:
            spalte = 76 + 10
        case 3:
            spalte = 127 + 10
        case 4:
            spalte = 178 + 10
        case 5:
            spalte = 229 + 10
        case 6:
            spalte = 280 + 10
        case 7:
            spalte = 331 + 10
    fallhoehe = 35
    change = 10
    pygame.draw.circle(game_window, farb, ((spalte + 1), fallhoehe), 23, 0)
    while fallhoehe <= (277 + 5):
        fallhoehe += change
        pygame.draw.circle(
            game_window, black, ((spalte + 1), (fallhoehe - change)), 23, 0
        )
        pygame.draw.circle(game_window, farb, ((spalte + 1), fallhoehe), 23, 0)
        pygame.display.update()
        fps.tick(60)


fps = pygame.time.Clock()
draw_table()

x = 1
player = True

while True:
    block = False
    try:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.KEYDOWN:
                # print("2")
                if event.key == pygame.K_1 and not block:
                    block = True
                    x = 1
                    newCircle(player, x)
                if event.key == pygame.K_2 and not block:
                    block = True
                    x = 2
                    newCircle(player, x)
                if event.key == pygame.K_3 and not block:
                    block = True
                    x = 3
                    newCircle(player, x)
                if event.key == pygame.K_4 and not block:
                    block = True
                    x = 4
                    newCircle(player, x)
                if event.key == pygame.K_5 and not block:
                    block = True
                    x = 5
                    newCircle(player, x)
                if event.key == pygame.K_6 and not block:
                    block = True
                    x = 6
                    newCircle(player, x)
                if event.key == pygame.K_7 and not block:
                    block = True
                    x = 7
                    newCircle(player, x)
        if block:
            pygame.display.update()
            fps.tick(10)
            player = not player
    except Exception as e:
        hi = 0
        print(e)
        pygame.quit()
        quit()
