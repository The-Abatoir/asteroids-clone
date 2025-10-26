import pygame 
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

'''
Add a scoring system
Implement multiple lives and respawning
Add an explosion effect for the asteroids
Add acceleration to the player movement
Make the objects wrap around the screen instead of disappearing
Add a background image
Create different weapon types
Make the asteroids lumpy instead of perfectly round
Make the ship have a triangular hit box instead of a circular one
Add a shield power-up
Add a speed power-up
Add bombs that can be dropped
'''

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Group declarations
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    roids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Group containers
    Asteroid.containers = (roids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    space = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for entity in updatable:
            entity.update(dt)
        for roid in roids:
            if roid.check_for_collision(player):
                print("Game over!")
                return
            if shots:
                for shot in shots:
                    if roid.check_for_collision(shot):
                        roid.split()
        for entity in drawable:
            entity.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000.0  # Limit to 60 FPS
        


if __name__ == "__main__":
    main()
