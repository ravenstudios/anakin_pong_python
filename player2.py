import pygame
from constants import *
import player

class Player2(player.Player):
    def __init__(self):
        super().__init__()

        self.rect.x = GAME_WIDTH - BLOCK_SIZE // 2
        self.rect.y = 0


    def update(self, ball):
        self.y = ball.y
