import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Blocks")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

player_width = 100
player_height = 20
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 7

block_width = 50
block_height = 50
block_speed = 3
block_list = []

score = 0
font = pygame.font.SysFont(None, 35)

clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, [x, y, player_width, player_height])

def draw_block(block):
    pygame.draw.rect(screen, RED, [block[0], block[1], block[2], block[3]])

def display_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, [10, 10])

def detect_collision(player_rect, block_rect):
    return player_rect.colliderect(block_rect)

def game_loop():
    global player_x, score
    game_over = False
    for i in range(5):
        block_x = random.randint(0, SCREEN_WIDTH - block_width)
        block_y = random.randint(-100, -40)
        block_list.append([block_x, block_y, block_width, block_height])
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if player_x < 0:
            player_x = 0
        if player_x > SCREEN_WIDTH - player_width:
            player_x = SCREEN_WIDTH - player_width
        for block in block_list:
            block[1] += block_speed  
            player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
            block_rect = pygame.Rect(block[0], block[1], block[2], block[3])

            if detect_collision(player_rect, block_rect):
                block[1] = random.randint(-100, -40)
                block[0] = random.randint(0, SCREEN_WIDTH - block_width)
                score += 1
            elif block[1] > SCREEN_HEIGHT:
                block[1] = random.randint(-100, -40)
                block[0] = random.randint(0, SCREEN_WIDTH - block_width)

        screen.fill(BLACK)

        draw_player(player_x, player_y)

        for block in block_list:
            draw_block(block)

        display_score(score)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

game_loop()
