import pygame
from constants import *
from player import Player


def main():
    pygame.init() # Initializes pygame
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets display size and assigns shorthand variable

    clock = pygame.time.Clock() # Assigns shorthand variable for Clock methods
    dt = 0 # 
    playerx = SCREEN_WIDTH / 2
    playery = SCREEN_HEIGHT / 2
    player = Player(playerx, playery)

    while True: # Initiate infinite game loop
        for event in pygame.event.get(): # X button in game window interrupts loop and closes game
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0)) # Sets screen background to black

        player.update(dt) # Update player position based on last time

        player.draw(screen) # Renders player model
        pygame.display.flip()

        dt = clock.tick(60) / 1000 # Saves time state


if __name__ == "__main__":
    main()