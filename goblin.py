

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
        self.speed = 0.75
        self.health_width = 100
        self.health_height = 8
        self.face_left = True
        self.max_frame = 4
        self.action = "Idle"
        #EXPLODE CHILDRENs
        self.alive = True
        self.death_frame = 0
        self.explode_frame = 0
        self.death_anim_done = False
        self.explode_anim_done = False
        self.explode_sp_sheet = sprites(pygame.image.load("Enemy_Assets\Goblin\explode.png"),7)
        self.death_sp_sheet = sprites(pygame.image.load("Enemy_Assets\Goblin\Death.png"),4) 


    def update(self,tx):
        if self.health <= 0: # Add this part    
            self.alive = False
            self.speed = 0  # Stop movement


        # Update death animation ADD TO THIS
            if not self.death_anim_done:
                self.death_frame += 0.1
                if self.death_frame >= 3.9:  # Slightly less than 4 to ensure smooth transition to explosion
                    self.death_anim_done = True
            # Update explosion animation after death is done
            elif not self.explode_anim_done:
                self.explode_frame += 0.2
                if self.explode_frame >= 11.9:  # Slightly less than 12
                    self.explode_anim_done = True


        if self.alive:
            self.frame += 0.05
            if self.x - 150 > tx: # tx is the x position of the player
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
        #     self.max_frame = 4
        #     self.img_width = 150 * self.scale
        #     self.img_height = 150 * self.scale
        # else:
        #     self.alive = False
        #     self.max_frame = 7
        #     self.img_width = 48 * self.scale
        #     self.img_height = 48 * self.scale
   
    def death_handler(self):
        #to explode or not to explode
        if self.alive == False:
            if not self.death_anim_done:
                current_death_frame = min(int(self.death_frame),3)
                death_image = self.death_sp_sheet.get_frame_single_row(current_death_frame)
                death_image = pygame.transform.flip(pygame.transform.scale(death_image,(self.img_width,self.img_height)),self.face_left,False)
                self.game.screen.blit(death_image,(self.x,self.y))
            elif not self.explode_anim_done:
                current_explode_frame = min(int(self.explode_frame),6)
                explode_image = self.explode_sp_sheet.get_explosion_frame(current_explode_frame)
                explode_image = pygame.transform.flip(pygame.transform.scale(explode_image,(self.img_width,self.img_height)),self.face_left,False)
                self.game.screen.blit(explode_image,(self.x,self.y))
            return
        else:
            image = self.sprite_sheet.get_frame_single_row(math.floor((self.frame) % 4))
            image = pygame.transform.flip(pygame.transform.scale(image,(self.img_width,self.img_height)),self.face_left,False)
            self.game.screen.blit(image,(self.x,self.y))
       
    def render(self):
        if self.alive == True:
            self.hit_box.topleft = (self.x + 200,self.y + 200)
        else:
            self.hit_box.topleft = (self.x + 500,self.y + 500)
        pygame.draw.rect(self.game.screen,(255,0,0),self.hit_box,2)
        self.death_handler()
        self.health_rect = pygame.Rect(self.x + 175,self.y + 180,self.health_width * (self.health / 20),self.health_height)
        pygame.draw.rect(self.game.screen,(255,75,0),self.health_rect)


                                                                                                                                    