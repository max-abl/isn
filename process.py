import pygame
from pygame.locals import *
from classes import *
from graphics import *
from random import randint


def process(player, player2, list1, list2, game): # fonction gérant les évènements de touche
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # gère les évènements du clavier
			game.exit()

		elif event.type == pygame.KEYDOWN: # si appui de touche

			#PLAYER1----------------------

			if event.key == pygame.K_ESCAPE: # si la touche est : echap : on quitte le jeu
				game.exit()
			if event.key == player.right: # si la touche appuyée correspond à la touche "right" du joueur (défini lors de sa création)
				player.xspeed = player.speedX # On donne une vitesse != 0 au joueur
				player.image = player.imgR # on affiche l'image correspondante à son orientation
				player.isRight = True # on indique son orientation
			if event.key == player.left: # idem
				player.xspeed = -player.speedX
				player.image = player.imgL
				player.isRight = False
			if event.key == player.up:#idem
				if player.yspeed == 0:				
					player.jump.play() # on joue un son
					player.yspeed = -player.speedY
			if event.key == player.gun: # si on veut tirer
				player.fire.play() # on joue un son
				if player.isRight == True: # en fonction de son orientation
					player.image = player.imgFR #image du joueur qui tire et ensuite on crée un objet balle
					b = Bullet(player.rect.x + player.rect.width, player.rect.y + int(player.rect.height/2) - 8, 18, bullet1)
				else: # autre direction
					player.image = player.imgFL
					b = Bullet(player.rect.x - 16, player.rect.y + int(player.rect.height/2) - 8, -18, bullet1left)


			#PLAYER2----------------------

			if event.key == player2.right: #idem
				player2.xspeed = player2.speedX
				player2.image = player2.imgR
				player2.isRight = True
			if event.key == player2.left:
				player2.xspeed = -player2.speedX
				player2.image = player2.imgL
				player2.isRight = False
			if event.key == player2.up:
				if player2.yspeed == 0:				
					player2.jump.play()
					player2.yspeed = -player2.speedY
			if event.key == player2.gun or event.key == pygame.K_o:
				player2.fire.play()
				if player2.isRight == True:
					player2.image = player2.imgFR
					b = Bullet(player2.rect.x + player2.rect.width, player2.rect.y + int(player2.rect.height/2) - 4, 18, bullet1)
				else:
					player2.image = player2.imgFL
					b = Bullet(player2.rect.x - 16, player2.rect.y + int(player2.rect.height/2) - 4, -18, bullet1left)
					
		elif event.type == pygame.KEYUP: # si on relève une touche

			#PLAYER1-------------------------

			if event.key == player.right: # On  remet la vitesse du joueur à 0
				if player.xspeed > 0:
					player.xspeed = 0
			if event.key == player.left:
				if player.xspeed < 0:
					player.xspeed = 0
			if event.key == player.gun:
				if player.isRight == True:
					player.image = player.imgR # on remet l'image de base du joueur en fonction de son orientation
				else:
					player.image = player.imgL

			#PLAYER2-------------------------

			if event.key == player2.right: #idem
				if player2.xspeed > 0:
					player2.xspeed = 0
			if event.key == player2.left:
				if player2.xspeed < 0:
					player2.xspeed = 0
			if event.key == player2.gun:
				if player2.isRight == True:
					player2.image = player2.imgR
				else:
					player2.image = player2.imgL

	collision(list1, list2, game.level) # appel de la focntion collision

def collision(player1, player2, levl): # fonction gérant les collisions entre balles/blocs et balles/joueur
	for b in Bullet.bullets: # pour chaque balle existante dans le jeu
		if pygame.sprite.spritecollide(b, levl.blockList, False): # on teste si la balle touche un bloc 
			b.destroy() # dans ce cas on détruit la balle

		elif pygame.sprite.spritecollide(b, player1, False): #sinon si c'est avec un joueur
			b.destroy() # on détruit
			player1[0].hit(randint(5, 10)) # le joueur concerné prend des dégâts

		elif pygame.sprite.spritecollide(b, player2, False):
			b.destroy()
			player2[0].hit(randint(5, 10))
	
	for item in Item.itemList: # collision avec les bonus
		if pygame.sprite.spritecollide(item, player1, False): # idem 
			item.setBonus(player1[0]) #met le bonus
			item.destroy() # détruit l'item

		elif pygame.sprite.spritecollide(item, player2, False):
			item.setBonus(player2[0])
			item.destroy()
			
