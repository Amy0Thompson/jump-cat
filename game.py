import random #for RNG
import pygame
pygame.init()

white = (255, 255, 255)
black = (0 ,0, 0)
#colors

width = 500
height = 500
#dimensions

score = 0
player_x = 50
player_y = 200
fps = 60
background = white
timer = pygame.time.Clock()
#game variables

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jump Cat')
#game window

gameRunning = True
while gameRunning:
    timer.tick(fps)
    screen.fill(background)
    floor = pygame.draw.rect(screen, black [0, 200, width, 5])
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            gameRunning = False #prevent infinite loop / allow exit
    pygame.display.flip()
pygame.quit()
    