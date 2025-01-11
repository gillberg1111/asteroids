import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius,velocity):
        super().__init__(x,y,radius)
        self.velocity = velocity


    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        Asteroid.kill(self)
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        velocity = pygame.Vector2(self.velocity)
        
        new_velocity1 = velocity.rotate(random_angle)*1.2
        new_velocity2 = velocity.rotate(-random_angle)*1.2
        offset1 = pygame.Vector2(random.uniform(-10, 10))
        offset2 = pygame.Vector2(random.uniform(-10, 10))
        new_position1 = pygame.Vector2(self.position.x, self.position.y) + offset1
        new_position2 = pygame.Vector2(self.position.x, self.position.y) + offset2
        new_asteroid1 = Asteroid(new_position1,new_position2,(self.radius - ASTEROID_MIN_RADIUS),new_velocity1)
        new_asteroid2 = Asteroid(new_position1,new_position2,(self.radius - ASTEROID_MIN_RADIUS),new_velocity2)
