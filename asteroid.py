import pygame
import circleshape
import random
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # Immediately kill itself (this asteroid is always destroyed)
        self.kill()
        
        # If the radius is less than or equal to ASTEROID_MIN_RADIUS, just return
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        
        # Create 2 new velocity vectors by rotating the current velocity
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        
        # Compute the new radius using the formula: old_radius - ASTEROID_MIN_RADIUS
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new Asteroid objects at the current position with new radius
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # Set velocities and make them move faster by scaling up by 1.2
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2 

