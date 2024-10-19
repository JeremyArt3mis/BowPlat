import pygame,sys
import math
from sprites import sprites
from player import Player


class Goblin:
    def __init__(self,x,y,sprite_sheet,game):
        pygame.init()
        self.x = x
        self.y = y
        self.sprite_sheet = sprite_sheet
        self.scale = 3
        self.img_width = 150 * self.scale
        self.img_height = 150 * self.scale
        self.game = game
        self.frame = 0
        self.hit_box = pygame.Rect(self.x,self.y,50,100)
        self.health = 20
        self.speed = 3/4
    def update(self,tx):
        self.frame += 0.2
        if self.x - 150 > tx:
            self.x -= self.speed
        else:
            self.x += self.speed
    def render(self):
        self.hit_box.topleft = (self.x + 200,self.y + 200)
        pygame.draw.rect(self.game.screen,(255,0,0),self.hit_box,2)
        image = self.sprite_sheet.get_frame_single_row(math.floor(self.frame) % 12)
        image = pygame.transform.scale(image,(self.img_width,self.img_height))
        self.game.screen.blit(image,(self.x,self.y))
    
    