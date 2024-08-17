import pygame,sys
from sprites import sprites

class Player:
    def __init__(self,x,y,sprite_sheet,game):
        pygame.init()
        self.x = x
        self.y = y
        self.sprite_sheet = sprite_sheet
        self.game = game
        self.xspeed = 0
        self.yspeed = 0
        self.action = "idle"
        self.frame = 0
    
    def render(self):
        player_frame = pygame.transform.scale(self.sprite_sheet.get_frame(self.action,self.frame),(288 * 2.5,128 * 2.5))
        self.game.screen.blit(player_frame,(self.x,self.y))
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.xspeed += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
        self.x = (self.x + self.xspeed) * 0.9
        