import pygame
from circleshape import *
from constants import *
    
class Shot(CircleShape):
    def __init__(self,position,angle):
        super().__init__(position.x,position.y,SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,1).rotate(angle) * PLAYER_SHOOT_SPEED
        
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt