import pygame
import random
from color_palette import *

pygame.init()

WIDTH, HEIGHT, CELL = 600, 600, 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Chessboard pattern on the screen
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

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
        
        #Check collision
        if (self.body[0].x < 0 or self.body[0].x >= WIDTH // CELL or
            self.body[0].y < 0 or self.body[0].y >= HEIGHT // CELL or #Wall collision
            any(seg.x == self.body[0].x and seg.y == self.body[0].y for seg in self.body[1:])): #Self-collision
            pygame.quit()
            exit()

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food, special_food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            self.score += food.weight
            food.respawn(self.body)
            if self.score > self.level * 3:  #Level up every 3 food collected
                self.level += 1
                return True  #Indicate level up
            
        # Check for special food
        if special_food.active and head.x == special_food.pos.x and head.y == special_food.pos.y:
            self.body.append(Point(head.x, head.y))
            self.score += special_food.weight
            self.level += 1
            special_food.active = False  #Erase special food
        return False

class Food:
    def __init__(self):
        self.respawn([]) # Initialize with a random position

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def respawn(self, snake_body):
        while True:
            new_pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
            if not any(seg.x == new_pos.x and seg.y == new_pos.y for seg in snake_body):
                self.pos = new_pos
                self.weight = random.randint(1, 2) # Random weight for food
                break

class SpecialFood:
    def __init__(self):
        self.active = False
        self.respawn([]) # Initialize with a random position

    def draw(self):
        if self.active:
            pygame.draw.rect(screen, colorBLUE, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
    
    def respawn(self, snake_body):
        while True:
            new_pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
            if not any(seg.x == new_pos.x and seg.y == new_pos.y for seg in snake_body):
                self.pos = new_pos
                self.weight = 4
                self.timer = pygame.time.get_ticks() # Reset timer
                self.active = True
                break

FPS = 5
clock = pygame.time.Clock()

food = Food()
snake = Snake()
special_food = SpecialFood()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1

    draw_grid_chess()
    snake.move()
    level_up = snake.check_collision(food, special_food)
    snake.draw()
    food.draw()
    special_food.draw()

    #Display score and level
    font = pygame.font.SysFont("Verdana", 20)
    screen.blit(font.render(f"Score: {snake.score}  Level: {snake.level}", True, "black"), (10, 10))
    
    if level_up:
        FPS += 1 #Increase speed on level up
    if snake.score % 10 == 0 and not special_food.active: # Spawn special food when points devided by 10
        special_food.respawn(snake.body)
    if special_food.active and pygame.time.get_ticks() - special_food.timer > 5000: # 5 seconds lifetime
        special_food.active = False
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()