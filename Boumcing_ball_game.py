import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
BALL_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
SPEED_X = 5
SPEED_Y = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")


ball_x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
ball_y = random.randint(BALL_RADIUS, HEIGHT - BALL_RADIUS)
ball_velocity_x = SPEED_X
ball_velocity_y = SPEED_Y

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    if ball_x <= BALL_RADIUS or ball_x >= WIDTH - BALL_RADIUS:
        ball_velocity_x *= -1
    if ball_y <= BALL_RADIUS or ball_y >= HEIGHT - BALL_RADIUS:
        ball_velocity_y *= -1

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)

    pygame.display.flip()

    pygame.time.delay(30)

pygame.quit()
