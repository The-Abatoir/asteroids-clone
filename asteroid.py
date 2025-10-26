from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            break_angle = self.velocity.rotate(angle)
            neg_break_angle = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            roid1 = Asteroid(self.position.x, self.position.y, new_radius)
            roid1.velocity = break_angle * 1.2
            roid2 = Asteroid(self.position.x, self.position.y, new_radius)
            roid2.velocity = neg_break_angle * 1.2
