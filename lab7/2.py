import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ball_radius = 25
ball_x = 375
ball_y = 275
ball_speed = 20
while True:
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - ball_speed >= ball_radius:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y + ball_speed <= 600 - ball_radius:
        ball_y += ball_speed
    if keys[pygame.K_LEFT] and ball_x - ball_speed >= ball_radius:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x + ball_speed <= 800 - ball_radius:
        ball_x += ball_speed

    pygame.display.flip()
    clock.tick(30)
