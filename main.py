import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1000, 1000), pygame.RESIZABLE)
pygame.display.set_caption("RPG Projekt")

clock = pygame.time.Clock()

background_surface = pygame.image.load("Bilder/test_room.png").convert()
player_surface = pygame.image.load("Bilder/test_front.png").convert_alpha()

player_x = 400
player_y = 400


player_speed = 5 



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # --- NEU: Bewegungslogik ---
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]: # Nach oben
        player_y -= player_speed
    if keys[pygame.K_s]: # Nach unten
        player_y += player_speed
    if keys[pygame.K_a]: # Nach links
        player_x -= player_speed
    if keys[pygame.K_d]: # Nach rechts
        player_x += player_speed
    # ---------------------------

    screen.blit(background_surface, (0, 0))
    screen.blit(player_surface, (player_x, player_y))

    pygame.display.update()
    clock.tick(60)