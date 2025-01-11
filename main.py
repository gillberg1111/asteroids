import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():

	print ("Starting asteroids!")
	print (f"Screen width: {SCREEN_WIDTH}")
	print (f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()
	screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable,shots)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots,updatable, drawable)

	player1 = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		pygame.Surface.fill(screen,(0,0,0))

		for asteroid in asteroids:
			if asteroid.detect_collision(player1):
				print(f"Collision detected with asteroid at {asteroid.position}!")
				print("Game over!")
				raise SystemExit
			
		print("Before updates:")
		print("Player in drawable:", player1 in drawable)

		for entity in updatable:
			print(f"Updating {entity}")
			entity.update(dt)

		print("After updates, before drawing:")
		print("Player in drawable:", player1 in drawable)

		for entity in drawable:
			print(f"Drawing {entity}")
			entity.draw(screen)

		print("After drawing:")
		print("Player in drawable:", player1 in drawable)
		
		for shot in shots:
			for asteroid in asteroids:
				if asteroid.detect_collision(shot):
					shot.kill()
					asteroid.split()

		pygame.display.flip()
		dt = clock.tick(60)/1000


if __name__ == "__main__":
	main()