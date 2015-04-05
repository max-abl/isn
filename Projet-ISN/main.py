import pygame, sys
from pygame.locals import *
from graphics import *
from classes import *
from process import *
from random import randint

pygame.init()


#Création / définition de l'écran

screen = pygame.display.set_mode(size, RESIZABLE)
pygame.display.set_icon(icon)
pygame.display.set_caption("Projet ISN")

clock = pygame.time.Clock() # création d'un objet horloge permmettant notemment de réguler le nombre de tours/s de la boucle

#Création d'objet : joueur1, joueur2

player1 = Player(160, 128, True, pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_f, player1, player1left, player1fire, player1fireleft, jump, fire)
player2 = Player(width - 192, 128, False, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_KP0, player2, player2left, player2fire, player2fireleft, jump, fire)

player1.setEnemy(player2)
player2.setEnemy(player1)

#Création d'un objet map

levl1 = Map(lvl1)

#Création de liste pour chaque joueur qui va être utilisée pour la détéction de collision balles/joueur

list1 = [player1] 
list2 = [player2]

#On appelle la fonction de la map qui va générer le terrain

levl1.generate()

#Boucle infinie

spawner = ItemSpawner(20)

while True:

	title = "Projet ISN. fps : " + str(clock.get_fps())

	pygame.display.set_caption(title)

	#PROCESS (test de processus ex évènements)

	process(player1, player2)

	#LOGIC

	collision(list1, list2, levl1) #appel de la fonction collision
	

	spawner.update(secTime)
	

	player1.update(levl1.blockList) # appel de la fonction update de la classe player
	player2.update(levl1.blockList) #Idem
	Bullet.move()

	#DRAW

	screen.blit(fond, (0, 0)) # Affichage du fond

	screen.blit(player1.image, (player1.rect.x, player1.rect.y)) # Affichage du joueur
	screen.blit(player2.image, (player2.rect.x, player2.rect.y)) # Idem

	levl1.blockList.draw(screen) # Affichage de tous les blocs du niveau

	Bullet.bullets.draw(screen) # affichage de toutes les balles tirées
	
	Item.itemList.draw(screen)

	player1.drawLifeBar(screen, 0, 0, 19, 4, lifeBarSupport1)
	player2.drawLifeBar(screen, width - 256, 0, width - player2.life * 2 - 20, 4, lifeBarSupport2)

	screen.blit(scoreSupport, (width/2 - 64, 0))
	player1.drawScore(screen, width/2 - 48, 16)
	player2.drawScore(screen, width/2 + 16, 16)

	#SPAWN ALEATOIRES


	# LE TEMPS ! (c'est de l'argent)

	if looptime < 60:
		looptime += 1

	else:
		looptime = 1
		secTime += 1
		print(secTime)
		if secTime >= 60:
			secTime = 0

	clock.tick(ups) # régule les tours de boucles à 60 tours/S

	pygame.display.update() #raffrachissment de l'écran

