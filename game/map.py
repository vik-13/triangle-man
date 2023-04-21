import pygame
from levels import *
from settings import *
from regular import Regular
from spike import Spike
from ice import Ice
from weak import Weak
from fan import Fan
from pygame.math import Vector2 as Vector

class Map:
    def __init__(self):
        self.level_index = 6
        self.map = {}
        self.generate_map()

    def get_start(self):
        return Vector(self.map['start']) if self.map['start'] else Vector(0, 0)

    def get_end(self):
        return Vector(self.map['end']) if self.map['end'] else Vector(0, 0)

    def get_blocks(self):
        return self.map['blocks']

    def get_elements(self):
        return self.map['elements']

    def generate_map(self):
        self.reset_map()
        current_map_data = LEVELS[self.level_index]

        for element in current_map_data:
            element_type = element[0]
            pos = (element[1] * TILE_SIZE, WINDOW_HEIGHT + (-element[2] - element[4]) * TILE_SIZE)
            size = (element[3] * TILE_SIZE, element[4] * TILE_SIZE)
            direction = (element[5] * TILE_SIZE, -element[6] * TILE_SIZE) if len(element) > 5 else (0, 0)

            if element_type == 0:
                self.map['blocks'].append(Regular(pos, size, direction))
            elif element_type == 1:
                self.map['blocks'].append(Spike(pos, size, direction))
            elif element_type == 2:
                self.map['blocks'].append(Ice(pos, size, direction))
            elif element_type == 4:
                self.map['blocks'].append(Weak(pos, size, direction))
            elif element_type == 8:
                self.map['elements'].append(Fan(pos))
            elif element_type == 6:
                self.map['start'] = pos
            elif element_type == 7:
                self.map['end'] = pos

    def restart_level(self):
        self.generate_map()

    def next_level(self):
        self.level_index += 1
        self.level_index = len(LEVELS) - 1 if self.level_index >= len(LEVELS) else self.level_index
        self.generate_map()

    def reset_map(self):
        self.map = {
            'blocks': [],
            'elements': [],
            'start': (0, 0),
            'end': (0, 0)
        }

    def update(self, dt, camera_offset):
        for block in self.map['blocks']:
            block.update(dt, camera_offset)

        for element in self.map['elements']:
            element.update(dt, camera_offset)
