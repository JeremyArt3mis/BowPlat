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
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.attack1()
            #self.platformer_physics()
            self.player.handle_input()
            self.player.update()
            self.render()
            pygame.display.update()
    
    
    def render(self):
        self.screen.fill((167,182,170))
        self.player.render()
        for arrow in self.player.active_projectiles:
            arrow.render()
        pygame.draw.rect(self.screen,(100,120,20),self.test_rect)
        
    
game = Game()
game.run()