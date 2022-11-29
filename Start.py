import pygame, sys, Elements, os

from pygame.locals import *
pygame.init()

hardwareDisp = (pygame.display.Info().current_w, pygame.display.Info().current_h)
surface = pygame.display.set_mode((600, 700))
center = (surface.get_width() / 2), (surface.get_height() / 2)

Title = pygame.font.SysFont('Bebas Neue', 100)

Text = ('START',50, '#FFFFFF', 'Bebas Neue', True)
start = Elements.button(Text, (center[0], 275), (250,75), ('#6138F6','#FFFFFF'), (5,5))

while True:
    
    surface.fill((32,32,32))
    Elements.draw_text('LEAD CADET', Title, '#FFFFFF', surface, (center[0], 125))
    start.checkClick(surface,True)
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
