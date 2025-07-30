import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2

        player1 = Player(x, y)
        player1.draw(screen)

        pygame.display.flip()


        #limit the framerate
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
