import pygame,sys
from sprites import sprites
from player import Player


class Goblin:
    def __init__(self,x,y,img,game):
        pygame.init()
        self.x = 0
        self.y = 0
        self.img = img
        self.img_width = 1800
        self.img_height = 150
        self.game = game
        self.frame = 0
    def get_frame(self,frame):
        return pygame.Surface.subsurface(self.img,(frame * (self.img_height / 12),0,self.img_width,self.img_height))
    def update(self):
        self.x += 0
    def render(self):
        image = pygame.transform.scale(self.get_frame(self.frame,None),self.img_width,self.img_height)
        self.game.screen.blit(image,(self.x,self.y))
    
    
