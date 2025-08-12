
import pygame
from constants import *  # Import screen dimensions and other constants from a separate file
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
# Main function to run the game
def main():
    # Initialize all imported pygame modules
    pygame.init()
    # Create the main display surface with the specified width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create a Clock object to manage fps and calculate delta time
    clock = pygame.time.Clock()
    # Create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Create a Player and assign to groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Player.containers = [updatables, drawables]
    updatables.add(player)
    drawables.add(player)
    Shot.containers = [shots, updatables, drawables]
    
    # Set static containers for Asteroid class
    Asteroid.containers = (asteroids, updatables, drawables)

    # Create asteroid instances
    asteroid1 = Asteroid(100, 100, 30)
    asteroid2 = Asteroid(300, 200, 40)

    # Set static containers for AsteroidField (only updatable)
    AsteroidField.containers = [updatables]

    # Create an AsteroidField instance
    asteroid_field = AsteroidField()
    
    # Delta time in seconds — used to make movement frame-rate independent
    dt = 0 
 
    # Main game loop — runs until the user quits
    while True:
        # Event handling loop — checks for user interactions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop and end the program if window is closed
        # Clear the screen by filling it with black (RGB: 0, 0, 0)
        screen.fill("black")
        # Update all updatable objects
        for obj in updatables:
            obj.update(dt)
        # Check to see if the player or asteroids have collided with each other
        for asteroid in list(asteroids):  # Use list() to safely modify group during iteration
            # Check for collisions between shots and asteroids
            for shot in list(shots):  # Use list() to safely modify group during iteration
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split() # This handles both killing and spawning new asteroids
            if player.collides_with(asteroid): # Exit game if player collides with an asteroid
                print("Game over!")
                pygame.quit()
                sys.exit()
        # Draw all drawable objects
        for obj in drawables:
            obj.draw(screen)
        # Update the full display surface to the screen
        pygame.display.flip()
        # Pause the loop to maintain 60 FPS and calculate time since last frame
        # .tick(60) returns milliseconds, so divide by 1000 to get seconds
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
