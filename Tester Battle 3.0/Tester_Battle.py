#--main.py--

from settings import *
from support import *
from timer import kill_timer

class Game:
    def __init__(self):
        #setup
        pygame.init()
        self.screen = pygame.display.set_mode((window_width,window_height))
        pygame.display.set_caption('Tester Battle')
        self.clock = pygame.time.Clock()
        self.running = True

        #groups
        self.all_sprites = pygame.sprite.Group()

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000 #60 fps cap
            #event loop 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            #update
            self.all_sprites.update(dt)
            #draw
            self.screen.fill(pink)
            self.all_sprites.draw(self.screen)
            pygame.display.update()

        pygame.quit()

        
if __name__ == '__main__':
    game = Game()
    game.run()


