import pygame
import random
import psycopg2
from color_palette import *

def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="snake",
        user="postgres",
        password="1488228"
    )
    return conn

def create_tables(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            max_score INTEGER DEFAULT 0,
            max_level INTEGER DEFAULT 1,
            last_played TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
    conn.commit()

def get_user_data(conn, username):
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
        
    if user:
        user_id = user[0]

        cur.execute("""
        SELECT score, level, max_score, max_level 
        FROM user_score 
        WHERE user_id = %s
        """, (user_id,))
        user_data = cur.fetchone()
        
        if user_data:
            score, level, max_score, max_level = user_data
            print(f"Welcome back, {username}!")
            print(f"Previous score: {score}, level: {level}")
            print(f"Record: {max_score} score, max level: {max_level}")
            return user_id, max_score, max_level, score, level
        else:
            cur.execute("""
            INSERT INTO user_score (user_id, score, level, max_score, max_level) 
            VALUES (%s, 0, 1, 0, 1)
            """, (user_id,))
            conn.commit()
            print(f"Welcome, {username}!")
            return user_id, 0, 1, 0, 1
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        
        cur.execute("""
        INSERT INTO user_score (user_id, score, level, max_score, max_level) 
        VALUES (%s, 0, 1, 0, 1)
        """, (user_id,))
        conn.commit()
        print(f"New player: {username}")
        return user_id, 0, 1, 0, 1

def save_progress(conn, user_id, score, level, max_score, max_level):
    cur = conn.cursor()
    new_max_score = max(score, max_score)
    new_max_level = max(level, max_level)

    cur.execute("""
    UPDATE user_score 
    SET score = %s, level = %s, max_score = %s, max_level = %s, last_played = CURRENT_TIMESTAMP 
    WHERE user_id = %s
    """, (score, level, new_max_score, new_max_level, user_id))
    conn.commit()
    print("Progress saved")
    return new_max_score, new_max_level

def main():
    conn = connect_db()
    if not conn:
        print("Server error. Game will start without the progress saving.")
        user_id, score, level, max_score, max_level = None, 0, 1, 0, 1
    else:
        create_tables(conn)
        username = input("Enter username: ").strip()
        user_id, score, level, new_max_score, new_max_level = get_user_data(conn, username)
        score = 0
        level = 1

    pygame.init()
    WIDTH, HEIGHT, CELL = 600, 600, 30
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    def draw_grid_chess():
        colors = [colorWHITE, colorGRAY]
        for i in range(HEIGHT // CELL):
            for j in range(WIDTH // CELL):
                pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

    class Point:
        def __init__(self, x, y):
            self.x, self.y = x, y

    class Snake:
        def __init__(self, initial_score=0, initial_level=1):
            self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
            self.dx = 1
            self.dy = 0
            self.score = initial_score
            self.level = initial_level

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
                return False
            return True

        def draw(self):
            head = self.body[0]
            pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
            for segment in self.body[1:]:
                pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

        def check_collision(self, food, special_food):
            head = self.body[0]
            if head.x == food.pos.x and head.y == food.pos.y:
                self.body.append(Point(self.body[-1].x, self.body[-1].y))
                self.score += food.weight
                food.respawn(self.body)
                if self.score > self.level * 3:  #Level up every 3 food collected
                    self.level += 1
                    return True  #Indicate level up
                
            # Check for special food
            if special_food.active and head.x == special_food.pos.x and head.y == special_food.pos.y:
                self.body.append(Point(self.body[-1].x, self.body[-1].y))
                self.score += special_food.weight
                self.level += 1
                special_food.active = False  #Erase special food
                return True
            return False

    class Food:
        def __init__(self):
            self.pos = Point(0, 0)
            self.weight = 1
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
            self.pos = Point(0, 0)
            self.weight = 4
            self.timer = 0

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

    FPS = 5 + (level - 1)
    clock = pygame.time.Clock()

    food = Food()
    snake = Snake(score, level)
    special_food = SpecialFood()

    running = True
    paused = False
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key == pygame.K_RIGHT and snake.dx == 0:
                        snake.dx, snake.dy = 1, 0
                    elif event.key == pygame.K_LEFT and snake.dx == 0:
                        snake.dx, snake.dy = -1, 0
                    elif event.key == pygame.K_DOWN and snake.dy == 0:
                        snake.dx, snake.dy = 0, 1
                    elif event.key == pygame.K_UP and snake.dy == 0:
                        snake.dx, snake.dy = 0, -1
                    elif event.key == pygame.K_p:  #Pause
                        paused = not paused
                        if paused:
                            print("Game paused")
                        else:
                            print("Game resumed")
                        if conn and user_id and paused:
                            max_score, max_level = save_progress(conn, user_id, snake.score, snake.level, max_score, max_level)

        if not paused and not game_over:
            draw_grid_chess()
            if not snake.move():
                game_over = True
            level_up = snake.check_collision(food, special_food)
            snake.draw()
            food.draw()
            special_food.draw()
            font = pygame.font.SysFont("Verdana", 20)
            score_text = font.render(f"Score: {snake.score}  Level: {snake.level}", True, (0, 0, 0))
            record_text = font.render(f"Record: {max(snake.score, new_max_score)}", True, (0, 0, 0))
            screen.blit(score_text, (10, 10))
            screen.blit(record_text, (10, 40))
            if level_up:
                FPS += 1
            if snake.score > 0 and snake.score % 10 == 0 and not special_food.active:
                special_food.respawn(snake.body)
            if special_food.active and pygame.time.get_ticks() - special_food.timer > 5000:
                special_food.active = False
        elif game_over:
            draw_grid_chess()
            font_large = pygame.font.SysFont("Verdana", 48)
            font = pygame.font.SysFont("Verdana", 24)
            
            game_over_text = font_large.render("GAME OVER", True, (255, 0, 0))
            score_text = font.render(f"Score: {snake.score}", True, (0, 0, 0))
            level_text = font.render(f"Level: {snake.level}", True, (0, 0, 0))
            
            screen.blit(game_over_text, (WIDTH // 2 - 140, HEIGHT // 2 - 60))
            screen.blit(score_text, (WIDTH // 2 - 60, HEIGHT // 2 + 10))
            screen.blit(level_text, (WIDTH // 2 - 60, HEIGHT // 2 + 50))

            if conn and user_id and not running:
                new_max_score, new_max_level = save_progress(conn, user_id, snake.score, snake.level, new_max_score, new_max_level)
        elif paused:
            font_pause = pygame.font.SysFont("Verdana", 48)
            pause_text = font_pause.render("PAUSED", True, (0, 0, 255))
            screen.blit(pause_text, (WIDTH // 2 - 90, HEIGHT // 2 - 30))
        
        pygame.display.flip()
        clock.tick(FPS)

    if conn and user_id:
        save_progress(conn, user_id, snake.score, snake.level, new_max_score, new_max_level)
        conn.close()
        
    pygame.quit()

if __name__ == "__main__":
    main()