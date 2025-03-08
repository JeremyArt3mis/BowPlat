
import pygame,sys
from sprites import sprites
from player import Player
from projectile import Projectile
from goblin import Goblin
from menu import Menu
from fruit import Fruit
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
        self.bit_fruit_tree = pygame.image.load("fruit_tree.png").convert_alpha()
        self.fruit_tree = pygame.transform.scale(self.bit_fruit_tree,(self.width,self.height))
        self.goblins = 3
        self.sprite_sheet = sprites(pygame.image.load("Player_Assets/animations/spritesheets/Player_Sheet_288x128.png"),100)
        self.goblin_sheet = sprites(pygame.image.load("Enemy_Assets/Goblin/Idle.png"),12)
        self.test_rect = pygame.Rect(0,900,1700,200)
        self.player = Player(500,0,self.sprite_sheet,self)
        self.goblin = Goblin(random.randint(-500,500),600,self.goblin_sheet,self)
        self.menu = Menu(self)
        self.state = "menu"
        self.fruit = Fruit(self.screen,32,32,pygame.image.load("Fruity.png"),5,3,2)

        
        #Beats
        pygame.mixer.init()
        pygame.mixer.music.load("backround_music.wav")
        pygame.mixer.music.play(-1) 
    def run(self):
        running = True
        self.fruit.start()
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # pygame.quit()
                    # quit()
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # pygame.quit()
                        # quit()
                        running = False
                if self.state == "menu":
                    if event.type == pygame.KEYDOWN:
                        #handle menu and attack
                        if event.key == pygame.K_SPACE:
                            self.state = "game"
                elif self.state == "game":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.player.attack1()
            #handle render stuff
            if self.state == "menu":
                self.menu.update()
                self.menu.render()
            elif self.state == "game":
                self.player.handle_input()
                self.player.update(self.goblin.hit_box)
                self.fruit.update(self.player.player_rect)
                self.update_arrow()
                self.render()
            pygame.display.update()
            
    
    def render(self):
        self.screen.blit(self.backround,(0,0))
        self.fruit.render(self.screen)
        self.screen.blit(self.fruit_tree,(0,0))
        health_percent = max(0,min(1,self.player.health / 100))
        r = int(255 * (1 - health_percent))
        g = int(255 * (health_percent))
        self.player_hp_bar = pygame.Rect(10,10,500 * health_percent,50)
        pygame.draw.rect(self.screen,(r,g,0),self.player_hp_bar)
        self.player.render()
        for arrow in self.player.active_projectiles:
            arrow.update(self.player.dir)
            self.goblin.collision(arrow.hit_box)
            arrow.render()
        for i in range(self.goblins):
            self.goblin.update(self.player.x)
            self.goblin.render()
            
            
        pygame.draw.rect(self.screen,(101, 173, 107),self.test_rect)
        
    def update_arrow(self):
        for i in range(self.goblins):
            projectiles = []
        for arrow in self.player.active_projectiles:
            arrow.update(self.player.dir)
            if self.goblin.collision(arrow.hit_box):
                projectiles.append(arrow)
            else: 
                arrow.render()
        for arrow in projectiles:
            projectiles.remove(arrow)
            # if self.goblin.hit_box.colliderect(arrow.hit_box):
            #     arrow.active = False

        
    
game = Game()
game.run()
