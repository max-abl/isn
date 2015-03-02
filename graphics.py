import pygame, sys
from pygame.locals import *

size = width, height = 1280, 720
scale = (32, 32)
ups = 60

icon = pygame.image.load("res/img/icon.png")
fond = pygame.transform.scale(pygame.image.load("res/img/fond.png"), size)
tileset = pygame.image.load("res/img/tileset.png")

#Levels

lvl1 = "res/levels/lvl1.txt"

#TEXTURES

#personnage

player1 = pygame.transform.scale(tileset.subsurface(0, 0, 8, 8), scale)
player1left = pygame.transform.flip(player1, True, False)

#block

block1 = pygame.transform.scale(tileset.subsurface(8, 0, 8, 8), scale)

#bullet

bullet1 = pygame.transform.scale(tileset.subsurface(0, 120, 8, 2), (16, 4))
bullet1left = pygame.transform.flip(bullet1, True, False)

#lifeBarSupport

lifeBarSupport1 = pygame.transform.scale(tileset.subsurface(0, 104, 56, 8), (256, 32))

#SOUNDS

pygame.mixer.init()

jump = pygame.mixer.Sound("res/sound/jump.wav")
jump.set_volume(0.3)
fire = pygame.mixer.Sound("res/sound/fire.wav")
fire.set_volume(0.5)

pygame.mixer.quit()