import pygame
import sys
from pygame.locals import QUIT

pygame.init()
Surface = pygame.display.set_mode((400,800))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("Test Window")

def main():
    while True:
        Surface.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()