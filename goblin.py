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
        self.max_frame = 4
        self.action = "Idle"
        #EXPLODE CHILDRENs
        self.alive = True
        self.death_frame = 0
        self.explode_frame = 0
        self.explode_sp_sheet = sprites(pygame.image.load("Enemy_Assets\Goblin\explode.png"),7)
        self.death_sp_sheet = sprites(pygame.image.load("Enemy_Assets\Goblin\death.png"),4)

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
        if self.health > 0:
            self.alive = True
            self.max_frame = 4
            self.img_width = 150 * self.scale
            self.img_height = 150 * self.scale
        else:
            self.alive = False
            self.max_frame = 7
            self.img_width = 48 * self.scale
            self.img_height = 48 * self.scale
    
    def death_handler(self):
        #to explode or not to explode
        current_death_frame = min(int(self.death_frame),4)
        if self.alive == True:
            self.action = "Idle"
            image = self.sprite_sheet.get_frame_single_row(self.death_frame)
            image = pygame.transform.flip(pygame.transform.scale(image,(self.img_width,self.img_height)),self.face_left,False)
            self.game.screen.blit(image,(self.x,self.y))
        elif self.alive == False:
            if min(int(self.death_frame),4):
                self.action = "death"
            elif min(int(self.explode_frame),7):
                self.action = "explode"
        #image loading
        if self.action == "death":
            death_image = self.death_sp_sheet.get_frame_single_row(self.current_death_frame)
            death_image = pygame.transform.flip(pygame.transform.scale(image,(self.img_width,self.img_height)),self.face_left,False)
            self.game.screen.blit(death_image,(self.x,self.y))
        elif self.action == "explode":
            explode_image = self.explode_sp_sheet.get_explosion_frame(self.explode_frame)
            explode_image = pygame.transform.flip(pygame.transform.scale(image,(self.img_width,self.img_height)),self.face_left,False)
            self.game.screen.blit(explode_image,(self.x,self.y))
        #put on ze screen
        


    def render(self):
        self.hit_box.topleft = (self.x + 200,self.y + 200)
        pygame.draw.rect(self.game.screen,(255,0,0),self.hit_box,2)
        self.death_frame = math.floor(self.frame) % self.max_frame
        self.death_handler()
        self.health_rect = pygame.Rect(self.x + 175,self.y + 180,self.health_width * (self.health / 20),self.health_height)
        pygame.draw.rect(self.game.screen,(255,75,0),self.health_rect)

                                                                                                                                             
    