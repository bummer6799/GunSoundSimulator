import random

import pygame
import sys
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

#player
playerImg = pygame.image.load('Player.png')
playerX = 400
playerY = 300
playerX_change = 0
playerY_change = 0

pygame.display.set_caption('GunSoundSimulator')
icon = pygame.image.load('GunSoundSimulatorIcon.png')
pygame.display.set_icon(icon)

#walls
wallImg = pygame.image.load('Wall.png')
wallX = 450
wallY = 350

def wall(x,y):
    screen.blit(wallImg, (x, y))
def player(x,y):
    screen.blit(playerImg, (x, y))

def crash():
    global wallY
    if playerY < (wallY + 32):
        if ((playerY > wallX and playerX < (wallX + 32)) or ((playerX + 32) > wallX) and (playerX + 32) < (wallX) + 32):
            print("Collision Detected")

running = True

while running:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #stops automatically quitting
            running = False

        if event.type == pygame.KEYDOWN:    #movement
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

    if playerX <= -1:   #border collisions
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
    wall(wallX, wallY)
    crash()
    pygame.display.update()


