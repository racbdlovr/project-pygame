import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # in degrees

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    



    
''' Save this for later 
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = self.speed
        else:
            self.velocity.x = 0

        if keys[pygame.K_UP]:
            self.velocity.y = -self.speed
        elif keys[pygame.K_DOWN]:
            self.velocity.y = self.speed
        else:
            self.velocity.y = 0

        # Update position based on velocity and delta time
        self.position += self.velocity * dt

        # Keep player within screen bounds
        if self.position.x < self.radius:
            self.position.x = self.radius
        elif self.position.x > SCREEN_WIDTH - self.radius:
            self.position.x = SCREEN_WIDTH - self.radius

        if self.position.y < self.radius:
            self.position.y = self.radius
        elif self.position.y > SCREEN_HEIGHT - self.radius:
            self.position.y = SCREEN_HEIGHT - self.radius
            '''