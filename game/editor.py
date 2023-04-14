import pygame, sys
from settings import *

class Editor:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.test_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        data = [
            [[0, 9, 36, 0, 21, 26], '', 'black', 1],
            [[21, 27, 34, 39, 34, 59], '', 'black', 1],
            [[21, 27, 21, 45, 8, 58], '', 'black', 1],
            [[22, 7, 29, 6, 26, 11], '', 'red', 1]
        ]
        pygame.draw.rect(self.test_surf, 'yellow', ((10, 10), (50, 50)))
        pygame.draw.line(self.test_surf, 'red', (0, 100), (WINDOW_WIDTH, 200))
        self.display_surface.blit(self.test_surf, (0, 0))

    def run(self, dt):
        self.display_surface.fill('grey')
        self.handle_events()

        self.draw()
