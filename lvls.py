#! /usr/bin/env python
#Snake Game
#Written by Kristopher Pellizzi

import sys,time,random,pygame
from pygame.locals import *
import snake_gameover, reg_stats

def lvl1(snakePosition,diff,best,newbest,f_content):
	pygame.init()
	whiteColour=(255,255,255)
	playSurface=pygame.display.set_mode((640,480))
	snakeHead=Rect(snakePosition[0],snakePosition[1],20,20)

	x=160
	while x<640:
		supRect=Rect(x,0,20,160)
		infRect=Rect(x,480-160,20,160)
		pygame.draw.rect(playSurface,whiteColour,supRect)
		pygame.draw.rect(playSurface,whiteColour,infRect)
		x+=160
		if snakeHead.collidelist([supRect,infRect])!=-1:
			reg_stats.reg(diff,best,newbest,f_content)
			snake_gameover.GameOver()
	return playSurface