#--main.py--
#if it doesnt work, go to terminal and type pip uninstall pygame then pip install pygame-ce
# notes
# video 10:28:58
# next step: adding health bars and attack animations
#
#
#


import pygame
from settings import *
from support import *
from timer import Timer
from enemy import Player, Enemy
from ui import UI

class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.screen = pygame.display.set_mode((window_width,window_height))
        pygame.display.set_caption('Tester Battle')
        self.clock = pygame.time.Clock()
        self.running = True
        self.import_assets()
        self.player_active=True
        # groups
        self.all_sprites = pygame.sprite.Group()

        # data
        player_list=['anqi', 'kami', 'saee', 'twinkles', 'shaili', 'charlie'] # max 4
        self.player_chars=[Player(name, self.back_surfs[name]) for name in player_list]
        self.player=self.player_chars[0]
        self.all_sprites.add(self.player)
        enemy_name='shaili'
        #enemy_name=choice(list(enemy_data.keys())) # random choice, can put any enemy
        self.enemy=Enemy(enemy_name, self.front_surfs[enemy_name], self.all_sprites)

        # ui
        self.ui=UI(self.player, self.player_chars, self.simple_surfs, self.get_input)

        # timers
        self.timers={'player end':Timer(2000, func=self.enemy_turn), 'enemy end':Timer(1000, func=self.player_turn)}


    def get_input(self, state, data=None):
        if state=='attack':
            self.apply_attack(self.enemy, data)

        elif state=='escape':
            self.running=False
        self.player_active=False
        self.timers['player end'].activate()

    def apply_attack(self, target, attack):
        attack_data=abilities_data[attack]
        # element multiplier
        attack_multiplier=element_data[attack_data['element']][target.element]
        target.health-=attack_data['damage']*attack_multiplier
        print(f'{attack} {target.health}/{target.max_health}')

    def enemy_turn(self):
        attack=choice(self.enemy.abilities)
        self.apply_attack(self.player, attack)
        self.timers['enemy end'].activate()

    def player_turn(self):
        self.player_active=True

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def import_assets(self):
        self.back_surfs=folder_importer('..', 'images', 'back')
        self.front_surfs=folder_importer('..', 'images', 'front')
        self.bg_surfs=folder_importer('..', 'images', 'other')
        self.simple_surfs=folder_importer('..', 'images', 'simple')

    def draw_sprite_shadow(self):
        for sprite in self.all_sprites:
            shadow_rect = self.bg_surfs['shadow'].get_rect(center=sprite.rect.midbottom+pygame.Vector2(0,-10))
            self.screen.blit(self.bg_surfs['shadow'], shadow_rect)

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000 # 60 fps cap

            # event loop 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.update_timers()
            self.all_sprites.update(dt)
            if self.player_active:
                self.ui.update()

            # draw
            self.screen.blit(self.bg_surfs['bg'], (0,0))
            self.draw_sprite_shadow()
            self.all_sprites.draw(self.screen)
            self.ui.draw()
            pygame.display.update()

        pygame.quit()

        
if __name__ == '__main__':
    game = Game()
    game.run()


