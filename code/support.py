import pygame
from os import walk

def import_folder(path):
    surface_list = []

    for _, _, img_files in walk(path):
        img_files.sort()
        for image in img_files:
            full_path = path + "/" + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)


    return surface_list