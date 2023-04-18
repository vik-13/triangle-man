import pygame
import pygame.gfxdraw
from pygame.math import Vector2 as Vector
from settings import *
from movable_platform import MovablePlatform


class Spike:
    def __init__(self, pos, size, direction):
        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(pos, size)

        self.original = Vector(pos)
        self.destination = Vector(self.original.x + direction[0], self.original.y + direction[1])

        self.is_movable = Vector(direction).magnitude() > 0
        if self.is_movable:
            self.movable_platform = MovablePlatform(self.original, self.destination, Vector(direction).magnitude(), Vector(size))

    def update(self, dt):
        if self.is_movable:
            self.movable_platform.update(dt)

            self.rect.topleft = self.movable_platform.pos

        self.render()

    def render(self):
        pygame.gfxdraw.box(self.screen, self.rect, pygame.Color('#8e2c0b'))


