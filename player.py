from pathlib import Path

import pygame

CHARACTER_SIZE = (35, 64)
PLAYER_WALKING_SPEED = 250  
IMAGE_DIR = Path(__file__).parent / "Bilder"
PLAYER_RUNNING_SPEED = 500

SPRITE_FILES = {
    "down": "test_front.png",
    "up": "test_back.png",
    "left": "test_left.png",
    "right": "test_right.png",
}


class Player:
    def __init__(self, start_pos=(400, 400)):

        self.sprites = {
            direction: pygame.transform.scale(
                pygame.image.load(IMAGE_DIR / filename).convert_alpha(),
                CHARACTER_SIZE,
            )
            for direction, filename in SPRITE_FILES.items()
        }

        self.direction = "down"
        self.image = self.sprites[self.direction]
        self.speed = PLAYER_WALKING_SPEED

        self.rect = self.image.get_rect(topleft=start_pos)
        self.pos = pygame.Vector2(self.rect.topleft)

    def update(self, dt, bounds):
        keys = pygame.key.get_pressed()


        move = pygame.Vector2(0, 0)

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.speed = PLAYER_RUNNING_SPEED
        else:
            self.speed = PLAYER_WALKING_SPEED
        # for debugging, use stuf flike: print(self.speed)

        
        if keys[pygame.K_w]:
            move.y -= 1
            self.direction = "up"
        if keys[pygame.K_s]:
            move.y += 1
            self.direction = "down"
        if keys[pygame.K_a]:
            move.x -= 1
            self.direction = "left"
        if keys[pygame.K_d]:
            move.x += 1
            self.direction = "right"



        if move.length_squared() > 0:
            move.normalize_ip()
            self.pos += move * self.speed * dt


        self.pos.x = max(bounds.left, min(self.pos.x, bounds.right - self.rect.width))
        self.pos.y = max(bounds.top, min(self.pos.y, bounds.bottom - self.rect.height))


        self.rect.topleft = self.pos
        self.image = self.sprites[self.direction]

    def draw(self, surface):
        surface.blit(self.image, self.rect)