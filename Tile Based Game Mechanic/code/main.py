import pygame, sys
from settings import *
from body import Body
from debug import debug

class Game :
    def __init__(self):

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Pixel RPG')
        self.clock = pygame.time.Clock()

        self.body = Body()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.body.run()
            debug('beta 1.00', 700, 0)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()