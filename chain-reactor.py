import pygame
import sys
from math import * # for math functions
width=400 #-> game window width
height=400 #-> game window height
background=(0,0,0) #-> all black
border=(208,211,212) #-> border color as light gray for grid lines
#text color
white=(244,246,247)
#player colors
red=(231,76,60)
green=(88,214,141)
violet=(136,78,160)
yellow=(244,208,63)
#list for all player colors in order
playercolor = [red,green,violet,yellow]
minplayer,maxplayer=2,4