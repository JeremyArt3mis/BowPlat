import pygame,sys
from sprites import sprites
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.width = 1700
        self.height = 1000
        self.screen = pygame.display.set_mode((self.width,self.height))
        
        #BUGGIES
        self.sprite_sheet = sprites(pygame.image.load("Player_Assets/animations/spritesheets/Player_Sheet_288x128.png"),100)
        
        self.test_rect = pygame.Rect(0,900,1700,200)
        self.player = Player(500,300,self.sprite_sheet,self)
    def run(self):
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            #self.platformer_physics()
            self.player.handle_input()
            self.player.update()
            self.render()
            pygame.display.update()
    
    def platformer_physics(self,_xsteps,_ysteps):
        keys = pygame.key.get_pressed()
        #vertical collision and movement
        self.y += _ysteps
        steps = -(steps / abs(steps))
        while sprites.colliderect(self.test_rect):
            self.y += steps
            self.yspeed = 0
            if (keys[pygame.K_UP] == True) and (steps > 0):
                self.yspeed = 10
        #horizantal collision and movement
        xspeed += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 0.5
        if not sprites.colliderect(self.test_rect):
            self.x += _xsteps
        if sprites.colliderect(self.test_rect):
            self.x += 1
            self.xspeed *= 0.8 * 0.95
        while sprites.colliderect(self.test_rect):
            self.x -= (_xsteps / abs(_xsteps))
        xspeed *= 0.8
        yspeed += 0.75

    
    def render(self):
        self.screen.fill((167,182,170))
        self.player.render()
        pygame.draw.rect(self.screen,(100,120,20),self.test_rect)
        
    
game = Game()
game.run()
game.run()
