import pygame,sys
from sprites import sprites

class Game:
    def __init__(self):
        pygame.init()
        self.width = 1700
        self.height = 1000
        self.screen = pygame.display.set_mode((self.width,self.height))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.render()
            pygame.display.update()
    
    def render(self):
        self.screen.fill((167,182,170))
        
    
game = Game()
game.run()