import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS




class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        print(f"Shot fired at: ({self.position.x}, {self.position.y})")
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            SHOT_RADIUS,
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt