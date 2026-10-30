import pygame

from player import Player

SCREEN_SIZE = (800, 600)
FPS = 60
MAX_DT = 0.05  

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("Mein Spiel")
    clock = pygame.time.Clock()

    player = Player()

    running = True
    while running:

        dt = min(clock.tick(FPS) / 1000, MAX_DT)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        player.update(dt, screen.get_rect())


        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()