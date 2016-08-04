#!/usr/bin/env/ python
#Snake Game
#Written By Kristopher Pellizzi

import pygame, sys, time, random
from pygame.locals import *
import snake_menu

fh=open('.lvl_chosen.txt','w')
fh.write('0')
fh.close()
snake_menu.menu()