import random #for RNG
import pygame
pygame.init()

white = (255, 255, 255)
black = (0 ,0, 0)
bg = pygame.image.load('cat hands.jpg')
jumping_cat = pygame.image.load('pixel cat.png')
#colors and images

width = 750
height = 500
#dimensions

score = 0
player_x = 50
player_y = 300
fps = 60
background = pygame.transform.scale(bg, (width, height))
timer = pygame.time.Clock()
player_image = pygame.transform.scale(jumping_cat, (100, 100))
#game variables

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jump Cat')
#game window

gameRunning = True
while gameRunning:
    timer.tick(fps)
    screen.blit(background, (0,0))
    floor = pygame.draw.rect(screen, black, [0, 400, width, 5])
    player = screen.blit(player_image, (player_x, player_y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            gameRunning = False #prevent infinite loop / allow exit
    pygame.display.flip()
    
pygame.quit() 
    