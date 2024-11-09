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
        self.health_width = 100
        self.health_height = 8
        self.face_left = True
    def update(self,tx):
        self.frame += 0.05
        if self.x - 150 > tx:
            self.x -= self.speed
            self.face_left = True
        else:
            self.x += self.speed
            self.face_left = False

    def collision(self,colliderect):
        if self.hit_box.colliderect(colliderect):
            self.health -= 1

    

    def render(self):
        self.hit_box.topleft = (self.x + 200,self.y + 200)
        pygame.draw.rect(self.game.screen,(255,0,0),self.hit_box,2)
        image = self.sprite_sheet.get_frame_single_row(math.floor(self.frame) % 4)
        image = pygame.transform.flip(pygame.transform.scale(image,(self.img_width,self.img_height)),self.face_left,False)
        self.game.screen.blit(image,(self.x,self.y))
        self.health_rect = pygame.Rect(self.x + 175,self.y + 180,self.health_width * (self.health / 20),self.health_height)
        pygame.draw.rect(self.game.screen,(255,75,0),self.health_rect)

    
    