
import pygame,sys
from sprites import sprites
from player import Player
from projectile import Projectile
from goblin import Goblin
import random

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.width = 1700
        self.height = 1000
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.bit_backround = pygame.image.load("backround.png").convert()
        self.backround = pygame.transform.scale(self.bit_backround,(self.width,self.height))
        self.goblins = 3
        self.sprite_sheet = sprites(pygame.image.load("Player_Assets/animations/spritesheets/Player_Sheet_288x128.png"),100)
        self.goblin_sheet = sprites(pygame.image.load("Enemy_Assets/Goblin/Idle.png"),12)
        self.test_rect = pygame.Rect(0,900,1700,200)
        self.player = Player(500,300,self.sprite_sheet,self)
        self.goblin = Goblin(random.randint(-500,500),600,self.goblin_sheet,self)
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
            self.player.update(self.goblin.hit_box)
            self.render()
            pygame.display.update()
    
    
    def render(self):
        self.screen.blit(self.backround,(0,0))
        health_percent = max(0,min(1,self.player.health / 100))
        r = int(255 * (1 - health_percent))
        g = int(255 * (health_percent))
        self.player_hp_bar = pygame.Rect(10,10,500 * health_percent,50)
        pygame.draw.rect(self.screen,(r,g,0),self.player_hp_bar)
        self.player.render()
        for i in range(self.goblins):
            self.goblin.update(self.player.x)
            self.goblin.render()
        for arrow in self.player.active_projectiles:
            arrow.update(self.player.dir)
            self.goblin.collision(arrow.hit_box)
            arrow.render()
        pygame.draw.rect(self.screen,(101, 173, 107),self.test_rect)
       
        
    
game = Game()
game.run()
