import pygame
from sprite import Sprite
from animation import Animation
from settings import *
from pygame.math import Vector2 as Vector

HORIZONTAL_SPEED = 4
FALLING_SPEED = -15
MAX_SPEED = .3
SIZE = (38, 60)
MASS = 10

MAIN = [
    [[0, 9, 36, 0, 21, 26], 'black', 'black', 1],
    [[21, 27, 34, 39, 34, 59], 'black', 'black', 1],
    [[21, 27, 21, 45, 8, 58], 'black', 'black', 1],
    [[22, 7, 29, 6, 26, 11], 'red', 'red', 1]
]

# idle, walk, jump, drop, wall, fall, die, fly
G_LIST = {
    'idle': {
        'main': MAIN,
        'animations': [[[1, 12, 37, 3, 22, 29], [22, 29, 35, 41, 34, 59], [22, 29, 21, 47, 8, 58], [23, 10, 30, 9, 27, 14]]],
        'speed': 4,
        'once': False
    },
    'walk': {
        'main': MAIN,
        'animations': [[[3, 8, 41, 5, 21, 28], [21, 27, 24, 44, 13, 60], [22, 26, 28, 44, 21, 58], [24, 9, 31, 10, 27, 14]], [[0, 9, 36, 0, 21, 26], [21, 27, 17, 44, 1, 55], [22, 26, 34, 40, 32, 58], [22, 7, 29, 6, 26, 11]], [[2, 8, 39, 3, 21, 28], [21, 26, 30, 41, 25, 60], [21, 27, 25, 45, 14, 60], [23, 8, 31, 9, 26, 13]]],
        'speed': 8,
        'once': False
    },
    'jump': {
        'main': MAIN,
        'animations': [[[1, 5, 36, -7, 24, 20], [24, 20, 26, 39, 17, 59], [24, 21, 20, 41, 8, 58], [24, 1, 30, -2, 28, 4]], [[2, 4, 39, -5, 23, 21], [23, 21, 27, 36, 17, 52], [23, 21, 23, 40, 11, 53], [25, 2, 32, 0, 29, 6]]],
        'speed': 150,
        'once': True
    },
    'drop': {
        'main': MAIN,
        'animations': [[[1, 21, 38, 22, 17, 44], [17, 43, 38, 46, 26, 58], [16, 42, 22, 56, 8, 58], [21, 25, 28, 26, 24, 30]], [0, 0, 0, 0]],
        'speed': 120,
        'once': True
    },
    'wall': {
        'main': [[[0, 2, 34, 0, 20, 21], 'black', 'black', 1], [[20, 20, 40, 30, 34, 14], 'black', 'black', 1], [[19, 20, 32, 33, 38, 53], 'black', 'black', 1], [[12, 9, 7, 4, 14, 4], 'red', 'red', 1]],
        'animations': [],
        'speed': 200,
        'once': False
    },
    'fall': {
        'main': [[[3, 0, 39, 10, 13, 26], 'black', 'black', 1], [[13, 25, 26, 38, 26, 57], 'black', 'black', 1], [[13, 25, 13, 44, 0, 57], 'black', 'black', 1], [[23, 8, 30, 10, 25, 13], 'red', 'red', 1]],
        'animations': [[0, [13, 25, 29, 33, 28, 52], [13, 25, 8, 43, -7, 51], 0]],
        'speed': 150,
        'once': True
    },
    'die': {
        'main': MAIN,
        'animations': [[[3, 56, 27, 27, 31, 58], [66, 46, 57, 60, 34, 59], [-29, 57, -8, 49, 7, 59], [21, 40, 25, 34, 26, 41]]],
        'speed': 1000,
        'once': True
    },
    'fly': {
        'main': [[[38, 0, 63, 28, 32, 27], 'black', 'black', 1], [[32, 26, 21, 40, 2, 42], 'black', 'black', 1], [[32, 26, 13, 27, 0, 14], 'black', 'black', 1], [[51, 19, 56, 24, 50, 24], 'red', 'red', 1]],
        'animations': [[[33, 0, 62, 23, 32, 27], [32, 27, 18, 37, -2, 28], [32, 26, 14, 23, 7, 9], [48, 17, 55, 19, 49, 22]]],
        'speed': 500,
        'once': False
    }
}

class Player:
    def __init__(self, map_data):
        self.map_data = map_data
        self.position = map_data.get_start() + Vector(TILE_SIZE / 2, TILE_SIZE)
        self.velocity = Vector()

        self.jump_first = False
        self.jump_second = False
        self.jump_done = False

        self.is_in_air = False
        self.is_on_floor = False

        self.status = 'idle'
        self.orientation = 'right'
        self.speed = 300

        self.rect = pygame.Rect((self.position.x, self.position.y), SIZE)

        current_animation = G_LIST[self.status]
        self.character = Animation(current_animation['main'], current_animation['animations'], self.rect, SIZE, current_animation['speed'], current_animation['once'])

    def reset(self, backward=False):
        self.velocity = Vector()
        if backward:
            self.position = self.map_data.get_end()
        else:
            self.position = self.map_data.get_start()
        self.position += Vector(TILE_SIZE / 2, TILE_SIZE)
        self.rect = pygame.Rect((self.position.x, self.position.y), SIZE)
        self.is_in_air = False

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.velocity.x = 1
            self.orientation = 'right'
        elif keys[pygame.K_LEFT]:
            self.velocity.x = -1
            self.orientation = 'left'
        else:
            self.velocity.x = 0

        if keys[pygame.K_SPACE] and self.velocity.y >= 0 and self.is_on_floor:
            self.velocity.y = -3

    def update_status(self):
        if self.is_in_air and self.velocity.y <= 0:
            next_status = 'jump'
        elif self.is_in_air and self.velocity.y > 0:
            next_status = 'fall'
        else:
            next_status = 'walk' if self.velocity.x != 0 else 'idle'

        if next_status != self.status:
            self.status = next_status
            current_animation = G_LIST[self.status]
            self.character = Animation(current_animation['main'], current_animation['animations'], self.rect, SIZE,
                                       current_animation['speed'], current_animation['once'])


    def move(self, dt):
        # vertical
        self.position.y += self.velocity.y * self.speed * dt
        self.rect.centery = round(self.position.y)
        self.collision('vertical')

        # horizontal
        self.position.x += self.velocity.x * self.speed * dt
        self.rect.centerx = round(self.position.x)
        self.collision('horizontal')

    def collision(self, direction):
        for block in self.map_data.get_blocks():
            if block.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    self.rect.right = block.rect.left if self.velocity.x > 0 else self.rect.right
                    self.rect.left = block.rect.right if self.velocity.x < 0 else self.rect.left
                    self.rect.centerx, self.position.x = self.rect.centerx, self.rect.centerx
                else:
                    self.rect.bottom = block.rect.top if self.velocity.y >= 0 else self.rect.bottom
                    self.rect.top = block.rect.bottom if self.velocity.y < 0 else self.rect.top
                    self.rect.centery, self.position.y = self.rect.centery, self.rect.centery
                    self.velocity.y = 0

    def apply_gravity(self, dt):
        self.velocity.y += GRAVITY[1] * dt
        self.rect.y += self.velocity.y

    def update(self, dt, camera_offset):
        self.input()
        self.apply_gravity(dt)
        self.move(dt)
        self.check_on_floor()

        self.update_status()

        self.character.rect = self.rect

        self.character.update(dt, camera_offset, self.orientation == 'left')

    def check_on_floor(self):
        floor_rect = pygame.Rect(self.rect.bottomleft, (self.rect.width, 2))
        floor_blocks = [block for block in self.map_data.get_blocks() if block.rect.colliderect(floor_rect)]
        if len(floor_blocks) >= 1 and floor_blocks[0].is_movable:
            block_velocity = floor_blocks[0].movable_platform.velocity
            self.position.x += block_velocity
            self.rect.centerx = round(self.position.x)
        self.is_on_floor = True if floor_blocks else False
        self.is_in_air = not self.is_on_floor


