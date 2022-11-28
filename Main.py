import pygame, sys

from pygame.locals import *
pygame.init()

surface = pygame.display.set_mode((1920, 1080), RESIZABLE)

while True:
    
    surface.fill((50,50,50))
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            