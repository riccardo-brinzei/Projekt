import pygame
from sys import exit
from player import Player

def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600



    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Mein Spiel")
    my_player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)



    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        my_player.update()



        screen.fill("black")
        screen.blit(my_player.image, my_player.rect)
        pygame.display.update()  
        clock.tick(60)

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()

