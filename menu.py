import pygame, graphics
from pygame.locals import *

class Menu(object):
	
	def __init__(self, game):
		self.game = game

		self.choice = 0
		self.index = 0
		self.baseIndex = 0

		self.out = 1

		self.cursorCoords = [264, 416, 560]

	def start(self, index):
		self.index = index
		self.baseIndex = index
		self.running = True
		self.loop()

	def stop(self):
		self.running = False

	def exit(self):
		if self.out == 1: return
		elif self.out == 2:
			self.game.exit()

	def loop(self):
		 while self.running:
		 	self.update()
		 	self.render()

		 self.exit()

	def update(self): 
		for event in pygame.event.get():
		 	if event.type == pygame.QUIT:
		 		self.stop()
		 		self.out = 2
		 		

		 	elif event.type == pygame.KEYDOWN:
		 		if event.key == pygame.K_UP:
		 			self.choice -= 1
		 			if self.choice < 0: self.choice = 2

		 		if event.key == pygame.K_DOWN:
		 			self.choice += 1
		 			if self.choice > 2: self.choice = 0

		 		if event.key == pygame.K_ESCAPE and self.index == 1:
		 			self.index = self.baseIndex

		 		if event.key == pygame.K_RETURN and self.index == self.baseIndex:
		 			if self.choice == 0:
		 				self.out = 1
		 				self.stop()

		 			elif self.choice == 1:
		 				self.index = 1

		 			elif self.choice == 2:
		 				self.out = 2
		 				self.stop()

	def render(self):
		self.game.screen.blit(graphics.menuBackground[self.index], (0, 0))

		if self.index == self.baseIndex:
			self.game.screen.blit(graphics.cursor, (448, self.cursorCoords[self.choice]))

		pygame.display.update()


