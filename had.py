import pygame
import random

pygame.init()

s_width = 800
s_height = 600
screen = pygame.display.set_mode((s_width, s_height))

clock = pygame.time.Clock()

running = True

player_surf = pygame.image.load("smiley.png").convert_alpha()
player_surf = pygame.transform.scale(player_surf, (100, 100))
player_x = 150
player_y = 150

player_rect = player_surf.get_rect(midbottom=(player_x, player_y))
player_speed = 6

coin_surf = pygame.image.load("gem.png").convert_alpha()
coin_surf = pygame.transform.scale(coin_surf, (50, 50))  

coin_rect = coin_surf.get_rect(center=(random.randint(50, s_width - 50), random.randint(50, s_height - 50)))

green_coin_surf = pygame.image.load("green_coin.png").convert_alpha()
green_coin_surf = pygame.transform.scale(green_coin_surf, (50, 50))

green_coin = None  
green_coin_timer = 0 
green_coin_spawn_time = 0
score = 0
font = pygame.font.Font("Barriecito-Regular.ttf", 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player_rect.top -= player_speed
    if key[pygame.K_a]:
        player_rect.left -= player_speed
    if key[pygame.K_s]:
        player_rect.bottom += player_speed
    if key[pygame.K_d]:
        player_rect.right += player_speed

    if player_rect.colliderect(coin_rect):
        score += 10
        coin_rect.x = random.randint(50, s_width - 50)
        coin_rect.y = random.randint(50, s_height - 50)

    if green_coin and player_rect.colliderect(green_coin):
        score += 100
        green_coin = None

    if green_coin:
        if pygame.time.get_ticks() - green_coin_spawn_time >= 2000:
            green_coin = None
    else:
        green_coin_timer += 1
        if green_coin_timer >= 180:
            green_coin = green_coin_surf.get_rect(topleft=(random.randint(50, s_width - 50), random.randint(50, s_height - 50)))
            green_coin_spawn_time = pygame.time.get_ticks()  
            green_coin_timer = 0

    screen.fill("pink")
    screen.blit(player_surf, player_rect)
    screen.blit(coin_surf, coin_rect)

    if green_coin:
        screen.blit(green_coin_surf, green_coin)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
