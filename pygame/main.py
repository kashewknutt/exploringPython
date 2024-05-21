#a simple program to understand the concept of pygame
import pygame
import sys
from pygame.locals import *
import random
import time


#initializing the pygame
pygame.init()


#setting the screen size
screen = pygame.display.set_mode((600, 600)) # creates a window



#setting the title of the screen
pygame.display.set_caption("Snake Game")


#setting the color
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)


#initializing the variables
fps = pygame.time.Clock()
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]
foodPos = [random.randrange(1, 60)*10, random.randrange(1, 60)*10]
foodSpawn = True
direction = 'RIGHT'
changeTo = direction
score = 0


#game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game Over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (300, 10)
    screen.blit(GOsurf, GOrect)
    showScore(0)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()


#show score function
def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score: {0}'.format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (300, 100)
    screen.blit(Ssurf, Srect)


#main logic of the game
while True: #step 2 which is the infinite game loop
    for event in pygame.event.get(): # step 3 event listner
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                changeTo = 'RIGHT'
            if event.key == K_LEFT:
                changeTo = 'LEFT'
            if event.key == K_UP:
                changeTo = 'UP'
            if event.key == K_DOWN:
                changeTo = 'DOWN'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()
    if foodSpawn == False:
        foodPos = [random.randrange(1, 60)*10, random.randrange(1, 60)*10]
    foodSpawn = True
    screen.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(screen, green, Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, blue, Rect(foodPos[0], foodPos[1], 10, 10))
    if snakePos[0] > 600 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 600 or snakePos[1] < 0:
        gameOver()
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()
    showScore() 
    pygame.display.flip()
    fps.tick(20)
