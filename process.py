import pygame
from pygame.locals import *
from classes import *
from graphics import *
from random import randint


def process(player, player2, list1, list2, game): # fonction gérant les évènements de touche
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game.stop()

		elif event.type == pygame.KEYDOWN:
			if event.key == player.right:
				player.xspeed = player.speedX
				player.image = player.imgR
				player.isRight = True
			if event.key == player.left:
				player.xspeed = -player.speedX
				player.image = player.imgL
				player.isRight = False
			if event.key == player.up:
				if player.yspeed == 0:				
					player.jump.play()
					player.yspeed = -player.speedY
			if event.key == player.gun:
				player.fire.play()
				if player.isRight == True:
					player.image = player.imgFR
					b = Bullet(player.rect.x + player.rect.width, player.rect.y + int(player.rect.height/2) - 4, 18, bullet1)
				else:
					player.image = player.imgFL
					b = Bullet(player.rect.x - 16, player.rect.y + int(player.rect.height/2) - 4, -18, bullet1left)


			#PLAYER2----------------------

			if event.key == player2.right:
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
					
		elif event.type == pygame.KEYUP:
			if event.key == player.right:
				if player.xspeed > 0:
					player.xspeed = 0
			if event.key == player.left:
				if player.xspeed < 0:
					player.xspeed = 0
			if event.key == player.gun:
				if player.isRight == True:
					player.image = player.imgR
				else:
					player.image = player.imgL

			#PLAYER2-------------------------

			if event.key == player2.right:
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

	collision(list1, list2, game.level)

def collision(player1, player2, levl): # fonction gérant les collisions entre balles/blocs et balles/joueur
	for b in Bullet.bullets:
		if pygame.sprite.spritecollide(b, levl.blockList, False):
			b.destroy()

		elif pygame.sprite.spritecollide(b, player1, False):
			b.destroy()
			player1[0].hit(randint(5, 10))

		elif pygame.sprite.spritecollide(b, player2, False):
			b.destroy()
			player2[0].hit(randint(5, 10))
	
	for item in Item.itemList:
		if pygame.sprite.spritecollide(item, player1, False):
			item.setBonus(player1[0])
			item.destroy()
		elif pygame.sprite.spritecollide(item, player2, False):
			item.setBonus(player2[0])
			item.destroy()
			
