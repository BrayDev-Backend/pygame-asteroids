from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
import pygame
from logger import log_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        delta_time = clock.tick(60)
        dt = delta_time / 1000
        # print(dt)
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
