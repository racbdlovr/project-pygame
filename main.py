
import pygame
from constants import *  # Import screen dimensions and other constants from a separate file
from player import Player

def main():
    # Initialize all imported pygame modules
    pygame.init()
    # Create the main display surface with the specified width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create a Clock object to manage frame rate and calculate delta time
    clock = pygame.time.Clock()
    # Create a Player object at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Delta time in seconds — used to make movement frame-rate independent
    dt = 0 

    # Debugging output to confirm game startup and screen dimensions
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}") 
    # Main game loop — runs until the user quits
    while True:
        # Event handling loop — checks for user interactions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop and end the program
        # Clear the screen by filling it with black (RGB: 0, 0, 0)
        screen.fill("black") 
        # Draw the player each frame
        player.draw(screen)

        # Update the full display surface to the screen
        pygame.display.flip()
        # Pause the loop to maintain 60 FPS and calculate time since last frame
        # .tick(60) returns milliseconds, so divide by 1000 to get seconds
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    # Run the main function only if this script is executed directly
    main()
