# ==========================================
# Title:  2048 GAME
# Author: Olamide V.O
# Date:   10 Jan 2021
# ==========================================

import sys
import random

import pygame

from game import Game
from box import Box
from grid import Grid
from movement import Movement
from content import Content
from stack import *

# 2048
# constants
COLOR = {'GRID_PRI': (220, 254, 220),
         'GRID_SEC': (146, 169, 146),
         'TXT_SEC': (48, 56, 48),
         'TXT_PRI': (48, 48, 56)}



game = Game()
content = Content()
grid = Grid()
box = Box()

while 1:

    Game.clock.tick(60)
    game.run()
    content.run()
    grid.run()
    box.run()

    pygame.display.flip()
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            Box.move(event.key)

        if event.type == pygame.QUIT:
            pygame.quit()
