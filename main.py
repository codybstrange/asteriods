import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    pygame.init()
    print("Starting asteroids!")
    # FPS
    clock = pygame.time.Clock()
    dt = 0
    # Create the groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for obj in drawable:
            obj.draw(screen)
        for obj in updatable:
            obj.update(dt)
        # Collision detection
        for asteroid in asteroids:
            if asteroid.overlaps(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.overlaps(shot):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
