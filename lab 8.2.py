import pygame
import random
from color_palette import *

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30

screen = pygame.display.set_mode((HEIGHT, WIDTH))

#Chessboard pattern on the screen
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.score = 0
        self.level = 1

    def move(self):
        #Move body segments
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        #Move head
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        #Check wall collision
        if self.body[0].x < 0 or self.body[0].x >= WIDTH // CELL or self.body[0].y < 0 or self.body[0].y >= HEIGHT // CELL:
            pygame.quit()
            exit()

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            self.score += 1
            food.respawn(self.body)
            if self.score % 3 == 0:  #Level up every 3 food collected
                self.level += 1
                return True  #Indicate level up
        return False

class Food:
    def __init__(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def respawn(self, snake_body):
        while True:
            new_pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
            if not any(segment.x == new_pos.x and segment.y == new_pos.y for segment in snake_body):
                self.pos = new_pos
                break

FPS = 5
clock = pygame.time.Clock()

food = Food()
snake = Snake()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx = 0
                snake.dy = -1

    draw_grid_chess()
    snake.move()
    level_up = snake.check_collision(food)
    snake.draw()
    food.draw()

    #Display score and level
    font = pygame.font.SysFont("Verdana", 20)
    score_text = font.render(f"Score: {snake.score}  Level: {snake.level}", True, "black")
    screen.blit(score_text, (10, 10))
    
    if level_up:
        FPS += 1  #Increase speed on level up
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()