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
        return pygame.Surface.subsurface(self.img,(frame * 288,row * 128,288,128))
    
    
    
    
    



    
    
