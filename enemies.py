import pygame,sys
from sprites import sprites
from player import Player

class Enemies:
    def __init__(self,x,y,img,game):
        pygame.init()
        self.x = x
        self.y = y
        self.img = img
        self.game = game
    def update():
        print("update")
    def render():
        print("render")