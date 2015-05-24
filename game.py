import graphics, sys
from classes import *
from process import process
from menu import *

class Game():
	def __init__(self, size, title, icon, background):

		# attributs

		self.size = self.width, self.height = size # taille fenêtre
		self.title = title # titre
		self.icon = icon # icone
		self.background = background # fond

		self.running = False # booléen : condition de la boucle while du jeu

		self.winIndex = 0 # index du menu

		self.loopTime = 0 # temps
		self.seconds = 0

		self.initScreen() # On appelle la méthode qui crée la fenêtre

		self.menu = Menu(self) # on crée un objet menu

	def initScreen(self):

		self.screen = pygame.display.set_mode(self.size, FULLSCREEN)
		pygame.display.set_icon(self.icon)
		pygame.display.set_caption(self.title)

	def initPlayer(self, x1, y1, x2, y2): # création des 2 joueurs
		self.player1 = Player(x1, y1, True, pygame.K_w, pygame.K_a, pygame.K_d, 
			pygame.K_f, graphics.player1, graphics.player1left, graphics.player1fire,
			graphics.player1fireleft, graphics.jump, graphics.fire)

		self.player2 = Player(x2, y2, False, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, 
			pygame.K_KP0, graphics.player2, graphics.player2left, graphics.player2fire,
			graphics.player2fireleft, graphics.jump, graphics.fire)

		self.player1.setEnemy(self.player2) # gère l'interraction entre les 2 joueurs
		self.player2.setEnemy(self.player1)
 
	def initLevel(self):
		self.spawner = ItemSpawner(10) # on crée l'objet gérant l'apparition des bonus

		self.level = Map(graphics.lvl1) # on crée un objet map

		self.level.generate() # on génère le niveau

	def getScores(self): # récupère les scores et arrête le jeu si = 9
		if self.player1.score == 9:
			self.winIndex = 2 # change l'image de base du menu
			self.stop()
		elif self.player2.score == 9:
			self.winIndex = 3
			self.stop()


	def start(self): # lance le jeu

		self.menu.start(self.winIndex) # lance le menu avec l'index de base à mettre en paramètre

		self.running = True # permet à la boucle de tourner

		self.loop(graphics.ups) # On lance la boucle du jeu

	def stop(self): # arrête la boucle du jeu
		self.running = False

	def exit(self): # quitte le programme
		pygame.display.quit() # quitte la fenêtre
		pygame.quit() # quitte le module
		sys.exit() # quitte le programme

	def loop(self, ups): # boucle du jeu

		clock = pygame.time.Clock() # horloge qui peut réguler le nbr de tours de boucle / s
		
		self.initPlayer(160, 128, self.width - 192, 128) # appelle la méthode pour créer les joueurs
		self.initLevel() # idem pour le niveau

		list1 = [self.player1] # liste utilisée pour gérer les collisions entre balles et joueur
		list2 = [self.player2]

		while self.running: # tant que self.running == True
			self.update(list1, list2) # On appelle la méthode update du jeu
			self.render() # idem avec la méthode render()

			pygame.display.update() # On raffraichit l'écran : permet l'affichage et le rafraichissement

			self.timeCount() # appel de la méthode qui gère le temps du jeu

			clock.tick(ups) # On régule le nombre de tours de boucles par seconde

		self.destroyAll() # en sortant de la boucle : fin du jeu : on détruit tous les objets

		return self.start() # en sortant de la boucle on appelle la méthode start


	def update(self, list1, list2): # met à jour tous les obets et variables du jeu
		process(self.player1, self.player2, list1, list2, self) # appel de la fonction process

		self.player1.update(self.level.blockList) #idem pour la méthode update du joueur 1
		self.player2.update(self.level.blockList)

		Bullet.move() # idem
		self.spawner.update(self.seconds, self.player1, self.player2) # idem
		
		self.getScores() # appel de la méthode gérant le score

	def render(self): # affiche toutes les images du jeu
		self.screen.blit(self.background, (0, 0))

		self.level.blockList.draw(self.screen)

		Bullet.bullets.draw(self.screen) # on appelle la méthode affichant toutes les balles

		Item.itemList.draw(self.screen) # idem

		self.screen.blit(graphics.scoreSupport, (self.width/2 - 64, 0))

		self.player1.render(self.screen, self.width/2 - 48, 16, 0, 0, 19, 4,
			graphics.lifeBarSupport1)
		self.player2.render(self.screen,self.width/2 + 16, 16, self.width - 256, 0,
			self.width - self.player2.life * 2 - 20, 4,graphics.lifeBarSupport2)

	def timeCount(self): # gère le temps du jeu
		if self.loopTime < graphics.ups - 1: # tant que pas 1 sec incrémentation
			self.loopTime += 1
		else: # dès que 1 sec mise à 0 : secondes incrémentées
			self.loopTime = 0
			self.seconds += 1

	def destroyAll(self): # détruit tous les objets
		del self.player1 # del : enlève de la mémoire l'objet
		del self.player2

		del self.spawner

		Item.destroyAll()
		Bullet.destroyAll()

		self.level.destroyAll()
