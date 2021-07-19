"""
Programmed By: Brendan Beard
Graphics By: Brendan Beard
Published By: AtlasStudios
"""
# --- Imports --- #

import pygame as pg
import sys
import os
pg.init()

# --- Constants --- #

SKYBLUE = (140, 255, 251)

TITLE = "WorldCreator"
pg.display.set_caption(TITLE)
ICON = pg.transform.scale2x(pg.image.load("./Images/WorldBlocks/CobblestoneBlock.png"))
pg.display.set_icon(ICON)
Game = True

# --- Classes --- #

class World:
    def __init__(self, file):
        self.filename = file
        self.map = self.create_world()
        self.bg = self.map
        self.bg.fill(SKYBLUE)

    def load_world(self):
        file = open(self.filename)
        data = file.read().splitlines()
        self.array = data
        List = []
        for lines in data:
            List.append(list(lines))
        return List

    def create_world(self):
        self.world = self.load_world()
        self.converter = Converter("Normal")
        self.Blocks_List = []
        x = 0
        y = 0
        for lists in self.world:
            x = 0
            for symbol in lists:
                block = self.converter.get_block(symbol, (x*16, y*16))
                self.Blocks_List.append(block)
                x += 1
            y += 1
        return pg.Surface((x*16, y*16))

class Converter:
    def __init__(self, type):
        self.type = type
        if self.type == "Normal":
            self.filename = "./Maps/WorldCreatorDecoders/NormalCharacterDecoder.txt"
        elif self.type == "Scientific":
            self.filename = "./Maps/WorldCreatorDecoders/ScientificCharacterDecoder.txt"
        self.dict = self.create_dict()

    def create_dict(self):
        List = []
        file = open(self.filename)
        data = file.read().splitlines()
        for string in data:
            tuple = (string[0], string[4:])
            List.append(tuple)
        file.close()
        return dict(List)
            
    def get_block(self, symbol, cord):
        name = self.dict.get(symbol)
        block = Blocks([name, cord, str(name)+"Block.png"])
        return block

            
class Blocks:
    def __init__(self, list):
        if list[0] == None:
            self.name = "PinkSky"
            self.x = int(list[1][0])
            self.y = int(list[1][1])
            self.image = pg.image.load("./Images/WorldBlocks/"+"PinkSky.png").convert_alpha()
        else:
            self.name = list[0]
            self.x = int(list[1][0])
            self.y = int(list[1][1])
            self.image = pg.image.load("./Images/WorldBlocks/"+list[2]).convert_alpha()

NonUsable = "Non-UsableWorlds/"
String = "StringWorlds/"
File = input("Seed: ")+".udb"
DISPLAY = pg.display.set_mode((1280,700), pg.RESIZABLE)
##try:
world = World("C:/Users/AtlasDisease/Documents/Python Projects/Main Projects/Creator/Maps/WorldCreatorWorlds/"+File)
##except:
##    world = World("C:/Users/AtlasDisease/Documents/Python Projects/Main Projects/Creator/Maps/WorldCreatorWorlds/Flat.udb")

while Game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Game = False
    for blocks in world.Blocks_List:
        world.map.blit(blocks.image, (blocks.x, blocks.y))
    DISPLAY.blit(world.map, (0,0))
    pg.display.update()

pg.quit()    
sys.exit(0)
