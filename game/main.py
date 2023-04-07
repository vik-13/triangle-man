import pygame
from editor import Editor
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.editor = Editor()

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            self.editor.run(dt)


if __name__ == '__main__':
    game = Game()
    game.run()
