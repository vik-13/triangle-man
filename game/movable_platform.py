import pygame
import pygame.gfxdraw
from settings import *
from sprite import Sprite
from pygame.math import Vector2 as Vector


class MovablePlatform:
    def __init__(self, original, destination, overall_distance, size):
        self.display_surface = pygame.display.get_surface()
        self.original = original
        self.destination = destination
        self.overall_distance = overall_distance
        self.distance = 0
        self.current = 0
        self.pos = self.original.copy()
        self.direction = 1

        self.g_holder_1_pos = Vector(self.original.x + (size.x / 2) - 20, self.original.y + (size.y / 2) - 20)
        self.g_holder_2_pos = Vector(self.destination.x + (size.x / 2) - 20, self.destination.y + (size.y / 2) - 20)

        self.gHolder1 = Sprite([
            [[12, 0, 0, 22, 11, 40, 40, 36, 40, 4], 'black', 'black', 1],
            [[19, 16, 16, 20, 19, 24, 24, 23, 26, 17], '#4d4d00', '#4d4d00', 1]
        ], self.g_holder_1_pos, (40, 40))

        self.gHolder2 = Sprite([
            [[12, 0, 0, 22, 11, 40, 40, 36, 40, 4], 'black', 'black', 1],
            [[19, 16, 16, 20, 19, 24, 24, 23, 26, 17], '#4d4d00', '#4d4d00', 1]
        ], self.g_holder_2_pos, (40, 40))

    def update(self, dt):
        next_pos = self.distance / self.overall_distance

        next_pos = 1 if next_pos > 1 else 0 if next_pos < 0 else next_pos

        self.pos.x = pygame.math.lerp(self.original.x, self.destination.x, next_pos)
        self.pos.y = pygame.math.lerp(self.original.y, self.destination.y, next_pos)

        if self.direction == 1 and next_pos == 1 or self.direction == -1 and next_pos == 0:
            self.direction *= -1

        self.distance += SPEED_MOVABLE * self.direction * dt

        self.render()

        self.gHolder1.update(dt)
        self.gHolder2.update(dt)

    def render(self):
        pygame.gfxdraw.line(
            self.display_surface,
            int(self.g_holder_1_pos.x) + 20,
            int(self.g_holder_1_pos.y) + 20,
            int(self.g_holder_2_pos.x) + 20,
            int(self.g_holder_2_pos.y) + 20,
            pygame.Color('#4d4d00'))
