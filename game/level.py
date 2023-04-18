import pygame
import sys
from sprite import Sprite
from pygame.math import Vector2 as Vector
from fan import Fan
from regular import Regular
from map import Map
from player import Player


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        # self.fan = Fan(Vector(500, 280))

        self.map = Map()

        self.player = Player(self.map)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self, dt):
        self.display_surface.fill('#957b50')
        self.handle_events()

        self.map.update(dt)

        self.player.update(dt)

        # self.fan.update(dt)

