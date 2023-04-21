import pygame
from pygame.math import Vector2 as Vector
from settings import *


class Camera:
    def __init__(self):
        self.offset = Vector()

    def update(self, map_data, player):
        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

        self.offset.y = 0 if self.offset.y > 0 else self.offset.y
        self.offset.x = 0 if self.offset.x < 0 else self.offset.x
        self.offset.x = map_data.get_end()[0] - WINDOW_WIDTH if self.offset.x > map_data.get_end()[0] - WINDOW_WIDTH else self.offset.x
