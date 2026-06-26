import pygame           #Pygame is a cross platform set of python modules. Used to run a game loop and handle events, graphics, and sound.
import constants            #constants.py is a module that contains constant values used throughout the game, such as screen dimensions and other configuration settings.
from logger import log_state            #logger.py is a module that handles logging game state and events to JSONL files.


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()



if __name__ == "__main__":
    main()
