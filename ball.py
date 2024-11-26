import pygame
from constants import *

class Ball():
    def __init__(self):
        self.rad = BLOCK_SIZE // 2
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT // 2
        self.x_speed = 5
        self.y_speed = 5

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed

        if self.x + self.rad >= GAME_WIDTH or self.x - self.rad < 0:
            self.x_speed = -self.x_speed

        if self.y + self.rad >= GAME_HEIGHT or self.y - self.rad < 0:
            self.y_speed = -self.y_speed


    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (self.x, self.y), self.rad)
