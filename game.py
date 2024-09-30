import pygame 
import sys 


pygame.init()


WIDTH, HEIGHT = 800, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-понг")

# Создание объектов
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 20)
paddle1 = pygame.Rect(30, HEIGHT // 2 - 70, 10, 140)
paddle2 = pygame.Rect(WIDTH - 40, HEIGHT // 2 - 70, 10, 140)


# Начальные скорости
BALL_SPEED_X, BALL_SPEED_Y = 7, 7
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y
PADDLE_SPEED = 10

while True:
    # Выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Управление ракетками
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += PADDLE_SPEED

    # Движение мяча
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Отскок мяча от стен
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x = -ball_speed_x