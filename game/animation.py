from sprite import Sprite
import copy


class Animation(Sprite):
    def __init__(self, graphic, animations, pos, size, speed, once=False):
        super().__init__(graphic, pos, size)

        self.total = len(animations) + 1
        self.slides = []
        self.index = 0
        self.time = 0
        self.last = 0
        self.is_finished = False
        self.speed = speed
        self.once = once
        self.data = []

        self.slides.append(graphic)

        for animation in animations:
            slide = []
            for index, item in enumerate(graphic):
                slide.append(copy.deepcopy(item))
                if animation[index]:
                    slide[index][0] = list(animation[index])
            self.slides.append(slide)

    def update(self, dt, camera_offset, invert=False):
        self.index += self.speed * dt
        if self.index >= len(self.slides):
            self.index = 0
            self.is_finished = True

        next_index = int(self.index + 1 if self.index + 1 < self.total else self.index if self.once else 0)

        tt = self.index - int(self.index)

        if self.once and self.is_finished:
            self.data = self.slides[len(self.slides) - 1]
        else:
            slide = self.slides[int(self.index)]
            self.data = []

            for layer_index, layer in enumerate(slide):
                self.data.append([])
                for item_index, item in enumerate(layer):
                    if item_index == 0:
                        coords = []
                        for coord_index, coord in enumerate(item):
                            coords.append(coord + (self.slides[next_index][layer_index][item_index][coord_index] - coord) * tt)
                        self.data[layer_index].append(coords)
                    else:
                        self.data[layer_index].append(item)

        self.render(camera_offset, invert)
