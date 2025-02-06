import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()
    print("Starting asteroids!")
    # FPS
    clock = pygame.time.Clock()
    dt = 0
    # Create the two groups for simple update and drawing
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

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
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
