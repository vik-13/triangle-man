import pygame
import pygame.gfxdraw

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# Set the scale factor for retina screens
scale_factor = 1

# Double the size of the drawn polygons for retina screens
polygon_scale = 1

data = [
            [[0, 9, 36, 0, 21, 26], 'silver', 'silver', 1],
            [[21, 27, 34, 39, 34, 59], 'silver', 'silver', 1],
            [[21, 27, 21, 45, 8, 58], 'silver', 'silver', 1],
            [[22, 7, 29, 6, 26, 11], 'red', 'red', 1]
        ]

# Loop through each layer in the data array and draw it
for layer in data:
    coords = layer[0]
    stroke_color = layer[1]
    fill_color = layer[2]
    connect_dots = layer[3]

    # Create a list of points from the coordinates
    points = [(polygon_scale*coords[i], polygon_scale*coords[i+1]) for i in range(0, len(coords), 2)]

    # If the layer is supposed to connect the first and last dots, add the first point to the end of the list
    if connect_dots:
        points.append(points[0])

    # Draw an anti-aliased filled polygon on the main screen Surface, scaled up for retina screens
    pygame.gfxdraw.aapolygon(screen, points, pygame.Color(fill_color))
    pygame.gfxdraw.filled_polygon(screen, points, pygame.Color(fill_color))

    # Draw an anti-aliased polygon stroke on the main screen Surface, scaled up for retina screens
    # pygame.gfxdraw.aapolygon(screen, points, pygame.Color(stroke_color))
    # pygame.gfxdraw.polygon(screen, points, pygame.Color(stroke_color))

# Update the screen
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()