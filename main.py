import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

playerImg = pygame.image.load('Player.png')
playerX = 400
playerY = 300

pygame.display.set_caption('GunSoundSimulator')
icon = pygame.image.load('GunSoundSimulatorIcon.png')
pygame.display.set_icon(icon)

def player():
    screen.blit(playerImg, (playerX, playerY))

running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player()
    pygame.display.update()
