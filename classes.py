import pygame, random
from pygame.locals import *
from graphics import *

#self.image = pygame.Surface((width, height))
#self.image.fill(color)

class Player(pygame.sprite.Sprite):

	def __init__(self, x, y, isRight, img, jump, fire):
		super(Player, self).__init__()

		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = x, y
		self.xspeed, self.yspeed = 0, 0
		self.speed = 5
		self.life= 100
		self.lifeBar = pygame.Surface((self.life * 2 + 1, 12))
		self.lifeBar.fill((10, 250, 10))
		self.jump = jump
		self.fire = fire
		self.isRight = isRight

	def update(self, collidable = pygame.sprite.Group(), event = None):

		self.gravity()

		self.rect.x += self.xspeed

		collisionList = pygame.sprite.spritecollide(self, collidable, False)

		for collided in collisionList:
			if self.xspeed > 0:
				self.rect.right = collided.rect.left
			if self.xspeed < 0:
				self.rect.left = collided.rect.right

		self.rect.y += self.yspeed

		collisionList = pygame.sprite.spritecollide(self, collidable, False)

		for collided in collisionList:
			if self.yspeed > 0:
				self.rect.bottom = collided.rect.top
				self.yspeed = 0
			if self.yspeed < 0:
				self.rect.top = collided.rect.bottom
				self.yspeed = 0

		if not event == None:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d:
					self.xspeed = self.speed
					self.image = player1
					self.isRight = True
				if event.key == pygame.K_a:
					self.xspeed = -self.speed
					self.image = player1left
					self.isRight = False
				if event.key == pygame.K_w:
					if self.yspeed == 0:
						self.jump.play()
						self.yspeed = -(self.speed)*3
				if event.key == pygame.K_f:
					self.fire.play()
					if self.isRight == True:
						b = Bullet(self.rect.x + self.rect.width, self.rect.y + int(self.rect.height/2) - 4, 12, bullet1)
					else:
						b = Bullet(self.rect.x - 16, self.rect.y + int(self.rect.height/2) - 4, -12, bullet1left)
				

				#PERTE DE VIE
				if event.key == pygame.K_g:
					self.life -= random.randint(5, 10)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_d:
					if self.xspeed > 0:
						self.xspeed = 0
				if event.key == pygame.K_a:
					if self.xspeed < 0:
						self.xspeed = 0

	def gravity(self, gravity = 1):
		if self.yspeed == 0:
			self.yspeed = 1
		else:
			self.yspeed += gravity

	def drawLifeBar(self):
		if self.life <= 0:
			self.lifeBar = pygame.Surface((0, 12))
		else:
			self.lifeBar = pygame.Surface((self.life * 2 + 1, 12))
		self.lifeBar.fill((10, 250, 10))
		return self.lifeBar

class Block(pygame.sprite.Sprite):

	def __init__(self, x, y, img):
		super(Block, self).__init__()

		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = x, y

class Map(object):

	def __init__(self, level):
		super(Map, self).__init__()

		self.blockList = pygame.sprite.Group()
		self.level = level

	def generate(self):
		with open(self.level, 'r') as level:

			y = 0

			for lines in level:
				x = 0
				for car in lines:
					if car != '\n':
						if car == "#":
							block = Block(x, y, block1)
							self.blockList.add(block)
					x += 32
				y += 32

class Bullet(pygame.sprite.Sprite):
	bullets = pygame.sprite.Group()

	def __init__(self, x, y, speed, img):
		super(Bullet, self).__init__()

		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = x, y
		self.speed = speed
		Bullet.bullets.add(self)

	@staticmethod
	def move():
		for bullet in Bullet.bullets:
			bullet.rect.x += bullet.speed

	def destroy(self):
		Bullet.bullets.remove(self)
		del self