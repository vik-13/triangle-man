import pygame
from levels import *
from settings import *
from regular import Regular
from fan import Fan

class Map:
    def __init__(self):
        self.level_index = 0
        self.map = {}
        self.generate_map()

    def generate_map(self):
        self.reset_map()
        current_map_data = LEVELS[self.level_index]

        for element in current_map_data:
            element_type = element[0]
            pos = (element[1] * TILE_SIZE, WINDOW_HEIGHT + (-element[2] - element[4]) * TILE_SIZE)
            size = (element[3] * TILE_SIZE ,element[4] * TILE_SIZE)

            if element_type == 0:
                self.map['blocks'].append(Regular(pos, size))
            elif element_type == 8:
                self.map['elements'].append(Fan(pos))
            elif element_type == 6:
                self.map['start'] = pos
            elif element_type == 7:
                self.map['end'] = pos

    def next_level(self):
        self.level_index += 1
        self.generate_map()

    def reset_map(self):
        self.map = {
            'blocks': [],
            'elements': [],
            'start': (0, 0),
            'end': (0, 0)
        }

    def update(self, dt):
        for block in self.map['blocks']:
            block.update(dt)

        for block in self.map['elements']:
            block.update(dt)
