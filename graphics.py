import pygame, sys
from pygame.locals import *

# constantes

size = width, height = 1280, 720
scale = (32, 32)
ups = 60

#time

loopTime = 0
secTime = 0

menuBackground = []


menuBackground.append(pygame.transform.scale(pygame.image.load("res/img/menu.png"), size))
menuBackground.append(pygame.transform.scale(pygame.image.load("res/img/help.png"), size))
menuBackground.append(pygame.transform.scale(pygame.image.load("res/img/win1.png"), size))
menuBackground.append(pygame.transform.scale(pygame.image.load("res/img/win2.png"), size))

icon = pygame.image.load("res/img/icon.png") # chargement de l'icone de la fenêtre
background = pygame.transform.scale(pygame.image.load("res/img/fond.png"), size) # idem pour le fond
tileset = pygame.image.load("res/img/tileset.png") # idem pour l'image générale contenant toutes les textures

cursor = pygame.transform.scale(pygame.image.load("res/img/cursor.png"), (64, 64))

score = []
area = (
	(624, 320),
	(624, 96),
	(624, 480),
	(624, 608)
	)
#Levels

lvl1 = "res/levels/lvl1.txt" # idem pour le fichier .txt représentant le niveau

#TEXTURES

#personnage

player1 = pygame.transform.scale(tileset.subsurface(0, 8, 8, 8), scale) #chargement de l'mage du joueur en découpant une partie de l'image principale 
#tout en la grossisant x4
player1left = pygame.transform.flip(player1, True, False) #On renverse horizontalement l'image précédente pour quand le joueur est orienté vers la gauche

player1fire = pygame.transform.scale(tileset.subsurface(8, 8, 8, 8), scale) #idem pour l'image où le joueur tire
player1fireleft = pygame.transform.flip(player1fire, True, False) # idem

player2 = pygame.transform.scale(tileset.subsurface(0, 16, 8, 8), scale) # idem
player2left = pygame.transform.flip(player2, True, False) # idem

player2fire = pygame.transform.scale(tileset.subsurface(8, 16, 8, 8), scale) # idem
player2fireleft = pygame.transform.flip(player2fire, True, False) # idem

#block

block = pygame.transform.scale(tileset.subsurface(8, 0, 8, 8), scale)  # idem

#number

for x in range(0, 73, 8):
	score.append(pygame.transform.scale(tileset.subsurface(120, x, 8, 8), scale))

#score.append(pygame.transform.scale(tileset.subsurface(120, 0, 8, 8), scale))
#score.append(pygame.transform.scale(tileset.subsurface(120, 8, 8, 8), scale))
#score.append(pygame.transform.scale(tileset.subsurface(120, 16, 8, 8), scale))
#score.append(pygame.transform.scale(tileset.subsurface(120, 24, 8, 8), scale))
#score.append(pygame.transform.scale(tileset.subsurface(120, 32, 8, 8), scale))
#score.append(pygame.transform.scale(tileset.subsurface(120, 40, 8, 8), scale))
#score.append(pygame.transform.scale(tileset.subsurface(120, 48, 8, 8), scale))
#score.append(pygame.transform.scale(tileset.subsurface(120, 56, 8, 8), scale))
#score.append(pygame.transform.scale(tileset.subsurface(120, 64, 8, 8), scale))
#score.append(pygame.transform.scale(tileset.subsurface(120, 72, 8, 8), scale))

#bullet

bullet1 = pygame.transform.scale(tileset.subsurface(0, 120, 8, 2), (16, 4)) # idem
bullet1left = pygame.transform.flip(bullet1, True, False) # idem

#lifeBarSupport

lifeBarSupport1 = pygame.transform.scale(tileset.subsurface(0, 104, 56, 8), (256, 32)) # idem
lifeBarSupport2 = pygame.transform.flip(lifeBarSupport1, True, False) # idem

#scoreSupport

scoreSupport = pygame.transform.scale(tileset.subsurface(0, 80, 32, 16), (128, 64))

#LifeBonus

lifeBonus = pygame.transform.scale(tileset.subsurface(32, 0, 8, 8), scale)
speedBonus =  pygame.transform.scale(tileset.subsurface(48, 0, 8, 8), scale)

#SOUNDS

pygame.mixer.init() # initialisation du module mixer permettant le chargement de sons

jump = pygame.mixer.Sound("res/sound/jump.wav") # chargement du son utilisé pour le saut du joeur
jump.set_volume(0.3) # modifie le volume du son chargé
fire = pygame.mixer.Sound("res/sound/fire.wav") # idem
fire.set_volume(0.5) # idem

pygame.mixer.quit() # On quitte le module
