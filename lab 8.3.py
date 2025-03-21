import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colors = [colorRED, colorBLUE, colorBLACK]
color_index = 0

clock = pygame.time.Clock()
THICKNESS = 5
drawing = False
draw_mode = "line"
start_pos = (0, 0)
end_pos = (0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)
            if event.key == pygame.K_r:
                draw_mode = "rectangle"
            if event.key == pygame.K_c:
                draw_mode = "circle"
            if event.key == pygame.K_l:
                draw_mode = "line"
            if event.key == pygame.K_e:
                draw_mode = "eraser"
            if event.key == pygame.K_TAB:
                color_index = (color_index + 1) % len(colors)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEMOTION and drawing:
            end_pos = event.pos
            if draw_mode == "line":
                pygame.draw.line(screen, colors[color_index], start_pos, end_pos, THICKNESS)
                start_pos = end_pos
            elif draw_mode == "eraser":
                pygame.draw.line(screen, colorWHITE, start_pos, end_pos, THICKNESS + 10)
                start_pos = end_pos

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            end_pos = event.pos
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

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
