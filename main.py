import pygame
from sys import exit

def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    CHARACTER_WIDTH = 35
    CHARACTER_HEIGHT = 64


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Mein Spiel")


    player_surface = pygame.image.load("Bilder/test_front.png").convert_alpha()
    player_surface = pygame.transform.scale(player_surface, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    player_rect = player_surface.get_rect(topleft=(400, 400))


    player_speed = 5


    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys =pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_rect.y -= player_speed
        if keys[pygame.K_s]:
            player_rect.y += player_speed
        if keys[pygame.K_a]:
            player_rect.x -= player_speed
        if keys[pygame.K_d]:
            player_rect.x += player_speed

        if player_rect.left < 0:
            player_rect.left = 0
        if player_rect.top < 0:
            player_rect.top = 0
        if player_rect.right > SCREEN_WIDTH:
            player_rect.right = SCREEN_WIDTH
        if player_rect.bottom > SCREEN_HEIGHT:
            player_rect.bottom = SCREEN_HEIGHT


        screen.fill("black")
        screen.blit(player_surface, player_rect)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()

