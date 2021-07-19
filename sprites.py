"""
Code By: Brendan Beard
Graphics By: Brendan Beard
Published By: AtlasStudios
"""

import pygame as pg
import sys
import os
pg.init()

TITLE = "World Creator"
WIDTH = 1280
HEIGHT = 700
pg.display.set_caption(TITLE)
DISPLAY = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)

#path = "C:/Program Files (x86)/AtlasCorporations/StrangerThings"
path = "C:/Users/AtlasDisease/Documents/Python Projects/Main Projects/Creator"

Image_Folder = "Images/"
Audio_Folder = "Audio/"
Maps_Folder = "Maps/"

Title_Screen_List = []
Blocks_List = []

Music_List = []
Sound_List = []

##Icon = pg.image.load(os.path.join(Image_Folder, "Icon.png")).convert_alpha()
##pg.display.set_icon(ST_Icon)

scanner = os.scandir(path)

for dir in scanner:
    if dir.is_dir():
        if dir.name != "__pycache__" and dir.name != "WorldCreator" and dir.name != "WorldCreatorInstaller" and dir.name != "Maps" and dir.name != "Files":
            newpath = (path+"/"+dir.name)
            scanner = os.scandir(newpath)
            for folder in scanner:
                if folder.name == "Music":
                    newest_path = (newpath+"/"+folder.name)
                    scanner = os.scandir(newest_path)
                    for file in scanner:
                        Music_List.append(newest_path+"/"+file.name)
                if folder.name == "Sounds":
                    newest_path = (newpath+"/"+folder.name)
                    scanner = os.scandir(newest_path)
                    for file in scanner:
                        Sound_List.append(newest_path+"/"+file.name)
                elif folder.name == "WorldBlocks":
                    newest_path = (newpath+"/"+folder.name)
                    scanner = os.scandir(newest_path)
                    for file in scanner:
                        Blocks_List.append(pg.image.load(newest_path+"/"+file.name).convert_alpha())
                elif folder.name == "Title_Screen":
                    newest_path = (newpath+"/"+folder.name)
                    scanner = os.scandir(newest_path)
                    for file in scanner:
                         Title_Screen_List.append(pg.image.load(newest_path+"/"+file.name).convert_alpha())
scanner.close()

#Doctor_1 = pg.image.load(os.path.join(path, Image_Folder, "Doctor_1.png")).convert_alpha()

All_Sprites = []
