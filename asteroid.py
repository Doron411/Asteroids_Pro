import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.position = pygame.Vector2(x, y)

        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius, 2)

        self.velocity = pygame.Vector2(50, 30)


    def update(self, dt):
        self.position += self.velocity * dt 
        self.rect.center = (self.position.x, self.position.y)

        print(f"Asteroid updated to x={self.position.x}, y={self.position.y}, rect center={self.rect.center}")