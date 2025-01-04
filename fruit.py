import pygame
import random

class Menu:
    def __init__(self,game,x,y):
        pygame.init()
        self.game = game
        self.x = x
        self.y = y
        self.frame = 0
        self.sprite_sheet = pygame.image.load("Fruity.png")