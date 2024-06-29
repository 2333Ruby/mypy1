import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((600, 500))
font = pygame.font.Font(None, 100)
number = '0'

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                number = '1'
                print('1')
            elif event.key == pygame.K_2:
                number = '2'
            elif event.key == pygame.K_3:
                number = '3'
            elif event.key == pygame.K_4:
                number = '4'
            elif event.key == pygame.K_RETURN:
                number = 'RETURN'

    screen.fill((0, 0, 200))
    imgText = font.render(number, True, (255, 255, 255))
    screen.blit(imgText, (300, 200))
    pygame.display.update()