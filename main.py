# -*- coding: utf-8 -*- 
import pygame, sys
from pygame.locals import *
from graphics import *
from classes import *

pygame.init()

#gère les collisions entre balle et mur

def collision():
	for b in Bullet.bullets:
		if pygame.sprite.spritecollide(b, levl1.blockList, False): #si collision : destruction de l'objet balle
			b.destroy()

screen = pygame.display.set_mode(size, RESIZABLE ) # création d'un écran avec plusieurs paramètres
pygame.display.set_icon(icon) # mise en place de l'icon
pygame.display.set_caption("Projet ISN") # mise en place du titre

clock = pygame.time.Clock() # création d'une horloge qui régulera les tours de boucles

player = Player(width/2, height/2, True, player1, jump, fire) #création objet player
levl1 = Map(lvl1) # création objet map

levl1.generate() # génération de la map par la fonction generate()

while True: #boucle infinie

	#EVENT

	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event == K_ESCAPE:
			pygame.quit()
			sys.exit()

	#MOVE

	Bullet.move()

	#LOGIC

	player.update(levl1.blockList, event)
	collision()

	event = None

	#DRAW

	screen.blit(fond, (0, 0))
	screen.blit(player.image, (player.rect.x, player.rect.y))
	levl1.blockList.draw(screen)
	Bullet.bullets.draw(screen)
	screen.blit(lifeBarSupport1, (0, 0))
	screen.blit(player.drawLifeBar(), (19, 4))

	clock.tick(ups)

	pygame.display.update()
