import pygame
import random
from player import Player

pygame.mixer.init()
flap_snd = pygame.mixer.Sound("flap.mp3")
class Fruit:
    def __init__(self,screen,frame_width,frame_height,sprite_sheet,frame_count,scale,fall_spd):
        pygame.init()
        self.screen = screen
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame = 0
        self.sprite_sheet = pygame.transform.scale(sprite_sheet,(int(sprite_sheet.get_width() * scale),int(sprite_sheet.get_height() * scale)))
        #pygame.image.load("Fruity.png")
        self.screen_width = 1700
        self.screen_height = 1000
        self.frame_count = frame_count
        self.scale = scale
        self.fall_spd = fall_spd
        self.fall = True
        self.ticks = 0
        self.frames = self.extract_frames()
        self.y = 0
        self.x = 0
        self.angle = 0
        self.rotate_spd = 2
        self.hit_box = pygame.Rect(0,0,self.frame_width * self.scale,self.frame_height * self.scale)



    def start(self):
        self.scale = 3
        self.fall_spd = 1
        self.rotate_spd = 2
        self.x = random.randint(0,self.screen_width - self.frame_width)
        self.y = 50

    def extract_frames(self):
        self.scale_width = self.sprite_sheet.get_width() // self.frame_count
        self.scale_height = self.sprite_sheet.get_height()
        frames = []
        for i in range(self.frame_count):
            frame_surface = pygame.Surface((self.scale_width,self.scale_height),pygame.SRCALPHA)
            frame_rect = pygame.Rect(i*self.scale_width,0,self.scale_width,self.scale_height)
            frame_surface.blit(self.sprite_sheet,(0,0),frame_rect)
            frames.append(frame_surface)
        return frames
        #frame = 32x32

    def update_hitbox(self):
        self.hit_box.x = self.x
        self.hit_box.y = self.y

    def update(self,hit_box):
        if self.fall == True:
            self.y += self.fall_spd
            self.angle += self.rotate_spd
            self.angle %= 360
            self.fall_spd += 0.2
            self.rotate_spd *= 0.99
            if self.hit_box.colliderect(hit_box):
                self.scale *= 0.5
                print("I'm TOUCHING YOU")
            self.update_hitbox()
            if not pygame.mixer.get_busy():
                flap_snd.play(-1)
        self.ticks += 1
        if self.ticks >= 5:
            self.ticks = 0
            self.frame = (self.frame + 0) % self.frame_count
        if self.y > self.screen_height:
            self.start()

    def render(self,screen):
        pygame.draw.rect(self.screen,(0,0,0),self.hit_box,2)
        if self.fall == True:
            cur_frame_surface = self.frames[self.frame]
            rotate_image = pygame.transform.rotate(cur_frame_surface,self.angle)
            screen.blit(rotate_image,(self.x,self.y))
        
        

