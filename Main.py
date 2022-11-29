import pygame, sys, Elements, os

from pygame.locals import *
pygame.init()

hardwareDisp = (pygame.display.Info().current_w, pygame.display.Info().current_h)
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
surface = pygame.display.set_mode((1920, 1080), RESIZABLE)

#Defining test menu
options = ['FULLSCREEN', 'BORDERLESS', 'WINDOWED']
drop = Elements.dropdown(options,(150,50),(surface.get_width() / 2, surface.get_height() / 2),'WINDOWED')
drop.style(('#FFFFFF', '#777777'), ('#000000', '#222222'), 'arialblack', 12)

Fullscreen = False
Borderless = False
Windowed = True

while True:
    
    surface.fill((50,50,50))
    
    #DROPDOWN LOGIC
    drop.checkClick(surface,True, '#888888')
    
    if drop.getActive() == 'FULLSCREEN':
        if Fullscreen == False:
            surface = pygame.display.set_mode((hardwareDisp), pygame.FULLSCREEN)
            Fullscreen = True
    else:
        Fullscreen = False
        
    if drop.getActive() == 'BORDERLESS':
        if Borderless == False:
            surface = pygame.display.set_mode((hardwareDisp), NOFRAME)
            Borderless = True
    else:
        Borderless = False
    
    if drop.getActive() == 'WINDOWED':
        if Windowed == False:
            surface = pygame.display.set_mode((1920,1080), RESIZABLE)
            Windowed = True
    else:
        Windowed = False
        
        
    #SCREEN LOGIC

    pygame.display.update()

    #EVENT LOGIC
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN:
            pygame.quit()
            sys.exit()
        if event.type == VIDEORESIZE:
            if Fullscreen == False:
                surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
