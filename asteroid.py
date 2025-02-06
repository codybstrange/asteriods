from constants import *
from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)



    def update(self, dt):
        self.position += dt*self.velocity

    def draw(self, screen):
        line_width = 2
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=line_width)
