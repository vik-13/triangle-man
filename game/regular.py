import pygame
import pygame.gfxdraw
from settings import *

class Regular:
    def __init__(self, pos, size):
        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(pos, size)

    def update(self, dt):
        self.render()

    def render(self):
        pygame.gfxdraw.box(self.screen, self.rect, pygame.Color('black'))


