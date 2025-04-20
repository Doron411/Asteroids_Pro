import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, scale=2.0):
        super().__init__(self.containers)
        self.position = pygame.Vector2(screen_width // 2, screen_height // 2)
        self.rotation = 0
        self.radius = PLAYER_RADIUS * scale
        self.speed = PLAYER_SPEED 
        self.velocity = pygame.Vector2(0, 0)

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, -1).rotate(self.rotation + 120) * self.radius / 1.5
        left = pygame.Vector2(0, -1).rotate(self.rotation - 120) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - right
        c = self.position - left

        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", [(p.x, p.y) for p in points], 2)

    def rotate(self, clockwise, dt):
        if clockwise:
            self.rotation += PLAYER_TURN_SPEED * dt
        else:
            self.rotation -= PLAYER_TURN_SPEED * dt

        self.rotation %= 360

    def move_forward(self, dt):
        forward_vector = pygame.Vector2(0, -1).rotate(self.rotation)
        self.velocity += forward_vector * self.speed * dt

    def move_backward(self, dt):
        backward_vector = pygame.Vector2(0, -1).rotate(self.rotation)
        self.velocity -= backward_vector * self.speed * dt
        

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d]:
            self.rotate(clockwise=True, dt=dt)
        if keys[pygame.K_a]:
            self.rotate(clockwise=False, dt=dt)
        if keys[pygame.K_w]:
            self.move_forward(dt)
        if keys[pygame.K_s]:
            self.move_backward(dt)

        self.position += self.velocity * dt

        self.velocity *= 0.99

        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
