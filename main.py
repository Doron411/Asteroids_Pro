import pygame
from player import Player
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()


Player.containers = (updatable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)

def main():
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")

        asteroid = Asteroid(100, 200, 30)

        player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
        print(f"DEBUG: Player created at x={SCREEN_WIDTH // 2}, y={SCREEN_HEIGHT // 2}")

        asteroid_field = AsteroidField()
        print("DEBUG: Asteroid field initialized successfully")
        print("(DEBUG) Current contents of updatable group:")
        for sprite in updatable:
            print(f" - {type(sprite).__name__}")
                
        running = True
        while running:
            dt = clock.tick(60) / 1000

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

            updatable.update(dt)
            print("(DEBUG) Checking which updatable sprites exist:")
            for sprite in updatable:
                print(f" - {type(sprite).__name__}")

            print("(DEBUG) Updatable.update() called")
            screen.fill((0, 0, 0)) 

            for sprite in drawable:
                sprite.draw(screen)
                                                

            pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()

