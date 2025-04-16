import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__(self.containers)
        self.position = pygame.Vector2(screen_width // 2, screen_height // 2)
        self.rotation = 0
        self.radius = 20
        self.speed = 0
        self.velocity = pygame.Vector2(0, 0)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 120) * self.radius / 1.5
        left = pygame.Vector2(0, 1).rotate(self.rotation - 120) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - right
        c = self.position - left

        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", [(p.x, p.y) for p in points], 2)

    def rotate(self, clockwise, dt):
        rotation_speed = 200
        if clockwise:
            self.rotation += rotation_speed * dt
        else:
            self.rotation -= rotation_speed * dt

        self.rotation %= 360
        

    def update(self, dt):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_d]: 
            self.rotate(clockwise=True, dt=dt)
        if keys[pygame.K_a]:
            self

    



    