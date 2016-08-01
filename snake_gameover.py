import pygame, sys, time, random
from pygame.locals import *
import snake_menu

def GameOver():

	print('Gameover')
	playSurface=pygame.display.set_mode((640,480))
	blackColour=(0,0,0)
	greyColour=(150,150,150)
	gameOverFont=pygame.font.Font('freesansbold.ttf',100)
	gameOverSurf=gameOverFont.render('Game Over', True, greyColour)
	gameOverRect=gameOverSurf.get_rect()
	gameOverRect.midtop=(320,200)
	playSurface.blit(gameOverSurf,gameOverRect)
	pygame.display.flip()
	time.sleep(2)
	playSurface.fill(blackColour)
	snake_menu.menu()