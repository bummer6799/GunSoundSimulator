import random

import pygame
import pygame.freetype

import sys
import time
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

#player
playerImg = pygame.image.load('player.png')
playerX = 400
playerY = 300
playerX_change = 0
playerY_change = 0

#icon
pygame.display.set_caption('GunSoundSimulator')
icon = pygame.image.load('GunSoundSimulatorIcon.png')
pygame.display.set_icon(icon)

#walls
wallImg = pygame.image.load('wall.png')
wallX = 450
wallY = 350

#sensors
off = pygame.image.load('off.png')
on = pygame.image.load('on.png')

def wall(x,y):
    screen.blit(wallImg, (x, y))
def player(x,y):
    screen.blit(playerImg, (x, y))

def isCollision(wallX, wallY, playerX, playerY):
    global distanceX
    global distanceY
    distanceX = wallX - playerX
    distanceY = wallY - playerY
    distance = math.sqrt((math.pow(wallX - playerX, 2)) + (math.pow(wallY - playerY, 2)))
    # if distanceX < 48 or distanceX < -48:
    #     return True
    # elif distanceY < 24 or distanceY < -24:
    #     return True
    # else:
    #     return False
    if distance < 32:
        return True
    else:
        return False

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

    collision = isCollision(wallX, wallY, playerX, playerY)     #collisons
    screen.blit(off, (8, 576))
    if collision:
        print("Collision Detected")
        screen.blit(on, (8, 576))
    #insert collision code

    font = pygame.freetype.Font("pixelfont.ttf", 20)    #font
    pX = str(round(playerX, 2))     #text
    pY = str(round(playerY, 2))
    text_surface1, rect1 = font.render(pX, (255, 255, 255))
    text_surface2, rect2 = font.render(pY, (255, 255, 255))
    screen.blit(text_surface1, (5, 5))
    screen.blit(text_surface2, (5, 30))
    dX = str(round(distanceX, 2))
    dY = str(round(distanceY, 2))
    distanceX_text, rect3 = font.render(dX, (127.5, 255, 255))
    distanceY_text, rect4 = font.render(dY, (127.5, 255,255))
    screen.blit(distanceX_text, (5, 55))
    screen.blit(distanceY_text, (5, 80))

    player(playerX, playerY)
    wall(wallX, wallY)

    pygame.display.update()


