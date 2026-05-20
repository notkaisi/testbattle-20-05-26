#--settings.py--

import pygame
import os
from os.path import join
from os import walk
import random
from random import choice
print('starting')
print('pygame imported')

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Working directory:", os.getcwd())
(os.path.abspath(__file__))

window_width, window_height = 1280, 720
tile_size=64

colours={
    'black':'#000000',
    'red':'#ee1a0f',
    'gray':'gray',
    'white':'#ffffff',
    }

enemy_data={
    'shaili':{'element':'water', 'health':90},
    'anqi':{'element':'plant', 'health':60},
    'saee':{'element':'fire', 'health':110},
    'twinkles':{'element':'special', 'health':160},
    'kami':{'element':'water', 'health':80},
    'charlie':{'element':'plant','health':100},
    }

abilities_data={
    'scratch':{'damage':20, 'element':'normal', 'animation':'attack'},
    'spark':{'damage':30, 'element':'fire', 'animation':'attack'},
    'nuke':{'damage':50, 'element':'fire', 'animation':'attack'},
    'splash':{'damage':30, 'element':'water', 'animation':'attack'},
    'shards':{'damage':50, 'element':'water', 'animation':'attack'},
    'spiral':{'damage':40, 'element':'plant', 'animation':'attack'},
    }

element_data={
    'fire':{'water':0.5, 'plant':2, 'fire':1, 'normal':1.2},
    'water':{'water':0.5, 'plant':0.5, 'fire':2, 'normal':1},
    'plant':{'water':2, 'plant':1, 'fire':0.5, 'normal':1},
    'normal':{'water':1, 'plant':1, 'fire':1, 'normal':1},
    # can add more :)
    'special':{'water':3, 'plant':3, 'fire':3, 'normal':3},
    
    
    
    
    }