import pygame
import random

class Fruit:
    def __init__(self,frame_width,frame_height,sprite_sheet,frame_count,scale,fall_spd):
        pygame.init()
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
    def start(self):
        self.x = random.randint(0,self.screen_width - self.frame_width)
        self.y = 150
    def extract_frames(self):
        frames = []
        for i in range(self.frame_count - 1):
            frame_surface = pygame.Surface((self.frame_width,self.frame_height),pygame.SRCALPHA)
            frame_rect = pygame.Rect(i*self.frame_width,0,self.frame_width,self.frame_height)
            frame_surface.blit(self.sprite_sheet,(0,0),frame_rect)
            frames.append(frame_surface)
        return frames
        #frame = 32x32
    def update(self):
        if self.fall == True:
            self.y += self.fall_spd
        self.ticks += 1
        if self.ticks >= 5:
            self.ticks = 0
            self.frame += 1  % self.frame_count - 1
        if self.y > self.screen_height:
            self.start()

    def render(self,screen):
        if self.fall == True:
            cur_frame_surface = self.frames[self.frame]
            screen.blit(cur_frame_surface,(self.x,self.y))
        
        

