import sys

import pygame           #Pygame is a cross platform set of python modules. Used to run a game loop and handle events, graphics, and sound.
import constants            #constants.py is a module that contains constant values used throughout the game, such as screen dimensions and other configuration settings.
from logger import log_state, log_event            #logger.py is a module that handles logging game state and events to JSONL files.
from player import Player            #player.py is a module that defines the Player class, which represents the player character in the game.
from asteroid import Asteroid            #asteroid.py is a module that defines the Asteroid class, which represents the asteroids in the game.
from asteroidfield import AsteroidField
from shot import Shot            #asteroidfield.py is a module that defines the AsteroidField class, which manages the spawning of asteroids.

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()          #Used to manage FPS (frames per second) and control the game loop timing.
    dt = 0.0          #dt is a variable that represents the time delta between frames, used for smooth movement and animation.
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()          #updatable is a sprite group that will contain all game objects that need to be updated.
    drawable = pygame.sprite.Group()          #drawable is a sprite group that will contain all game objects that need to be drawn.
    Player.containers = updatable, drawable          #The player object is added to both the
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)        #The player object is created at the center of the screen.
    asteroids = pygame.sprite.Group()          #asteroids is a sprite group that will contain all asteroid objects.
    Asteroid.containers = updatable, drawable, asteroids          #The asteroid object is added to the updatable, drawable, and asteroids groups.
    AsteroidField.containers = updatable          #The asteroid field object is added to the updatable group.
    asteroidfield = AsteroidField()          
    shots = pygame.sprite.Group()          #shots is a sprite group that will contain all shot objects.
    Shot.containers = updatable, drawable, shots          #The shot object is added to the updatable, drawable, and shots groups.
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for objects in asteroids:
            if player.collides_with(objects):
                log_event("player_hit")
                print("Game over!") 
                sys.exit()  # Exit the game if the player collides with an asteroid  
        for objects2 in asteroids:
            for bullet in shots:
                if objects2.collides_with(bullet):
                    log_event("asteroid_shot")
                    objects2.split()
                    bullet.kill()       
        for draw1 in drawable:
            draw1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0       #Convert milliseconds to seconds


if __name__ == "__main__":
    main()
