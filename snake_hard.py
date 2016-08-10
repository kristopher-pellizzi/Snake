#!/usr/bin/env/ python
#Snake Game
#Written By Kristopher Pellizzi

import pygame, sys, time, random
from pygame.locals import *
import snake_gameover, lvls, reg_stats

def play():

	print('Si gioca!')
	fpsClock=pygame.time.Clock()

	screen_width=640
	screen_height=480
	playSurface=pygame.display.set_mode((screen_width,screen_height))
	playRect=playSurface.get_rect()

	redColour=(255,0,0)
	whiteColour=(255,255,255)
	blackColour=(0,0,0)
	greyColour=(150,150,150)
	raspberryPosition=[random.randrange(0,32)*20,random.randrange(0,24)*20]
	raspberrySpawned=1
	points=0
	newbest=0
	raspCount=0
	ticks=10
	ticksLimit=25
	f_handler=open('.lvl_chosen.txt','r')
	f_content=f_handler.read()
	lvl=int(f_content)
	if lvl==2:
		snakePosition=[20,240]
		snakeSegments=[(20,240),(20,220),(20,200)]
		direction='down'
	else:
		snakePosition=[320,240]
		snakeSegments=[[320,240],[300,240],[280,240]]
		direction='right'
	changeDirection=direction
	f_handler.close()
	f_handler=open('.game_stats.txt','r')	
	f_content=f_handler.readlines()
	lvlSurf=[]
	for line in f_content:
		line_list=line.split('=')
		if line_list[0]=='hard_best':
			if line_list[1]=='\n':
				best=0
			else:
				best=line_list[1]
	f_handler.close()
	lines_pos=[playRect.topleft,(playRect.topright[0]-1,playRect.topright[1]),(playRect.bottomright[0]-1,playRect.bottomright[1]-1),(playRect.bottomleft[0],playRect.bottomleft[1]-1)]

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
		playSurface.fill(blackColour)
		if lvl!=0:
			if lvl==1:
				lvlSurf=lvls.lvl1()
			if lvl==2:
				lvlSurf=lvls.lvl2()
			if lvl==3:
				lvlSurf=lvls.lvl3()
			if lvl==4:
				lvlSurf=lvls.lvl4()
			for rect in lvlSurf:
				pygame.draw.rect(playSurface,whiteColour,rect)
		if snakePosition==raspberryPosition:
			raspberrySpawned=0
			raspCount+=1
			points+=1
		else:
			snakeSegments.pop()
		if raspberrySpawned==0:
			x=random.randrange(0,32)
			y=random.randrange(0,24)
			raspberryPosition=[x*20,y*20]
			raspberryRect=Rect(raspberryPosition[0],raspberryPosition[1],20,20)
			while raspberryRect.collidelist(lvlSurf)!=-1:
				x=random.randrange(0,32)
				y=random.randrange(0,24)
				raspberryPosition=[x*20,y*20]
				raspberryRect=Rect(raspberryPosition[0],raspberryPosition[1],20,20)
			raspberrySpawned=1
		for position in snakeSegments:
			pygame.draw.rect(playSurface,whiteColour,Rect(position[0],position[1],20,20))
		pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0],raspberryPosition[1],20,20))
		pygame.draw.lines(playSurface,whiteColour,True,lines_pos)

		font=pygame.font.Font('freesansbold.ttf',30)
		countDisp=font.render(str(points),True,greyColour)
		countRect=countDisp.get_rect()
		countRect.topleft=(playRect.topleft[0]+5,playRect.topleft[1]+5)
		playSurface.blit(countDisp,countRect)

		if (best==0 or points>int(best)) and points>0 :
			bestDisp=font.render('NEW BEST!',True,greyColour)
			bestRect=bestDisp.get_rect()
			bestRect.topleft=(countRect.topright[0]+5,countRect.topright[1])
			playSurface.blit(bestDisp,bestRect)
			newbest=points

		pygame.display.flip()
		
		snakeHead=Rect(snakePosition[0],snakePosition[1],20,20)
		if snakeHead.collidelist(lvlSurf)!=-1:
			reg_stats.reg('hard_best',best,newbest,f_content)
			snake_gameover.GameOver()

		if snakePosition[0]<0 or snakePosition[0]>620 or snakePosition[1]<0 or snakePosition[1]>460:
			reg_stats.reg('hard_best',best,newbest,f_content)
			snake_gameover.GameOver()
		for body in snakeSegments[1:]:
			if body==snakePosition:
				reg_stats.reg('hard_best',best,newbest,f_content)
				snake_gameover.GameOver()	
		if raspCount>0 and raspCount%10==0 and ticks<ticksLimit:
			ticks+=2.5
			raspCount=0
		fpsClock.tick(ticks)