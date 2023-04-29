import pygame
import sys
from sprite import Sprite
from pygame.math import Vector2 as Vector
from fan import Fan
from regular import Regular
from map import Map
from player import Player
from camera import Camera
from settings import *


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.map = Map()

        self.player = Player(self.map)

        self.camera = Camera()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self, dt):
        self.display_surface.fill('#957b50')
        self.handle_events()

        self.camera.update(self.map, self.player)

        self.map.update(dt, self.camera.offset)

        self.player.update(dt, self.camera.offset)

        if self.player.is_dead:
            self.map.restart_level()
            self.player.reset()

        # End level
        if self.player.position.x < 0:
            self.map.previous_level()
            self.player.reset(True)

        if self.player.position.x >= self.map.get_end().x + TILE_SIZE:
            self.map.next_level()
            self.player.reset()

        # Fall down
        if self.player.position.y > WINDOW_HEIGHT:
            self.map.restart_level()
            self.player.reset()


