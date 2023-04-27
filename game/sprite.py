import pygame
import pygame.gfxdraw


class Sprite:
    def __init__(self, data, pos, size):
        self.surf = pygame.display.get_surface()
        self.data = data

        # TODO: Calculate real size based on data
        self.rect = pygame.Rect((pos.x, pos.y), size)

    def update(self, dt, camera_offset, invert=False):
        self.render(camera_offset, invert)

    def render(self, camera_offset, invert):
        offset_rect = self.rect.copy()
        offset_rect.center -= camera_offset
        for layer in self.data:
            coords = layer[0]
            stroke_color = layer[1]
            fill_color = layer[2]
            connect_dots = layer[3]

            points = [(offset_rect.x + coords[i] if not invert else self.rect.width + offset_rect.x - coords[i], offset_rect.y + coords[i + 1]) for i in range(0, len(coords), 2)]

            if connect_dots:
                points.append(points[0])

            pygame.gfxdraw.aapolygon(self.surf, points, pygame.Color(stroke_color))
            pygame.gfxdraw.filled_polygon(self.surf, points, pygame.Color(fill_color))

       #  pygame.draw.rect(self.surf, 'red', offset_rect, 1)

