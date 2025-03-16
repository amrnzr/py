import pygame
import time
import datetime

pygame.init()
clock = pygame.image.load("clock.png")
m_hand = pygame.image.load("min_hand.png")
s_hand = pygame.image.load("sec_hand.png")

clock_rect = clock.get_rect()
width, height = clock_rect.size
center = (width // 2, height // 2)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Clock")

def rotate(image, angle, pivot):
    r_image = pygame.transform.rotate(image, -angle)
    r_rect = r_image.get_rect(center=pivot)
    return r_image, r_rect

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    now = datetime.datetime.now()
    s = now.second
    m = now.minute
    s_angle = (s / 60) * 360
    m_angle = (m / 60) * 360
    screen.blit(clock, (0, 0))
    r_m_hand, m_rect = rotate(m_hand, m_angle, center)
    r_s_hand, s_rect = rotate(s_hand, s_angle, center)
    screen.blit(r_m_hand, m_rect.topleft)
    screen.blit(r_s_hand, s_rect.topleft)
    pygame.display.update()
    time.sleep(1)

pygame.quit()