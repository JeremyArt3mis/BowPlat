import pygame,sys,math
class sprites:
    def __init__(self,img,frames,x,y,xspeed,yspeed):
        pygame.init()
        self.frames = frames
        self.img = img
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
    def get_frame(self,action,frame):
        row = None
        if action == "idle":
            row = 1
            pygame.Surface.subsurface(self.img,(frame * 288,row * 128,288,128))
    /*
    def platformer_physics(_gravity,_jump_spd,_max_slope,_friction,_acceleration,_xsteps,_ysteps):
        keys = pygame.key.get_pressed()
        #vertical collision and movement
        self.y += _ysteps
        steps = -(steps / abs(steps))
        while sprites.colliderect(<level>):
            self.y += steps
            self.yspeed = 0
            if (keys[pygame.K_UP] == True) and (steps > 0):
                self.yspeed = _jump_spd
        #horizantal collision and movement
        xspeed += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * _acceleration
        if not sprites.colliderect(<level>):
            self.x += _xsteps
        if sprites.colliderect(<level>):
            self.x += _max_slope
            self.xspeed *= _friction * 0.95
        while sprites.colliderect(<level>):
            self.x -= (_xsteps / abs(_xsteps))
        xspeed *= _friction
        yspeed += _gravity
            

        
    */
