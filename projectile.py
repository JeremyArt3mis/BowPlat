import pygame,sys



class Projectile:
    def __init__(self,game,frame,img,x,y):
        pygame.init()
        self.frame = frame
        self.img = img
        self.x = x
        self.y = y
        self.game = game
        self.dir = dir
        self.speed = 5
        self.run = 0
        self.face_left = 0
    def get_frame(self,frame,action):
        row = 0
        return pygame.transform.flip(pygame.Surface.subsurface(self.img,(frame * 256,row * 128,256,128)),self.face_left,False)
    def render(self):
        image = pygame.transform.scale(self.get_frame(0,None),(256 * 2,128 * 2))
        self.game.screen.blit(image,(self.x,self.y))
    def update(self,direction):
        if self.run == 0:
            self.dir = direction
            if self.dir  == -1:
                self.x -= 275
            self.run += 1
        self.x += self.dir * self.speed
        if self.dir == -1:
            self.face_left = True
        if self.dir == 1:
            self.face_left = False
