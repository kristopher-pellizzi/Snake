#!/usr/bin/env/ python
#Snake Game
#Written By Kristopher Pellizzi

import sys,time,random,pygame
from pygame.locals import *
import snake_menu

def see():
	playSurface=pygame.display.set_mode((640,480))
	fpsClock=pygame.time.Clock()
	playRect=playSurface.get_rect()
	greyColour=(150,150,150)
	blackColour=(0,0,0)
	whiteColour=(255,255,255)
	selectorPosition=None

	while True:
		fh=open('game_stats.txt','r')
		f_content=fh.readlines()
		stat_list=[]
		for line in f_content:
			line_list=line.split('=')
			stat_list=stat_list+[line_list[1]]
		fh.close()
		playSurface.fill(blackColour)
		titlefont=pygame.font.Font('freesansbold.ttf',100)
		font=pygame.font.Font('freesansbold.ttf',40)
		titleSurf=titlefont.render('Statistiche',True,greyColour)
		titleRect=titleSurf.get_rect()
		titleRect.midtop=(playRect.midtop[0],playRect.midtop[1]+15)
		playSurface.blit(titleSurf,titleRect)
		bestSurf=font.render('Migliori punteggi:',True,greyColour)
		bestRect=bestSurf.get_rect()
		bestRect.topleft=(playRect.left+10,titleRect.bottom+25)
		playSurface.blit(bestSurf,bestRect)
		easySurf=font.render('Facile: '+str(stat_list[0]),True,greyColour)
		easyRect=easySurf.get_rect()
		easyRect.topleft=(bestRect.midbottom[0],bestRect.midbottom[1]+10)
		playSurface.blit(easySurf,easyRect)
		normalSurf=font.render('Normale: '+str(stat_list[1]),True,greyColour)
		normalRect=normalSurf.get_rect()
		normalRect.topleft=(easyRect.bottomleft[0],easyRect.bottomleft[1]+10)
		playSurface.blit(normalSurf,normalRect)
		hardSurf=font.render('Difficile: '+str(stat_list[2]),True,greyColour)
		hardRect=hardSurf.get_rect()
		hardRect.topleft=(normalRect.bottomleft[0],normalRect.bottomleft[1]+10)
		playSurface.blit(hardSurf,hardRect)
		gameSurf=font.render('Partite giocate: '+str(stat_list[3]),True,greyColour)
		gameRect=gameSurf.get_rect()
		gameRect.topleft=(bestRect.bottomleft[0],hardRect.bottomleft[1]+10)
		playSurface.blit(gameSurf,gameRect)
		quitSurf=font.render('Torna al menu',True,greyColour)
		quitRect=quitSurf.get_rect()
		quitRect.bottomright=(playRect.bottomright[0]-25,playRect.bottomright[1]-25)
		playSurface.blit(quitSurf,quitRect)
		rstSurf=font.render('Azzera statistiche',True,greyColour)
		rstRect=rstSurf.get_rect()
		rstRect.bottomright=(quitRect.bottomleft[0]-15,quitRect.bottomleft[1])
		playSurface.blit(rstSurf,rstRect)
		
		if selectorPosition==None:
			left=quitRect.left
			right=quitRect.right
			top=quitRect.top
			bottom=quitRect.bottom

		for event in pygame.event.get():
			if event.type==KEYDOWN:
				if event.key==K_RETURN:
					if selectorPosition!=None:
						if selectorPosition[2]==quitRect.topright:
							snake_menu.menu()
						if selectorPosition[2]==rstRect.topright:
							fh=open('game_stats.txt','w')
							for line in f_content:
								line_list=line.split('=')
								if line_list[0]=='game_played':
									terminal=str(0)
								else:
									terminal='\n'
								fh.write(line_list[0]+'='+terminal)
							fh.close()
				if event.key==K_ESCAPE:
					snake_menu.menu()
				if event.key==K_LEFT:
					left=rstRect.left
					right=rstRect.right
					top=rstRect.top
					bottom=rstRect.bottom
				if event.key==K_RIGHT:
					left=quitRect.left
					right=quitRect.right
					top=quitRect.top
					bottom=quitRect.bottom
			if event.type==QUIT:
				pygame.quit()
				sys.exit()

		selectorPosition=[(left,bottom),(right,bottom),(right,top),(left,top)]
		selectorPadding=[(left-5,bottom+5),(right+5,bottom+5),(right+5,top-5),(left-5,top-5)]
		pygame.draw.lines(playSurface,whiteColour,True,selectorPadding,3)
		pygame.display.flip()

		fpsClock.tick(30)