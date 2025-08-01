from constants import *
import pygame
import circleshape
from shot import Shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
        self.space_pressed = False

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        # Update shoot cooldown timer
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt) 
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        
        # Handle shooting with single press detection
        if keys[pygame.K_SPACE]:
            if not self.space_pressed:  # Only shoot on first press
                self.shoot()
                self.space_pressed = True
        else:
            self.space_pressed = False  # Reset when key is released

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Check if cooldown has expired
        if self.shoot_cooldown <= 0:
            # Calculate the tip of the player's triangle
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            tip_position = self.position + forward * self.radius
            shot = Shot(tip_position.x, tip_position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED 
            # Reset cooldown timer
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
