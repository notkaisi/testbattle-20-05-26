#--main.py--
#if it doesnt work, go to terminal and type pip uninstall pygame then pip install pygame-ce
# notes
# video 10:28:58
# next step: adding health bars and attack animations

import pygame
from settings import *
from support import *
from timer import Timer
from enemy import *
from ui import *
from attack import AttackAnimationSprite

class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.screen = pygame.display.set_mode((window_width,window_height))
        pygame.display.set_caption('Tester Battle')
        self.clock = pygame.time.Clock()
        self.running = True
        self.import_assets()
        self.audio['music'].play(-1)
        self.player_active=True
        # groups
        self.all_sprites = pygame.sprite.Group()

        # data
        player_list=['anqi', 'kami', 'saee', 'twinkles', 'shaili', 'charlie'] # max 4
        self.player_chars=[Player(name, self.back_surfs[name]) for name in player_list]
        self.player=self.player_chars[0]
        self.all_sprites.add(self.player)
        #enemy_name='shaili' picking one selectively
        enemy_name=choice(list(enemy_data.keys())) # random choice, can put any enemy
        self.enemy=Enemy(enemy_name, self.front_surfs[enemy_name], self.all_sprites)

        # ui
        self.ui=UI(self.player, self.player_chars, self.simple_surfs, self.get_input)
        self.opponent_ui=OpponentUI(self.enemy)

        # timers
        self.timers={'player end':Timer(2000, func=self.enemy_turn), 'enemy end':Timer(1000, func=self.player_turn)}

    def get_input(self, state, data=None):
        if state=='attack':
            self.apply_attack(self.enemy, data)

        elif state=='heal':
            self.player.health+=50
            AttackAnimationSprite(self.player, self.attack_frames['green'], self.all_sprites)
            self.audio['green'].play()

        elif state=='switch':
            self.player.kill()
            self.player=data
            self.all_sprites.add(self.player)
            self.ui.player=self.player

        elif state=='escape':
            self.running=False
        self.player_active=False
        self.timers['player end'].activate()

    def apply_attack(self, target, attack):
        attack_data=abilities_data[attack]
        # element multiplier
        attack_multiplier=element_data[attack_data['element']][target.element]
        target.health-=attack_data['damage']*attack_multiplier
        #print(f'{attack} {target.health}/{target.max_health}')
        AttackAnimationSprite(target, self.attack_frames[attack_data['animation']], self.all_sprites)
        self.audio[attack_data['animation']].play()

    def enemy_turn(self):
        if self.enemy.health<=0:
            self.player_active=True
            self.enemy.kill()
            print('You win!')
            enemy_name=choice(list(enemy_data.keys()))
            self.enemy=Enemy(enemy_name, self.front_surfs[enemy_name], self.all_sprites)
            self.opponent_ui.enemy=self.enemy
        else:
            attack=choice(self.enemy.abilities)
            self.apply_attack(self.player, attack)
            self.timers['enemy end'].activate()

    def player_turn(self):
        self.player_active=True
        #if defeated, next monster
        #if no monsters left, endgame
        if self.player.health<=0:
            available_chars=[player for player in self.player_chars if player.health>0]
            if available_chars:
                self.player.kill()
                self.player=available_chars[0]
                self.all_sprites.add(self.player)
                self.ui.player=self.player
            else:
                self.running=False

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def import_assets(self):
        self.back_surfs=folder_importer('..', 'images', 'back')
        self.front_surfs=folder_importer('..', 'images', 'front')
        self.bg_surfs=folder_importer('..', 'images', 'other')
        self.simple_surfs=folder_importer('..', 'images', 'simple')
        self.attack_frames=tile_importer(4, '..', 'images', 'attacks')
        self.audio=audio_importer('..', 'audio')

    def draw_sprite_shadow(self):
        for sprite in self.all_sprites:
            if isinstance(sprite, Attributes):
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
            self.opponent_ui.draw()
            pygame.display.update()

        pygame.quit()

        
if __name__ == '__main__':
    game = Game()
    game.run()


