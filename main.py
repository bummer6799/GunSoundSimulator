import pygame
import sys
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

playerImg = pygame.image.load('Player.png')
playerX = 400
playerY = 300
playerX_change = 0
playerY_change = 0

pygame.display.set_caption('GunSoundSimulator')
icon = pygame.image.load('GunSoundSimulatorIcon.png')
pygame.display.set_icon(icon)

def player(x,y):
    screen.blit(playerImg, (x, y))

running = True

while running:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left Pressed")
                playerX_change = -0.1
                print(playerX,playerY)
            if event.key == pygame.K_RIGHT:
                print("Right Pressed")
                playerX_change = 0.1
                print(playerX, playerY)
            if event.key == pygame.K_UP:
                print("Up Pressed")
                playerY_change = -0.1
                print(playerX, playerY)
            if event.key == pygame.K_DOWN:
                print("Down Pressed")
                playerY_change = 0.1
                print(playerX, playerY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key Released")
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                print("Key Released")
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    if playerX <= -1:
        playerX = 0
        #print("Boundaries Reached")
    elif playerX >= 769:
        playerX = 768
        #print("Boundaries Reached")
    elif playerY <= 0:
        playerY = 0
        #print("Boundaries Reached")
    elif playerY >= 568:
        playerY = 568
        #print("Boundaries Reached")

    player(playerX, playerY)
    pygame.display.update()


