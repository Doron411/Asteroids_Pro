
from constants import PLAYER_RADIUS
import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(self.containers)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

    def draw(self, screen):
        color = (255, 0, 0)
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

        self.rect.center = (int(self.position.x), int(self.position.y))