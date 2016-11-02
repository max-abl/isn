import pygame, graphics
from pygame.locals import *

class Menu(object):

	def __init__(self, game):
		self.game = game # récupère l'objet game : utilisé pour quitter le programme

		self.choice = 0 # gère le choix du joueur dans le menu
		self.index = 0 # gère l'image de fond du menu
		self.baseIndex = 0 # index de base qui gère l'image de base du menu

		self.out = 1 # gère la sortie du menu

		self.cursorCoords = [264, 416, 560] # coordonnées possibles du curseur

	def start(self, index):
		self.index = index # gère l'index en fonction du paramètre
		self.baseIndex = index # utile pour l'écran de fin
		self.running = True # similaire à game
		self.loop()

	def stop(self):# arrête la boucle
		self.running = False

	def exit(self): # sort du menu en fonction de self.out
		if self.out == 1: return # si out == 1 : retourne rien donc continue le jeu
		elif self.out == 2: # sinon quitte le programme
			self.game.exit()

	def loop(self):
		 while self.running:
			self.update()
			self.render()

		 self.exit() # appelé auto dès que la boucle s'arrête

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # si on appuie sur la croix
				self.out = 2 # indique qu'on veut quitter le programme
				self.stop()  # arrêt de la boucle


			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP and self.index != 1:
					graphics.select.play()
					self.choice -= 1
					if self.choice < 0: self.choice = 2

				if event.key == pygame.K_DOWN and self.index != 1:
					graphics.select.play()
					self.choice += 1
					if self.choice > 2: self.choice = 0

				if event.key == pygame.K_ESCAPE and self.index == 1: # si on se situe dans la page help
					self.index = self.baseIndex # on retourne à l'index de base

				if event.key == pygame.K_RETURN and self.index == self.baseIndex: # si on est dans l'index de base
					if self.choice == 0: # si "start"
						self.out = 1 #indique qu'on veut lancer le jeu
						self.stop() # quitte la boucle

					elif self.choice == 1: #  si "help"
						self.index = 1 # on va dans l'index 1 : page d'aide

					elif self.choice == 2: # si "quit"
						self.out = 2 # ... on quitte
						self.stop()

	def render(self):
		self.game.screen.blit(graphics.menuBackground[self.index], (0, 0)) # (1)

		#(1) On affiche l'image de fond en fonction de l'index

		if self.index == self.baseIndex: # si on se situe dans l'index de base on affiche le curseur
			self.game.screen.blit(graphics.cursor, (448, self.cursorCoords[self.choice]))

		pygame.display.update() # on raffraichit l'écran
