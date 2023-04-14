import pygame
import sys
from level.sprite import Sprite
from pygame.math import Vector2 as Vector
from level.fan import Fan


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.character = Sprite([
            [[0, 9, 36, 0, 21, 26], 'black', 'black', 1],
            [[21, 27, 34, 39, 34, 59], 'black', 'black', 1],
            [[21, 27, 21, 45, 8, 58], 'black', 'black', 1],
            [[22, 7, 29, 6, 26, 11], 'red', 'red', 1]
        ], Vector(500, 100), (38, 60))

        self.fan = Fan(Vector(200, 400))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self, dt):
        self.display_surface.fill('#957b50')
        self.handle_events()

        self.character.update(dt)

        self.fan.update(dt)
