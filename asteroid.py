import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    containers = []  # Will be set in main.py
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        for group in Asteroid.containers:
            group.add(self)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt