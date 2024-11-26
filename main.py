import pygame
from constants import *
import ball

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

ball_obj = ball.Ball()
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

    pygame.display.flip()


def update():
    ball_obj.update()


if __name__ == "__main__":
    main()
