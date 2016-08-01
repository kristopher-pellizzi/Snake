#!/usr/bin/env/ python
#Snake Game
#Written By Kristopher Pellizzi

import sys,time,random,pygame
from pygame.locals import *
import snake_normal,snake_easy,snake_hard

def menu():

	pygame.init()
	playSurface=pygame.display.set_mode((640,480))
	blackColour=(0,0,0)
	greyColour=(150,150,150)
	whiteColour=(255,255,255)
	fpsClock=pygame.time.Clock()
	actualPos=None
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
		quitRect.midtop=(normalRect.midbottom[0],normalRect.midbottom[1]+25)
		playSurface.blit(quitSurf,quitRect)
		byFont=pygame.font.Font('freesansbold.ttf',25)
		bySurf=byFont.render('by Kristopher Pellizzi',True,greyColour)
		byRect=bySurf.get_rect()
		byRect.topleft=(titleRect.midbottom[0]+100,titleRect.midbottom[1])
		playSurface.blit(bySurf,byRect)

		padding=[-5,5]
		if actualPos==None:
			left=normalRect.left
			right=normalRect.right
			top=normalRect.top
			bottom=normalRect.bottom

		for event in pygame.event.get():
			if event.type==KEYDOWN:
				if event.key==K_RIGHT:
					print('right key pressed')
					if actualPos!=None:
						if actualPos[2]==normalRect.topright:
							left=hardRect.left
							right=hardRect.right
						if actualPos[2]==easyRect.topright:
							left=normalRect.left
							right=normalRect.right
				if event.key==K_LEFT:
					print('left key pressed')
					if actualPos!=None:
						if actualPos[2]==normalRect.topright:
							left=easyRect.left
							right=easyRect.right
						if actualPos[2]==hardRect.topright:
							left=normalRect.left
							right=normalRect.right
				if event.key==K_DOWN:
					print('down key pressed')
					left=quitRect.left
					right=quitRect.right
					bottom=quitRect.bottom
					top=quitRect.top
				if event.key==K_UP:
					print('up key pressed')
					left=normalRect.left
					right=normalRect.right
					top=normalRect.top
					bottom=normalRect.bottom
				if event.key==K_RETURN:
					if selectorPosition[2]==easyRect.topright:
						playSurface.fill(blackColour)
						snake_easy.play()
					if selectorPosition[2]==normalRect.topright:
						playSurface.fill(blackColour)
						snake_normal.play()
					if selectorPosition[2]==hardRect.topright:
						playSurface.fill(blackColour)
						snake_hard.play()
					if selectorPosition[2]==quitRect.topright:
						pygame.quit()
						sys.exit()
				if event.key==K_ESCAPE:
					pygame.quit()
					sys.exit()

		selectorPosition=[(left,bottom),(right,bottom),(right,top),(left,top)]
		actualPos=selectorPosition
		selectorPadding=[(left+padding[0],bottom+padding[1]),(right+padding[1],bottom+padding[1]),(right+padding[1],top+padding[0]),(left+padding[0],top+padding[0])]
		pygame.draw.lines(playSurface,whiteColour,True,selectorPadding,3)
		pygame.display.flip()	
		fpsClock.tick(30)