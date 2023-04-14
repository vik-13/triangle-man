import pygame

class Level:
    def __init__(self):
        self.display_surf = pygame.display.get_surface()

    def draw_test_sprite(self):
        surf = pygame.surface.Surface((100, 100))
        surf.fill('yellow')
        self.display_surf.blit(surf, (100, 100))

    def run(self, dt):
        self.draw_test_sprite()
