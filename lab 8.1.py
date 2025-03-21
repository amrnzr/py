import pygame
import random
import time

pygame.init()
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#set_mode() takes a tuple as an argument
image_background = pygame.image.load('AnimatedStreet.png')
image_player = pygame.image.load('Player.png')
image_enemy = pygame.image.load('Enemy.png')
original_coin = pygame.image.load('gold_coin.png')
image_coin = pygame.transform.scale(original_coin, (30, 30))
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)
sound_crash = pygame.mixer.Sound('crash.wav')
font = pygame.font.SysFont("Verdana", 60)
image_game_over = font.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))
coin_font = pygame.font.SysFont("Verdana", 30)

#Track the number of collected coins
coins_collected = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5
        # or
        # self.rect.midbottom = (WIDTH // 2, HEIGHT)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 10
        # or
        # self.rect.midbottom = (WIDTH // 2, HEIGHT)
    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.bottom = 0
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()

#New Coin class for collectible coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect()
        self.speed = 5
        #Set initial position after getting the rect dimensions
        self.generate_random_rect()
        
    def generate_random_rect(self):
        #Valid width value before calculating random position
        coin_width = self.rect.width
        #Don't exceed screen boundaries
        max_x = max(0, WIDTH - coin_width)
        self.rect.left = random.randint(0, max_x)
        self.rect.bottom = 0
        
    def move(self):
        #Move the coin down the screen
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            #If coin goes off-screen generate a new position
            self.generate_random_rect()

running = True
#this object allows us to set the FPS
clock = pygame.time.Clock()
FPS = 60
player = Player()
enemy = Enemy()
enemy.generate_random_rect()  #Initialize enemy position

#Initialize coin sprite group
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

#Add initial enemy to sprite groups
all_sprites.add(player, enemy)
enemy_sprites.add(enemy)

#Generate initial coin
coin = Coin()
all_sprites.add(coin)
coin_sprites.add(coin)

#Variable to track when to spawn new coins
coin_spawn_timer = 0
coin_spawn_interval = 3000

while running:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Check the time to spawn a new coin
    if current_time - coin_spawn_timer > coin_spawn_interval:
        #Reset the timer
        coin_spawn_timer = current_time
        #Randomly decide whether to spawn a coin
        if random.random() > 0.5:
            new_coin = Coin()
            all_sprites.add(new_coin)
            coin_sprites.add(new_coin)
    
    player.move()
    screen.blit(image_background, (0, 0))
    
    #Move and draw all sprites
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
    
    #Check for coin collection
    coins_hit = pygame.sprite.spritecollide(player, coin_sprites, True)
    for coin in coins_hit:
        coins_collected += 1
        new_coin = Coin()
        all_sprites.add(new_coin)
        coin_sprites.add(new_coin)
    
    #Display coin counter
    coin_counter = coin_font.render(f"Coins: {coins_collected}", True, "white")
    coin_counter_rect = coin_counter.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(coin_counter, coin_counter_rect)
    
    #Check for collision with enemy
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)
        running = False
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        
        #Show final coin count on game over screen
        final_score = coin_font.render(f"Coins collected: {coins_collected}", True, "white")
        final_score_rect = final_score.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70))
        screen.blit(final_score, final_score_rect)
        
        pygame.display.flip()
        time.sleep(3)
    
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()