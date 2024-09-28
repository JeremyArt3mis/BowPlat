import pygame,sys
from sprites import sprites
from projectile import Projectile
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
        self.attack_frame = 0
        self.active_projectiles = []
        
      
    
    def render(self):
        #animation
        face_left = self.xspeed < 0
        if self.action != "attack1": 
            if self.yspeed > 0:
                self.action = "fall"
            elif self.yspeed < 0:
                self.action = "jump"
            elif abs(self.xspeed) < 1.5:
                self.action = "idle"
            else:
                self.action = "run" 
        if self.action == "attack1":
            self.max_frame = 13  
        elif self.action == "idle":
            self.max_frame = 12
        elif self.action == "run":
            self.max_frame = 10
        else:
            self.max_frame = 2
        #render
        if self.action == "attack1":
            player_frame = pygame.transform.flip(pygame.transform.scale(self.sprite_sheet.get_frame(self.action,math.floor(self.attack_frame % self.max_frame)),(288 * 2.5,128 * 2.5)),face_left,False)
        else:
            player_frame = pygame.transform.flip(pygame.transform.scale(self.sprite_sheet.get_frame(self.action,math.floor(self.frame % self.max_frame)),(288 * 2.5,128 * 2.5)),face_left,False)
        self.game.screen.blit(player_frame,(self.x,self.y))
        self.player_rect = pygame.Rect(self.x + 345,self.y + 200,30,120)
        #pygame.draw.rect(self.game.screen,(10,50,200),self.player_rect)
        self.frame += 0.2
        
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        print(self.attack_frame)
        self.xspeed += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 0.75
        if round(self.attack_frame) == 8:
            self.attack_frame += 1
            self.spawn_arrow()
        

    def attack1(self):
        print(self.attack_frame)
        if self.action == "idle":
            self.action = "attack1"
        
            
    
    def spawn_arrow(self):
        new_arrow = Projectile(self.game,0,pygame.image.load("BowPlat-main/Player_Assets/animations/spritesheets/Projectile_256x128_SpriteSheet.png"),self.x + 245,self.y + 100)
        self.active_projectiles.append(new_arrow)

        

    def fix_collision(self,keys):
        if self.player_rect.colliderect(self.game.test_rect):
            while self.player_rect.colliderect(self.game.test_rect):
                self.player_rect.y -= self.yspeed / abs(self.yspeed)
            self.y = self.player_rect.y - 199
            self.yspeed = 0
            self.yspeed += -15 * keys[pygame.K_UP]
        else:
            self.yspeed += 0.0000000000001
    
    def move(self):
        self.y += self.yspeed
        self.x += self.xspeed
        self.xspeed *= 0.9
    
    def handle_attack(self):
        if self.action == "attack1":
            self.attack_frame += 0.2
            if self.attack_frame >= self.max_frame - 1:
                self.attack_frame = 0
                self.action = "idle"

    def update(self):
        keys = pygame.key.get_pressed()
        self.yspeed += 0.5
        self.fix_collision(keys)
        self.move()
        self.handle_attack()
        
        
