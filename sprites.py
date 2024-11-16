import pygame,sys
class sprites:
    def __init__(self,img,frames):
        pygame.init()
        self.frames = frames
        self.img = img
    def get_frame(self,action,frame):
        row = None
        if action == "idle":
            row = 0
        if action == "run":
            row = 1
        if action == "jump":
            row = 3
        if action == "fall":
            row = 5
        if action == "attack1":
            row = 11
        if action == "me_dead":
            row = 16
        return pygame.Surface.subsurface(self.img,(frame * 288,row * 128,288,128))
    
    def get_frame_single_row(self,frame):
        return pygame.Surface.subsurface(self.img,(frame * 150,0,150,150))
    
    def get_explosion_frame(self,frame):
        return pygame.Surface.subsurface(self.img,(frame * 48,0,48))
    #336x48
    
    
    



    
    