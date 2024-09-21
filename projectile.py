import pygame,sys

class Projectile:
    def __init__(self,game,frame,img,x,y):
        pygame.init()
        self.frame = frame
        self.img = img
        self.x = x
        self.y = y
        self.game = game
    def get_frame(self,frame,action):
        row = 0
        return pygame.Surface.subsurface(self.img,(frame * 256,row * 128,256,128))
    def render(self):
        image = pygame.transform.scale(self.get_frame(0,None),(256 * 2,128 * 2))
        self.game.screen.blit(image,(self.x,self.y))