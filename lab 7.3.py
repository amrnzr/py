import pygame

pygame.init()
width, height = 500, 500
ball_rad = 25
ball_col = (255, 0, 0)
bg_col = (255, 255, 255)
step = 20

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball")

x, y = width // 2, height // 2

running = True
while running:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x - ball_rad - step >= 0:
        x -= step
    if keys[pygame.K_RIGHT] and x + ball_rad + step <= width:
        x += step
    if keys[pygame.K_UP] and y - ball_rad - step >= 0:
        y -= step
    if keys[pygame.K_DOWN] and y + ball_rad + step <= height:
        y += step
    
    screen.fill(bg_col)
    pygame.draw.circle(screen, ball_col, (x, y), ball_rad)
    pygame.display.update()

pygame.quit()
