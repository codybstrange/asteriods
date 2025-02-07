from constants import *
from circleshape import CircleShape
import pygame
import random as r

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        theta = r.uniform(20, 50)
        v_left = self.velocity.rotate(theta)*BREAKUP_SPEED_GAIN
        v_right = self.velocity.rotate(-theta)*BREAKUP_SPEED_GAIN
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child_left = Asteroid(self.position.x, self.position.y, new_radius)
        child_left.velocity = v_left
        child_right = Asteroid(self.position.x, self.position.y, new_radius)
        child_right.velocity = v_right

    def update(self, dt):
        self.position += dt*self.velocity

    def draw(self, screen):
        line_width = 2
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=line_width)
