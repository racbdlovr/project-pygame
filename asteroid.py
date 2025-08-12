import pygame
from circleshape import CircleShape
from constants import *
import random
# Asteroid class inherits from CircleShape
# Represents an asteroid in the game
# It has a position, velocity, and radius
# It can draw itself as a circle and update its position based on velocity 
# It can also split into smaller asteroids when hit
# The asteroid is a circular shape with a defined radius

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
    
    
    
    def split(self):
        # Always kill the current asteroid
        self.kill()

        # If it's already small, don't split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        
    # Compute new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors rotated in opposite directions
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Create two new asteroids at the same position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2

        # Add them to the appropriate groups
        for group in Asteroid.containers:
            group.add(asteroid1)
            group.add(asteroid2)


