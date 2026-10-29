import pygame

CHARACTER_WIDTH = 35
CHARACTER_HEIGHT = 64

class Player:

    def __init__(self, screen_width, screen_height):

        img_front = pygame.image.load("Bilder/test_front.png").convert_alpha()
        img_back = pygame.image.load("Bilder/test_back.png").convert_alpha()
        img_left = pygame.image.load("Bilder/test_left.png").convert_alpha()
        img_right = pygame.image.load("Bilder/test_right.png").convert_alpha()

 
        self.sprites = {
            "down": pygame.transform.scale(img_front, (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
            "up": pygame.transform.scale(img_back, (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
            "left": pygame.transform.scale(img_left, (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
            "right": pygame.transform.scale(img_right, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
        }


        self.direction = "down"

        
        self.rect = self.image.get_rect(topleft=(400, 400))
        
        self.speed = 5
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        keys = pygame.key.get_pressed()



        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.direction = "up"

        if keys[pygame.K_s]:
            self.rect.y += self.speed
            self.direction = "down"

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.direction = "left"     

        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direction = "right"

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height

        self.image = self.sprites[self.direction]

    pass
