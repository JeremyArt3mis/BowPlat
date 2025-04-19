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
        self.speed = 10
        self.run = 0
        self.face_left = 0
        self.hit_box = pygame.Rect(self.x,self.y,75,10)
        self.active = True
        self.hit_enemy = False

    def get_frame(self,frame,action):
        row = 0
        return pygame.transform.flip(pygame.Surface.subsurface(self.img,(frame * 256,row * 128,256,128)),self.face_left,False)
    
    def render(self):
        if not self.active:
            return 
        image = pygame.transform.scale(self.get_frame(0,None),(256 * 2,128 * 2))
        self.game.screen.blit(image,(self.x,self.y))
        self.hit_box.topleft = (self.x + 220,self.y + 120)
        #pygame.draw.rect(self.game.screen,(255,0,0),self.hit_box,2) #generates hitbox
    
    def update(self,direction):
        if not self.active:
            return
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
        if self.x <= 0 or self.x >= 1700:
            self.active = False
        