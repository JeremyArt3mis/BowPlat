import pygame,sys
from sprites import sprites
from player import Player
from projectile import Projectile
from goblin import Goblin
import random
import math

class Menu:
    def __init__(self,game):
        pygame.init()
        self.game = game
        self.font2 = pygame.font.Font("Font.ttf",50)
        self.font = pygame.font.Font("Font.ttf",100)
        self.buttons = [{"Label":"Start","Rect":pygame.Rect((800,475),(1100,525)),"Action":"Start"}]
        self.x = 625
        self.y = 275
        self.timer = 0
        self.sin_y = 0
        # self.bit_backround = pygame.image.load("backround.png").convert()
        # self.backround = pygame.transform.scale(self.bit_backround,(self.width,self.height))
    def update(self):
        self.timer += 0.1
        self.sin_y = math.sin(self.timer)
        self.y += self.sin_y
        print(self.sin_y)
    def render(self):
        self.game.screen.blit(self.game.backround,(0,0))
        title = self.font.render("Arrow Feast",True,(27,43,48))
        self.game.screen.blit(title,(self.x,self.y))
        press_space = self.font2.render("Press Space To Start",True,(27,43,48))
        self.game.screen.blit(press_space,(self.x + 30,self.y + 100))
        pygame.display.flip()
        

        

        