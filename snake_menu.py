#!/usr/bin/env/ python
#Snake Game
#Written By Kristopher Pellizzi

import sys,time,random,pygame
from pygame.locals import *
import snake_normal,snake_easy,snake_hard, stats, choose_lvl

def menu():

	pygame.init()
	playSurface=pygame.display.set_mode((640,480))
	blackColour=(0,0,0)
	greyColour=(150,150,150)
	whiteColour=(255,255,255)
	fpsClock=pygame.time.Clock()
	selectorPosition=None
	pygame.display.set_caption('Snake')

	while True:
		playSurface.fill(blackColour)
		title=pygame.font.Font('freesansbold.ttf',250)
		titleSurf=title.render('Snake',True, greyColour)
		titleRect=titleSurf.get_rect()
		titleRect.midtop=(320,10)
		playSurface.blit(titleSurf,titleRect)
		diff=pygame.font.Font('freesansbold.ttf',50)
		diffSurf=diff.render('Difficolta:',True,greyColour)
		diffRect=diffSurf.get_rect()
		diffRect.midbottom=(titleRect.midtop[0],titleRect.midbottom[1]+100)
		playSurface.blit(diffSurf,diffRect)
		normal=pygame.font.Font('freesansbold.ttf',35)
		normalSurf=normal.render('Normale',True,greyColour)
		normalRect=normalSurf.get_rect()
		normalRect.midtop=(diffRect.midbottom[0],diffRect.midbottom[1]+50)
		playSurface.blit(normalSurf,normalRect)
		easy=pygame.font.Font('freesansbold.ttf',35)
		easySurf=easy.render('Facile',True,greyColour)
		easyRect=easySurf.get_rect()
		easyRect.top=normalRect.top
		easyRect.right=normalRect.left-50
		playSurface.blit(easySurf,easyRect)
		hard=pygame.font.Font('freesansbold.ttf',35)
		hardSurf=hard.render('Difficile',True,greyColour)
		hardRect=hardSurf.get_rect()
		hardRect.top=normalRect.top
		hardRect.left=normalRect.right+50
		playSurface.blit(hardSurf,hardRect)
		quitSurf=normal.render('Esci',True,greyColour)
		quitRect=quitSurf.get_rect()
		quitRect.midtop=(hardRect.midbottom[0],hardRect.midbottom[1]+25)
		playSurface.blit(quitSurf,quitRect)
		statSurf=normal.render('Statistiche',True,greyColour)
		statRect=statSurf.get_rect()
		statRect.midtop=(normalRect.midbottom[0],normalRect.midbottom[1]+25)
		playSurface.blit(statSurf,statRect)
		lvlSurf=normal.render('Livelli',True,greyColour)
		lvlRect=lvlSurf.get_rect()
		lvlRect.midtop=(easyRect.midbottom[0],easyRect.midbottom[1]+25)
		playSurface.blit(lvlSurf,lvlRect)
		byFont=pygame.font.Font('freesansbold.ttf',25)
		bySurf=byFont.render('by Kristopher Pellizzi',True,greyColour)
		byRect=bySurf.get_rect()
		byRect.topleft=(titleRect.midbottom[0]+100,titleRect.midbottom[1])
		playSurface.blit(bySurf,byRect)

		padding=[-5,5]
		if selectorPosition==None:
			left=normalRect.left
			right=normalRect.right
			top=normalRect.top
			bottom=normalRect.bottom

		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==K_RIGHT:
					print('right key pressed')
					if selectorPosition!=None:
						if selectorPosition[2]==normalRect.topright:
							left=hardRect.left
							right=hardRect.right
						if selectorPosition[2]==easyRect.topright:
							left=normalRect.left
							right=normalRect.right
						if selectorPosition[2]==statRect.topright:
							left=quitRect.left
							right=quitRect.right
						if selectorPosition[2]==lvlRect.topright:
							left=statRect.left
							right=statRect.right
				if event.key==K_LEFT:
					print('left key pressed')
					if selectorPosition!=None:
						if selectorPosition[2]==normalRect.topright:
							left=easyRect.left
							right=easyRect.right
						if selectorPosition[2]==hardRect.topright:
							left=normalRect.left
							right=normalRect.right
						if selectorPosition[2]==quitRect.topright:
							left=statRect.left
							right=statRect.right
						if selectorPosition[2]==statRect.topright:
							left=lvlRect.left
							right=lvlRect.right
				if event.key==K_DOWN:
					print('down key pressed')
					left=statRect.left
					right=statRect.right
					bottom=statRect.bottom
					top=statRect.top
				if event.key==K_UP:
					print('up key pressed')
					left=normalRect.left
					right=normalRect.right
					top=normalRect.top
					bottom=normalRect.bottom
				if event.key==K_RETURN:
					if selectorPosition!=None:
						if selectorPosition[2]==easyRect.topright:
							playSurface.fill(blackColour)
							snake_easy.play()
						if selectorPosition[2]==normalRect.topright:
							playSurface.fill(blackColour)
							snake_normal.play()
						if selectorPosition[2]==hardRect.topright:
							playSurface.fill(blackColour)
							snake_hard.play()
						if selectorPosition[2]==statRect.topright:
							playSurface.fill(blackColour)
							stats.see()
						if selectorPosition[2]==lvlRect.topright:
							playSurface.fill(blackColour)
							choose_lvl.lvls()
						if selectorPosition[2]==quitRect.topright:
							pygame.quit()
							sys.exit()
				if event.key==K_ESCAPE:
					pygame.quit()
					sys.exit()

		selectorPosition=[(left,bottom),(right,bottom),(right,top),(left,top)]
		selectorPadding=[(left+padding[0],bottom+padding[1]),(right+padding[1],bottom+padding[1]),(right+padding[1],top+padding[0]),(left+padding[0],top+padding[0])]
		pygame.draw.lines(playSurface,whiteColour,True,selectorPadding,3)
		pygame.display.flip()	
		fpsClock.tick(30)