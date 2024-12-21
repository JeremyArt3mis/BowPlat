import pygame,sys
from sprites import sprites
from player import Player
from projectile import Projectile
from goblin import Goblin
import random

class Menu:
    def __init__(self,game):
        pygame.init()
        self.game = game
        self.font = pygame.font.Font("Font.ttf",50)
        self.buttons = [{"Label":"Start","Rect":pygame.Rect((800,475),(1100,525)),"Action":"Start"}]
        #self.backround = pygame.load.image("backround.png")
    def render(self):
        title = self.font.render("Arrow Feast",True,(255,255,255))
        self.game.screen.blit(title,(800,500))
        

        

        