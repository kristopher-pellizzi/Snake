#! /usr/bin/env python
#Snake Game
#Written by Kristopher Pellizzi

import sys,time,random,pygame
from pygame.locals import *
import snake_menu

def lvls():
	greyColour=(150,150,150)
	blackColour=(0,0,0)
	whiteColour=(255,255,255)
	playSurface=pygame.display.set_mode((640,480))
	playRect=playSurface.get_rect()
	selectorPosition=None
	imgs={
		'noLvl':pygame.transform.scale(pygame.image.load('snake_0.tiff').convert(),(350,250)),
		'lvl1':pygame.transform.scale(pygame.image.load('snake_1.tiff').convert(),(350,250)),
		'lvl2':pygame.transform.scale(pygame.image.load('snake_2.tiff').convert(),(350,250)),
		'lvl3':pygame.transform.scale(pygame.image.load('snake_3.tiff').convert(),(350,250)),
		'lvl4':pygame.transform.scale(pygame.image.load('snake_4.tiff').convert(),(350,250))
	}
	while True:
		playSurface.fill(blackColour)
		titleFont=pygame.font.Font('freesansbold.ttf',100)
		font=pygame.font.Font('freesansbold.ttf',40)
		title=titleFont.render('Scegli il livello: ',True,greyColour)
		titleRect=title.get_rect()
		titleRect.midtop=(playRect.midtop[0],playRect.midtop[1]+15)
		playSurface.blit(title,titleRect)
		noLvl=font.render('Nessun livello',True,greyColour)
		noLvlRect=noLvl.get_rect()
		noLvlRect.topleft=(playRect.left+20,titleRect.bottom+20)
		playSurface.blit(noLvl,noLvlRect)
		lvl1=font.render('Livello 1',True,greyColour)
		lvl1Rect=lvl1.get_rect()
		lvl1Rect.topleft=(noLvlRect.bottomleft[0],noLvlRect.bottomleft[1]+10)
		playSurface.blit(lvl1,lvl1Rect)
		lvl2=font.render('Livello 2',True,greyColour)
		lvl2Rect=lvl2.get_rect()
		lvl2Rect.topleft=(lvl1Rect.left,lvl1Rect.bottom+10)
		playSurface.blit(lvl2,lvl2Rect)
		lvl3=font.render('Livello 3',True,greyColour)
		lvl3Rect=lvl3.get_rect()
		lvl3Rect.topleft=(lvl2Rect.left,lvl2Rect.bottom+10)
		playSurface.blit(lvl3,lvl3Rect)
		lvl4=font.render('Livello 4',True,greyColour)
		lvl4Rect=lvl4.get_rect()
		lvl4Rect.topleft=(lvl3Rect.left,lvl3Rect.bottom+10)
		playSurface.blit(lvl4,lvl4Rect)
		back=font.render('Torna al menu principale',True,greyColour)
		backRect=back.get_rect()
		backRect.bottomleft=(lvl1Rect.left, playRect.bottom-15)
		playSurface.blit(back,backRect)
		

		if selectorPosition==None:
			left=noLvlRect.left
			right=noLvlRect.right
			top=noLvlRect.top
			bottom=noLvlRect.bottom

		selectorPosition=[(left,bottom),(right,bottom),(right,top),(left,top)]
		selectorPadding=[(left-5,bottom+5),(right+5,bottom+5),(right+5,top-5),(left-5,top-5)]
		pygame.draw.lines(playSurface,whiteColour,True,selectorPadding,3)

		if selectorPosition==None or selectorPosition[2]==noLvlRect.topright:
			imgPrev=imgs['noLvl']
		if selectorPosition[2]==lvl1Rect.topright:
			imgPrev=imgs['lvl1']
		if selectorPosition[2]==lvl2Rect.topright:
			imgPrev=imgs['lvl2']
		if selectorPosition[2]==lvl3Rect.topright:
			imgPrev=imgs['lvl3']
		if selectorPosition[2]==lvl4Rect.topright:
			imgPrev=imgs['lvl4']
		if selectorPosition[2]!=backRect.topright:
			imgRect=imgPrev.get_rect()
			imgRect.topleft=(noLvlRect.right+75,noLvlRect.top)
			playSurface.blit(imgPrev,imgRect)
			pygame.draw.lines(playSurface,whiteColour,True,[imgRect.bottomleft,imgRect.bottomright,imgRect.topright,imgRect.topleft])

		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==K_RETURN:
					if selectorPosition!=None:
						if selectorPosition[2]==backRect.topright:
							snake_menu.menu()
						else:
							fh=open('.lvl_chosen.txt','w')
							if selectorPosition[2]==noLvlRect.topright:
								fh.write('0')
							if selectorPosition[2]==lvl1Rect.topright:
								fh.write('1')
							if selectorPosition[2]==lvl2Rect.topright:
								fh.write('2')
							if selectorPosition[2]==lvl3Rect.topright:
								fh.write('3')
							if selectorPosition[2]==lvl4Rect.topright:
								fh.write('4')
							fh.close()
							snake_menu.menu()

				if event.key==K_DOWN:
					if selectorPosition!=None:
						if selectorPosition[2]==noLvlRect.topright:
							left=lvl1Rect.left
							right=lvl1Rect.right
							top=lvl1Rect.top
							bottom=lvl1Rect.bottom
						if selectorPosition[2]==lvl1Rect.topright:
							left=lvl2Rect.left
							right=lvl2Rect.right
							top=lvl2Rect.top
							bottom=lvl2Rect.bottom
						if selectorPosition[2]==lvl2Rect.topright:
							left=lvl3Rect.left
							right=lvl3Rect.right
							top=lvl3Rect.top
							bottom=lvl3Rect.bottom
						if selectorPosition[2]==lvl3Rect.topright:
							left=lvl4Rect.left
							right=lvl4Rect.right
							top=lvl4Rect.top
							bottom=lvl4Rect.bottom
						if selectorPosition[2]==lvl4Rect.topright:
							left=backRect.left
							right=backRect.right
							top=backRect.top
							bottom=backRect.bottom
				if event.key==K_UP:
					if selectorPosition!=None:	
						if selectorPosition[2]==lvl1Rect.topright:
							top=noLvlRect.top
							bottom=noLvlRect.bottom
							left=noLvlRect.left
							right=noLvlRect.right
						if selectorPosition[2]==backRect.topright:
							left=lvl4Rect.left
							right=lvl4Rect.right
							top=lvl4Rect.top
							bottom=lvl4Rect.bottom
						if selectorPosition[2]==lvl2Rect.topright:
							left=lvl1Rect.left
							right=lvl1Rect.right
							top=lvl1Rect.top
							bottom=lvl1Rect.bottom
						if selectorPosition[2]==lvl3Rect.topright:
							left=lvl2Rect.left
							right=lvl2Rect.right
							top=lvl2Rect.top
							bottom=lvl2Rect.bottom
						if selectorPosition[2]==lvl4Rect.topright:
							left=lvl3Rect.left
							right=lvl3Rect.right
							top=lvl3Rect.top
							bottom=lvl3Rect.bottom
				if event.key==K_ESCAPE:
					snake_menu.menu()

		pygame.display.flip()