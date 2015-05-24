import pygame
from pygame.locals import *
from game import *
from graphics import background, icon, size

pygame.init() # initialisation du module

game = Game(size, "Cave Battle", icon, background) # On crée un objet game

game.start() #On le lance