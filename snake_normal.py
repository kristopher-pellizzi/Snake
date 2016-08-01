#!/usr/bin/env/ python
#Snake Game
#Written By Kristopher Pellizzi

import pygame, sys, time, random
from pygame.locals import *
import snake_gameover

def play():

	print('Si gioca!')
	fpsClock=pygame.time.Clock()

	screen_width=640
	screen_height=480
	playSurface=pygame.display.set_mode((screen_width,screen_height))

	redColour=(255,0,0)
	whiteColour=(255,255,255)
	blackColour=(0,0,0)
	greyColour=(150,150,150)
	snakePosition=[100,100]
	snakeSegments=[[100,100],[80,100],[60,100]]
	raspberryPosition=[300,300]
	raspberrySpawned=1
	direction='right'
	changeDirection=direction

	while True:
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			elif event.type==KEYDOWN:
				if event.key==K_RIGHT or event.key==ord('d'):
					changeDirection='right'
				if event.key==K_LEFT or event.key==ord('a'):
					changeDirection='left'
				if event.key==K_UP or event.key==ord('w'):
					changeDirection='up'
				if event.key==K_DOWN or event.key==ord('s'):
					changeDirection='down'
				if event.key==K_ESCAPE:
					pygame.event.post(pygame.event.Event(QUIT))
		if changeDirection=='left' and not direction=='right':
			direction=changeDirection
		if changeDirection=='right' and not direction=='left':
			direction=changeDirection
		if changeDirection=='up' and not direction=='down':
			direction=changeDirection
		if changeDirection=='down' and not direction=='up':
			direction=changeDirection
		if direction=='right':
			snakePosition[0]+=20
		if direction=='left':
			snakePosition[0]-=20
		if direction=='up':
			snakePosition[1]-=20
		if direction=='down':
			snakePosition[1]+=20
		snakeSegments.insert(0,list(snakePosition))
		if snakePosition==raspberryPosition:
			raspberrySpawned=0
		else:
			snakeSegments.pop()
		if raspberrySpawned==0:
			x=random.randrange(0,32)
			y=random.randrange(0,24)
			raspberryPosition=[x*20,y*20]
		raspberrySpawned=1
		playSurface.fill(blackColour)
		for position in snakeSegments:
			pygame.draw.rect(playSurface,whiteColour,Rect(position[0],position[1],20,20))		#pygame.display.flip()
		pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0],raspberryPosition[1],20,20))
		pygame.display.flip()
		if snakePosition[0]<0 or snakePosition[0]>620 or snakePosition[1]<0 or snakePosition[1]>460:
			snake_gameover.GameOver()
		for body in snakeSegments[1:]:
			if body==snakePosition:
				snake_gameover.GameOver()	

		fpsClock.tick(15)