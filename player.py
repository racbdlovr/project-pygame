import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
# Player class inherits from CircleShape
# Represents the player in the game
# It has a position, velocity, radius, and rotation
# It can draw itself as a triangle and move or rotate based on user input
# It can also shoot shots
# The player is a circular shape with a defined radius

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # in degrees
        self.shoot_timer = 0  # Timer starts at 0
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
# in the player class
    def triangle(self): # Returns the vertices of the triangle representing the player
        # Calculate the three points of the triangle based on the player's position and rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt): # Rotate the player based on the turn speed and delta time
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt): # Update the player based on user input
        keys = pygame.key.get_pressed()
        # Update shoot timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        # Handle player input for movement and shooting
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        # Only shoot if cooldown has expired
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            return self.shoot()  # Return the shot so it can be added to the game

    def move(self, dt): # Move the player forward or backward based on the current rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        # Keep player within screen bounds
        if self.position.x < self.radius:
            self.position.x = self.radius
        elif self.position.x > SCREEN_WIDTH - self.radius:
            self.position.x = SCREEN_WIDTH - self.radius
        if self.position.y < self.radius:
            self.position.y = self.radius
        elif self.position.y > SCREEN_HEIGHT - self.radius:
            self.position.y = SCREEN_HEIGHT - self.radius
    
    def shoot(self): # Create a shot in the direction the player is facing
        # Calculate the shot's position and velocity based on the player's position and rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_velocity = forward * PLAYER_SHOOT_SPEED
        shot_position = self.position + forward * self.radius
        return Shot(shot_position.x, shot_position.y, shot_velocity)



