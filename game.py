import graphics, sys
from classes import *
from process import process
from menu import *

class Game(object):
	def __init__(self, size, title, icon, background):
		super(Game, self).__init__()

		self.size = self.width, self.height = size
		self.title = title
		self.icon = icon
		self.background = background

		self.running = False

		self.winIndex = 0

		self.loopTime = 0
		self.seconds = 0

		self.initScreen()

		self.menu = Menu(self)

	def initScreen(self):

		self.screen = pygame.display.set_mode(self.size, FULLSCREEN)
		pygame.display.set_icon(self.icon)
		pygame.display.set_caption(self.title)

	def initPlayer(self, x1, y1, x2, y2):
		self.player1 = Player(x1, y1, True, pygame.K_w, pygame.K_a, pygame.K_d, 
			pygame.K_f, graphics.player1, graphics.player1left, graphics.player1fire,
			graphics.player1fireleft, graphics.jump, graphics.fire)

		self.player2 = Player(x2, y2, False, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, 
			pygame.K_KP0, graphics.player2, graphics.player2left, graphics.player2fire,
			graphics.player2fireleft, graphics.jump, graphics.fire)

		self.player1.setEnemy(self.player2)
		self.player2.setEnemy(self.player1)
 
	def initLevel(self):
		self.spawner = ItemSpawner(10)

		self.level = Map(graphics.lvl1)

		self.level.generate()

	def getScores(self):
		if self.player1.score == 9:
			self.winIndex = 2
			self.stop()
		elif self.player2.score == 9:
			self.winIndex = 3
			self.stop()


	def start(self):

		self.menu.start(self.winIndex)

		self.running = True

		self.loop(graphics.ups)

	def stop(self):
		self.running = False

	def exit(self):
		pygame.display.quit()
		pygame.quit()
		sys.exit(0)

	def loop(self, ups):

		clock = pygame.time.Clock()
		
		self.initPlayer(160, 128, self.width - 192, 128)
		self.initLevel()

		list1 = [self.player1]
		list2 = [self.player2]

		while self.running:
			self.update(list1, list2)
			self.render()

			pygame.display.update()

			self.timeCount()

			clock.tick(ups)

		self.destroyAll()

		return self.start()


	def update(self, list1, list2):
		process(self.player1, self.player2, list1, list2, self)

		self.player1.update(self.level.blockList)
		self.player2.update(self.level.blockList)

		Bullet.move()
		self.spawner.update(self.seconds, self.player1, self.player2)
		
		self.getScores()

	def render(self):
		self.screen.blit(self.background, (0, 0))

		self.level.blockList.draw(self.screen)

		Bullet.bullets.draw(self.screen)

		Item.itemList.draw(self.screen)

		self.screen.blit(graphics.scoreSupport, (self.width/2 - 64, 0))

		self.player1.render(self.screen, self.width/2 - 48, 16, 0, 0, 19, 4,
			graphics.lifeBarSupport1)
		self.player2.render(self.screen,self.width/2 + 16, 16, self.width - 256, 0,
			self.width - self.player2.life * 2 - 20, 4,graphics.lifeBarSupport2)

	def timeCount(self):
		if self.loopTime < 59:
			self.loopTime += 1
		else:
			self.loopTime = 0
			self.seconds += 1

	def destroyAll(self):
		del self.player1
		del self.player2

		del self.spawner

		Item.destroyAll()
		Bullet.destroyAll()

		self.level.destroyAll()



