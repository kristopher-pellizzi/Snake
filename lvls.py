#! /usr/bin/env python
#Snake Game
#Written by Kristopher Pellizzi

import sys,time,random,pygame
from pygame.locals import *
import snake_gameover, reg_stats

def lvl1():
	rectList=[]

	x=160
	while x<640:
		supRect=Rect(x,0,20,160)
		infRect=Rect(x,480-160,20,160)
		rectList=rectList+[supRect,infRect]
		x+=160
	return rectList

def lvl2():
	rectList=[]

	x=160
	i=0
	while x<640:
		lvlRect=Rect(x,i,20,340)
		if i==0:
			i=480-200
		else:
			i=0
		rectList=rectList+[lvlRect]	
		x+=160
	return rectList

def lvl3():
	rectList=[]

	x=100
	y=100
	rectList=rectList+[Rect(x,y,440,20),Rect(x,480-y,440,20),Rect(x,y+20,20,100),Rect(x,480-y-100,20,100),Rect(620-x,y+20,20,100),Rect(620-x,480-y-100,20,100)]
	return rectList

def lvl4():
	rectList=[]

	x=100
	y=100
	lenght=180
	height=260
	closeHeight=80
	rectList=rectList+[Rect(x,y,lenght,20),Rect(x,480-y,lenght,20),Rect(x,y+20,20,height),Rect(x+lenght-20,y+20,20,closeHeight),Rect(x+lenght-20,480-y-closeHeight,20,closeHeight)]

	x=640-100-lenght
	rectList=rectList+[Rect(x,y,lenght,20),Rect(x,480-y,lenght,20),Rect(x+lenght-20,y+20,20,height),Rect(x,y+20,20,closeHeight),Rect(x,480-y-closeHeight,20,closeHeight)]
	return rectList