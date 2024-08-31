import pygame,sys
from sprites import sprites
import math

class Player:
    def __init__(self,x,y,sprite_sheet,game):
        pygame.init()
        self.x = x
        self.y = y
        self.sprite_sheet = sprite_sheet
        self.game = game
        self.xspeed = 0
        self.yspeed = 0
        self.action = "run"
        self.frame = 0
        self.max_frame = 10
        self.player_rect = pygame.Rect(0,0,0,0)
      
    
    def render(self):
        face_left = self.xspeed < 0
        if abs(self.xspeed) < 1.5:
            self.action = "idle"
        else:
            self.action = "run" 
        if self.action == "idle":
            self.max_frame = 12
        else:
            self.max_frame = 10
        player_frame = pygame.transform.flip(pygame.transform.scale(self.sprite_sheet.get_frame(self.action,math.floor(self.frame % self.max_frame)),(288 * 2.5,128 * 2.5)),face_left,False)
        self.game.screen.blit(player_frame,(self.x,self.y))
        self.player_rect = pygame.Rect(self.x + 345,self.y + 200,30,120)
        #pygame.draw.rect(self.game.screen,(10,50,200),self.player_rect)
        self.frame += 0.2
        
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.xspeed += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 0.75
        
        

    def update(self):
        keys = pygame.key.get_pressed()
        self.yspeed += 0.5
        if self.player_rect.colliderect(self.game.test_rect):
            while self.player_rect.colliderect(self.game.test_rect):
                self.player_rect.y -= 1
            self.y = self.player_rect.y - 199
            self.yspeed = 0
            self.yspeed += -15 * keys[pygame.K_UP]
        self.y += self.yspeed
        print(self.y,self.x)
        self.x += self.xspeed
        self.xspeed *= 0.9
        
        
        
            
        
