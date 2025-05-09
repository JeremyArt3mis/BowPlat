
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
        self.goblins = 1
        self.sprite_sheet = sprites(pygame.image.load("Player_Assets/animations/spritesheets/Player_Sheet_288x128.png"),100)
        self.goblin_sheet = sprites(pygame.image.load("Enemy_Assets/Goblin/Idle.png"),12)
        self.test_rect = pygame.Rect(0,900,1700,200)
        self.player = Player(500,0,self.sprite_sheet,self)
        self.menu = Menu(self)
        self.state = "menu"
        self.fruit = Fruit(self.screen,32,32,pygame.image.load("Fruity.png"),5,3,2)
        self.time = 0
        self.score = 0
        self.score_font = pygame.font.Font("Font.ttf",100)
        self.floor = pygame.image.load("FLOOR.png").convert_alpha()
        self.real_floor = pygame.transform.scale(self.floor,(self.width,self.height))
        self.blackout = pygame.transform.scale(pygame.image.load("blackout.png"),(self.width,self.height))
        
        #Beats
        pygame.mixer.init()
        pygame.mixer.music.load("backround_music.wav")
        pygame.mixer.music.play(-1) 
        self.multiple_goblins = []
        self.num_goblins = 3
        for i in range(self.num_goblins):
            goblin_x = random.randint(0,self.width)
            goblin_y = 600
            goblin = Goblin(goblin_x,goblin_y,self.goblin_sheet,self)
            self.multiple_goblins.append(goblin)
            self.black = False
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
                elif self.state == "game_over":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.state = "menu"
                            self.score = 0
                            self.player.health = 100
                            self.player.x = 500
                            self.player.y = 0
                            self.multiple_goblins.clear()
                            self.goblins = 3
                            for i in range(self.num_goblins):
                                goblin_x = random.randint(0,self.width)
                                goblin_y = 600
                                goblin = Goblin(goblin_x,goblin_y,self.goblin_sheet,self)
                                self.multiple_goblins.append(goblin)
                            self.player.active_projectiles = []
                          
            #handle render stuff
            if self.state == "menu":
                self.menu.update()
                self.menu.render()
            elif self.state == "game":
                self.player.handle_input()
                # for goblin in self.multiple_goblins:
                self.player.update(self.multiple_goblins)
                self.fruit.update(self.player)
                self.render()
                self.update_arrow()
                score = self.score_font.render(f"Score: {self.score}",True,(27,43,48))
                if self.player.health <= 0:
                    self.state = "game_over"
                    self.black = True
                else:
                    self.screen.blit(score,(700,300))
            elif self.state == "game_over":
                 if self.black == False:
                     self.screen.blit(self.blackout,(0,0))
                     self.black = True
                 game_over = self.score_font.render("GAME OVER",True,(27,43,48))
                 self.screen.blit(game_over,(625,275))
                 press_space = self.score_font.render("Press Space To Start Over",True,(27,43,48))
                 self.screen.blit(press_space,(400,350))
                 score = self.score_font.render(f"Score: {self.score}",True,(110, 28, 5))
                 self.screen.blit(score,(700,500))
                 
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
        for goblin in self.multiple_goblins:
            goblin.update(self.player.x)
            #if goblin near death last dying words PULSE, which equals -1 
            pulse = goblin.render()
            if (pulse == -1):
                self.score += 1
                self.multiple_goblins.remove(goblin)
                self.goblins = 0
        self.screen.blit(self.real_floor,(0,35))
        #pygame.draw.rect(self.screen,(101, 173, 107),self.test_rect)
        #font
        
        
    def update_arrow(self):
        #update every arrow
        for arrow in self.player.active_projectiles:
            arrow.update(self.player.dir)
            arrow.render()
        #increase timer
        self.time += 1
        #spawn goblin every ten seconds if under 3 goblins in game
        if self.goblins < 3:
            if self.time % 300 == 0:
                self.goblins += 1
                goblin_x = random.randint(0,self.width)
                goblin_y = 600
                goblin = Goblin(goblin_x,goblin_y,self.goblin_sheet,self)
                self.multiple_goblins.append(goblin)

        #define projectiles list
        projectiles = []
        #collision boolean
        hit_goblin = False
        #for loop for every goblin
        for goblin in self.multiple_goblins:
            #append arrow to list and collision
            for arrow in self.player.active_projectiles:
                if goblin.collision(arrow.hit_box):
                    if arrow not in projectiles:
                        projectiles.append(arrow)
                    hit_goblin = True
                    break
        #render arrow no matter what
        # for arrow in self.player.active_projectiles:
        #     arrow.render()
        #delete arrow if colliding
        for arrow in projectiles:
            self.player.active_projectiles.remove(arrow)
         
        print(self.goblins)

        
    
game = Game()
game.run()
