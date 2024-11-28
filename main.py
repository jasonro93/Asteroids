import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
import sys


def main():
    pygame.init() # Initializes pygame
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets display size and assigns shorthand variable

    clock = pygame.time.Clock() # Assigns shorthand variable for Clock methods
    dt = 0 # 

    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable, )
    Asteroid.containers = (asteroids, updatable, drawables)
    Player.containers = (updatable, drawables)
    Shot.containers = (shots, updatable, drawables)

    playerx = SCREEN_WIDTH / 2
    playery = SCREEN_HEIGHT / 2
    player = Player(playerx, playery)
    shot = Shot(player.position.x, player.position.y, PLAYER_SHOOT_SPEED)
    asteroids_init = AsteroidField()

    while True: # Initiate infinite game loop
        for event in pygame.event.get(): # X button in game window interrupts loop and closes game
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0)) # Sets screen background to black

        updatable.update(dt) # Update player position based on last time

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()

            for shot in shots:
                if shot.is_colliding(asteroid):
                    pygame.sprite.Sprite.kill(asteroid)
                    pygame.sprite.Sprite.kill(shot)

        for drawable in drawables:
            drawable.draw(screen) # Renders player model
        pygame.display.flip()

        dt = clock.tick(60) / 1000 # Saves time state


if __name__ == "__main__":
    main()