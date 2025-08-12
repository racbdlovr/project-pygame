import pygame
from circleshape import CircleShape  # Base class for circular shapes
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, direction_vector):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = direction_vector

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)