import pygame
import pygame.gfxdraw
from pygame.math import Vector2 as Vector
from movable_platform import MovablePlatform
from pygame import Surface, Rect


class Weak:
    damage: bool = False
    screen: Surface
    rect: Rect
    original: Vector
    destination: Vector
    is_movable: bool
    movable_platform: MovablePlatform | None

    def __init__(self, pos, size, direction):
        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(pos, size)

        self.original = Vector(pos)
        self.destination = Vector(self.original.x + direction[0], self.original.y + direction[1])

        self.is_movable = Vector(direction).magnitude() > 0
        if self.is_movable:
            self.movable_platform = MovablePlatform(self.original, self.destination, Vector(direction).magnitude(),
                                                    Vector(size))

    def update(self, dt, camera_offset):
        if self.is_movable:
            self.movable_platform.update(dt, camera_offset)

            self.rect.topleft = self.movable_platform.pos

        self.render(camera_offset)

    def render(self, camera_offset):
        offset_rect = self.rect.copy()
        offset_rect.center -= camera_offset
        pygame.gfxdraw.box(self.screen, offset_rect, pygame.Color('green'))
