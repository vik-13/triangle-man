import pygame
from sprite import Sprite
from settings import *
from pygame.math import Vector2 as Vector

HORIZONTAL_SPEED = 4
FALLING_SPEED = -15
MAX_SPEED = .3
SIZE = (38, 60)
MASS = .9

GRAPHIC = [
    [[0, 9, 36, 0, 21, 26], 'black', 'black', 1],
    [[21, 27, 34, 39, 34, 59], 'black', 'black', 1],
    [[21, 27, 21, 45, 8, 58], 'black', 'black', 1],
    [[22, 7, 29, 6, 26, 11], 'red', 'red', 1]
]


class Player:
    def __init__(self, map_data):
        self.map_data = map_data
        self.position = Vector(map_data.get_start())
        self.velocity = Vector()

        self.jump_first = False
        self.jump_second = False
        self.jump_done = False

        self.is_in_air = False

        self.rect = pygame.Rect((0, 0), SIZE)
        self.rect.midbottom = (self.position[0] + TILE_SIZE / 2, self.position[1] + TILE_SIZE)

        self.character = Sprite(GRAPHIC, self.rect, SIZE)

    def reset(self):
        self.velocity = Vector()
        self.position = Vector(self.map_data.get_start())
        self.rect = pygame.Rect((0, 0), SIZE)
        self.rect.midbottom = (self.position[0] + TILE_SIZE / 2, self.position[1] + TILE_SIZE)
        self.is_in_air = False

    def update(self, dt):
        keys = pygame.key.get_pressed()

        temp_velocity = self.velocity.copy() if self.velocity.magnitude() <= 1 else self.velocity.copy().normalize()
        acceleration = temp_velocity * FALLING_SPEED
        # acceleration += Vector(GRAVITY) * MASS
        acceleration *= dt

        if keys[pygame.K_RIGHT]:
            acceleration += Vector(HORIZONTAL_SPEED * dt, 0)
        elif keys[pygame.K_LEFT]:
            acceleration += Vector(-HORIZONTAL_SPEED * dt, 0)

        self.velocity += acceleration

        if self.velocity.x < -MAX_SPEED:
            self.velocity.x = -MAX_SPEED
        elif self.velocity.x > MAX_SPEED:
            self.velocity.x = MAX_SPEED

        self.position += self.velocity

        self.rect.midbottom = (self.position[0] + TILE_SIZE / 2, self.position[1] + TILE_SIZE)
        self.character.rect = self.rect



        self.character.update(dt)

    def get_collisions(self):
        for block in self.map_data.get_blocks():
            if self.rect.colliderect(block.rect):

