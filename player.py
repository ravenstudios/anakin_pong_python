import pygame
from constants import *

class Player():
    def __init__(self):

        self.x = 0
        self.y = 0
        self.width = BLOCK_SIZE // 2
        self.height = BLOCK_SIZE * 4
        self.y_speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.topleft = (self.x, self.y)


    def update(self):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_UP]:
            self.rect.y -= self.y_speed

        if keys[pygame.K_DOWN]:
            self.rect.y += self.y_speed

        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y + self.height > GAME_HEIGHT:
            self.rect.y = GAME_HEIGHT - self.height

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)
