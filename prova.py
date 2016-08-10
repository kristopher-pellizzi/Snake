#! /usr/bin/env python
#Snake Game
#Written by Kristopher Pellizzi

import sys,time,random,pygame
from pygame.locals import *

pygame.init()
playSurface=pygame.display.set_mode((640,480))
fpsClock=pygame.time.Clock()
img=pygame.image.load('snake_0.tiff').convert()
img=pygame.transform.scale(img,(640,480))
while True:
	playSurface.fill((255,255,255))
	playRect=img.get_rect()
	playSurface.blit(img,[0,0])
	pygame.display.flip()
	fpsClock.tick(60)