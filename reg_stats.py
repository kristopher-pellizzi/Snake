#! /usr/bin/env python
#Snake Game
#Written by Kristopher Pellizzi

def reg(diff,best,newbest,f_content):
	f_handler=open('.game_stats.txt','w')
	for line in f_content:
		line_list=line.split('=')
		if line_list[0]==diff:
			if newbest!=0:
				line_list[1]=str(newbest)
			else:
				line_list[1]=str(best)
		if line_list[0]=='game_played':
			line_list[1]=str(int(line_list[1])+1)
		if '\n' in line_list[1]:
			stat_str=line_list[0]+'='+line_list[1]
		else:
			stat_str=line_list[0]+'='+line_list[1]+'\n'
		f_handler.write(stat_str)
	f_handler.close()