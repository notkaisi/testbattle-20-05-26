#--support.py--
import settings
from os import walk
from os.path import join
import pygame 

def folder_importer(*path):
    surfs={}
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in file_names:
            full_path = join(folder_path, file_name)
            # print('trying: ', full_path)

            try:
                surfs[file_name.split('.')[0]] = pygame.image.load(full_path).convert_alpha()
                # print('success')
            except Exception as e:
                # print('failed: ', file_name)
                print(e)
    return surfs

#audio
def audio_importer(*path):
    audio_dict={}
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in file_names:
            audio_dict[file_name.split('.')[0]] = pygame.mixer.Sound(join(folder_path, file_name))
    return audio_dict