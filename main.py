import pygame
from constants import *
import ball
import player, player2
clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

ball_obj = ball.Ball()
player_obj = player.Player()
player2_obj = player2.Player2()



def main():
    running = True

    while running:
        clock.tick(TICK_RATE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        update()
        draw()
    pygame.quit()


def draw():
    surface.fill(BLACK)

    ball_obj.draw(surface)
    player_obj.draw(surface)
    player2_obj.draw(surface)
    pygame.display.flip()


def update():
    ball_obj.update()
    player_obj.update()
    player2_obj.update(ball_obj)

if __name__ == "__main__":
    main()
