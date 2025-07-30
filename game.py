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
y_change = 0
x_change = 0
gravity = 1
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 18
            if event.key == pygame.K_RIGHT:
                x_change = 4
            if event.key == pygame.K_LEFT:
                x_change = -4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_LEFT:
                x_change = 0
#movement

    if 0 <= player_x <= 749:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > 650:
        player_x = 650
#boundaries
                
    if y_change > 0 or player_y < 300:
        player_y -= y_change
        y_change -= gravity
    if player_y > 300:
        player_y = 300 #preventing glitching through floor
    if player_y == 300 and y_change < 0:
        y_change = 0
#jumping
            
    pygame.display.flip()
    
pygame.quit() 
    