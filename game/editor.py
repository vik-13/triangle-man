import pygame, sys

class Editor:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self, dt):
        self.display_surface.fill('grey')
        self.handle_events()
