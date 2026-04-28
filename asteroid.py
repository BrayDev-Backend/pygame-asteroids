from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        ranodm_angle = random.uniform(20, 50)
        first_vector_change = self.velocity.rotate(ranodm_angle)
        second_vector_change = self.velocity.rotate(-ranodm_angle)
        self.radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position, self.position, self.radius)
        asteroid2 = Asteroid(self.position, self.position, self.radius)
        asteroid1.velocity = first_vector_change * 1.2
        asteroid2.velocity = second_vector_change * 1.2
