import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for upd in updatable:
            upd.update(dt)

        for ast in asteroids:
            if ast.collides_with(player):
                print ("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(ast):
                    shot.kill()
                    ast.kill()


        screen.fill("black")
        
        for dra in drawable:
            dra.draw(screen)


        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
