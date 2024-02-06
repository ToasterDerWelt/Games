import pygame
import random
import time

window_x = 377
window_y = 350
map = [[0 for _ in range(6)] for _ in range(7)]
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)
orange = pygame.Color(255, 125, 0)
pink = pygame.Color(255, 0, 255)
lila = pygame.Color(190, 0, 255)
pygame.init()
# Initialise game window
pygame.display.set_caption("Vier gewinnt")
game_window = pygame.display.set_mode((window_x, window_y))
size = (window_x, window_y)
screen = pygame.display.set_mode(size)
screen.fill(white)
pygame.display.update()
hoehe = 300
change = 0
sollChange = True
while True:
    img = pygame.image.load("dinoLegDown.png")
    screen.blit(img, (20, hoehe - change))
    time.sleep(0.1)
    pygame.display.update()
    screen.fill(white)
    img = pygame.image.load("dinoLegUp.png")
    screen.blit(img, (20, hoehe - change))
    time.sleep(0.1)
    pygame.display.update()
    fps.tick(60)
    screen.fill(white)
    if sollChange:
        change -= 10
        if change <= -100:
            sollChange = False
    elif not sollChange:
        change += 10
        if change >= 100:
            sollChange = True
