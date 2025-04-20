
import pygame
from player import Player
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Player.containers = (updatable)
Asteroid.containers = (asteroids, updatable, drawable)
 

def main():
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")

        asteroid = Asteroid(100, 200, 30)
        print(f"Asteroid created at x={asteroid.position.x}, y={asteroid.position.y}, radius={30}")
        print(f"Asteroid in drawable: {asteroid in drawable}")
        print(f"Asteroid in updatable: {asteroid in updatable}")

        player = Player(SCREEN_WIDTH, SCREEN_HEIGHT, scale=2.0)
        print(f"DEBUG: Player created at x={SCREEN_WIDTH // 2}, y={SCREEN_HEIGHT // 2}")

        running = True
        while running:
            dt = clock.tick(60) / 1000

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

            updatable.update(dt)
            screen.fill((0, 0, 0)) 

            player.draw(screen)
            drawable.draw(screen)

            for sprite in drawable:
                sprite.draw(screen)

            pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()

