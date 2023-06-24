from animation import Animation
from sprite import Graphic


GRAPHIC: Graphic = [
    ((1, 56, 118, 55, 109, 44, 9, 45), 'black', 'black', 1),
    ((0, 50, 0, 81, 120, 81, 120, 50), 'black', 'black', 1),
    ((8, 60, 7, 66, 11, 69, 15, 68, 15, 62), '#4d4d00', '#4d4d00', 1),
    ((103, 59, 108, 62, 107, 68, 100, 69, 99, 62), '#4d4d00', '#4d4d00', 1),
    ((18, 45, 14, 34, 14, 27, 12, 18, 15, 11, 18, 1, 19, 1, 17, 11, 14, 17, 17, 26, 18, 34, 20, 44), 'black', 'black',
     1),
    ((30, 46, 27, 37, 29, 30, 25, 15, 29, 6, 29, 0, 32, 0, 31, 6, 27, 15, 31, 29, 30, 37, 33, 45), 'black', 'black', 1),
    ((62, 45, 64, 44, 63, 30, 61, 21, 64, 12, 65, 1, 62, 1, 60, 11, 58, 21, 61, 30), 'black', 'black', 1),
    ((90, 45, 92, 45, 91, 37, 92, 26, 95, 17, 94, 8, 94, 2, 91, 2, 92, 9, 92, 16, 88, 25, 88, 37), 'black', 'black', 1)]

ANIMATIONS = [
    [0, 0, 0, 0, [18, 45, 23, 34, 24, 26, 23, 20, 13, 19, 10, 13, 13, 8, 16, 16, 26, 17, 27, 26, 25, 35, 20, 44],
     [30, 46, 37, 37, 39, 30, 41, 16, 44, 9, 36, 1, 41, 1, 47, 8, 44, 17, 42, 29, 41, 37, 33, 45],
     [62, 45, 64, 44, 58, 30, 67, 26, 73, 21, 63, 10, 62, 17, 69, 20, 64, 24, 56, 31],
     [90, 45, 92, 45, 95, 37, 101, 24, 99, 16, 92, 10, 85, 5, 82, 6, 88, 13, 96, 17, 99, 25, 92, 37]],
    [0, 0, 0, 0, [17, 45, 9, 35, 4, 29, 2, 19, 3, 12, 18, 13, 19, 16, 7, 14, 6, 20, 9, 28, 14, 35, 19, 44],
     [30, 46, 24, 38, 21, 31, 12, 20, 7, 14, 1, 10, 4, 8, 12, 14, 17, 20, 25, 30, 27, 38, 33, 45],
     [62, 45, 64, 44, 70, 31, 65, 18, 56, 13, 44, 10, 42, 13, 52, 15, 62, 20, 67, 32],
     [90, 45, 92, 45, 88, 36, 83, 28, 83, 21, 86, 13, 94, 14, 93, 9, 84, 12, 79, 20, 79, 28, 84, 36]]]


SPEED = 10

class Fan(Animation):
    def __init__(self, pos):
        self.damage = False
        super().__init__(GRAPHIC, ANIMATIONS, pos, (122, 82), SPEED)



