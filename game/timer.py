import pygame


class Timer:
    duration: int
    active: bool
    start_time: int

    def __init__(self, duration: int) -> None:
        self.duration = duration
        self.active = False
        self.start_time = 0

    def activate(self) -> None:
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self) -> None:
        self.active = False
        self.start_time = 0

    def update(self) -> None:
        current_time: int = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration:
            self.deactivate()
