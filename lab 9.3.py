import pygame
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))

# Define colors
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colors = [colorRED, colorBLUE, colorBLACK]
color_index = 0  # Start with the first color

clock = pygame.time.Clock()
THICKNESS = 5  # Default thickness of shapes and lines
drawing = False

# Drawing mode variable
draw_mode = "line"
start_pos = (0, 0)
end_pos = (0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle keyboard inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1  # Increase thickness
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)  # Decrease thickness but not below 1
            if event.key == pygame.K_r:
                draw_mode = "rectangle"
            if event.key == pygame.K_c:
                draw_mode = "circle"
            if event.key == pygame.K_l:
                draw_mode = "line"
            if event.key == pygame.K_e:
                draw_mode = "eraser"
            if event.key == pygame.K_s:
                draw_mode = "square"
            if event.key == pygame.K_t:
                draw_mode = "triangle"
            if event.key == pygame.K_y:
                draw_mode = "e_triangle"
            if event.key == pygame.K_i:
                draw_mode = "rhombus"
            if event.key == pygame.K_TAB:
                color_index = (color_index + 1) % len(colors)  # Cycle through colors

        # Handle mouse inputs
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEMOTION and drawing:
            end_pos = event.pos
            if draw_mode == "line":
                pygame.draw.line(screen, colors[color_index], start_pos, end_pos, THICKNESS)
                start_pos = end_pos  # Update start position for continuous drawing
            elif draw_mode == "eraser":
                pygame.draw.line(screen, colorWHITE, start_pos, end_pos, THICKNESS + 10)
                start_pos = end_pos

        # Handle mouse button release
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            end_pos = event.pos
            # Draw the final shape based on the selected mode
            if draw_mode == "rectangle":
                rect_x = min(start_pos[0], end_pos[0])
                rect_y = min(start_pos[1], end_pos[1])
                rect_width = abs(start_pos[0] - end_pos[0])
                rect_height = abs(start_pos[1] - end_pos[1])
                pygame.draw.rect(screen, colors[color_index], (rect_x, rect_y, rect_width, rect_height), THICKNESS)
            elif draw_mode == "circle":
                center = start_pos
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, colors[color_index], center, radius, THICKNESS)
            elif draw_mode == "square":
                side = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, colors[color_index], (start_pos[0], start_pos[1], side, side), THICKNESS)
            elif draw_mode == "triangle":
                pygame.draw.polygon(screen, colors[color_index], [start_pos, end_pos, (start_pos[0], end_pos[1])], THICKNESS)
            elif draw_mode == "e_triangle":
                height = abs(end_pos[1] - start_pos[1])
                base_half = height / math.sqrt(3)
                pygame.draw.polygon(screen, colors[color_index], [(start_pos[0], start_pos[1] - height), (start_pos[0] - base_half, start_pos[1]), (start_pos[0] + base_half, start_pos[1])], THICKNESS)
            elif draw_mode == "rhombus":
                width = abs(end_pos[0] - start_pos[0])
                height = abs(end_pos[1] - start_pos[1])
                pygame.draw.polygon(screen, colors[color_index], [(start_pos[0], start_pos[1] - height // 2), (start_pos[0] + width // 2, start_pos[1]), (start_pos[0], start_pos[1] + height // 2), (start_pos[0] - width // 2, start_pos[1])], THICKNESS)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()