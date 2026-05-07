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

while True:
    try:
        noplayers=int(input(f"Enter number of players ({minplayer}-{maxplayer}): ").strip())
        #checks if entered number is within valid range
        if minplayer<=noplayers<=maxplayer:
            #if valid breaks out of the loop
            break
        print(f"Plz enter a number between {minplayer} and {maxplayer}.")
    except ValueError:
        print("Plz enter a valid integer!!")
#list for storing player names
playernames = []
for i in range(noplayers):
    name=input(f"Enter name for player {i+1}: ").strip()
    #adding name to list but if there is no name then [player x]
    playernames.append(name if name else f"Player {i+1}")
#pygame initialization
pygame.init()
display = pygame.display.set_mode((width,height)) #-> created the game window with width & height
clock = pygame.time.Clock() #-> This is for to control the frame rate
font = pygame.font.SysFont("Impact",25)
pygame.display.set_caption("Chain Reaction %d Player" % noplayers) #-> Title for the game window
#grids
blocks = 40 #-> the size of each grid cell in pixels
top_offset = 40 #-> the header area for player names
scr=[] #-> to store game scores for each players
for i in range(noplayers):
    scr.append(0)
players=[] #-> for storeing player colors
for i in range (noplayers):
    players.append(playercolor[i])
d=blocks//2-2 #-> calculates the diameter of orbs based on blck sixe
cols=int(width//blocks) #-> number of cols in the grid 
rows=int((height-top_offset)//blocks) #-> number of rows [top offset is the header so it's needs to minused]
grid=[] #-> create an empty list that will store the game grid cells
def close(): #-> when user wants to exit.
    pygame.quit() #-> quit pygame 
    sys.exit() #-> exits the entire python program.
class Spot(): #-> each cell in the game grid is a spot object
    def __init__(self): #-> when a new spot object is created
        self.color=border 
        self.nghbr=[] #-> for neighboring cells
        self.noOrbs=0
    def addnghbr(self,i,j): #-> to find and store [up,down,left,right]
        if i>0: #-> check if there's a cell above 
            self.nghbr.append(grid[i-1][j]) #-> then add the cell above
        if i<cols-1: #-> check if there's a cell below
            self.nghbr.append(grid[i+1][j]) #-> then add the cell below
        if j<rows-1: #-> check if there's a cell right
            self.nghbr.append(grid[i][j+1]) #-> then add the cell right
        if j>0: #-> check if there's a cell left
            self.nghbr.append(grid[i][j-1]) #-> then add the cell left
def initGrid(): #-> creates a fresh grid for a new game
    global grid,score,players 
    score=[] #-> creates fresh scr list for new game
    for i in range(noplayers): #-> loop through each player and reset their scr to 0
        score.append(0)
    players=[] #-> creates fresh color list for new game
    for i in range(noplayers): #-> loop thorugh each color and assign their color
        players.append(playercolor[i])
    grid=[[]for _ in range(cols)] #-> creates a grid of empty lists [one list per cols]
    for i in range(cols): #-> Outer loop: go through each column
        for j in range(rows): #-> Inner loop: go through each row
            newObj=Spot() #-> Create a new Spot object for this grid position
            grid[i].append(newObj) #-> Add this Spot to the grid at position [i][j]
    for i in range(cols):
        for j in range(rows):
            grid[i][j].addnghbr(i,j) #-> For each Spot, find its neighboring cells
def drawGrid(currentIndex): #-> draw the game grid line
    r=0 #-> init row position to 0
    c=0 #-> init col position to 0
    for i in range(cols): #-> loop through each col
        r+=blocks #-> move row pos dwn by one blc
        c+=blocks #-> move col pos rght by one blc
        # Draw a vertical line at position c (separates columns)
        # Uses current player's color, from top_offset to bottom of screen
        pygame.draw.line(display,players[currentIndex],(c,top_offset),(c,height))
        # Draw a horizontal line at position r (separates rows)
        # Uses current player's color, across the entire width
        pygame.draw.line(display,players[currentIndex],(0,top_offset+r),(width,top_offset+r))
def drawCurrentPlayerName(currentIndex): 
    txt=font.render(f"Turn: {playernames[currentIndex]}",True,white) #->txt showing current player name
    txt_rect=txt.get_rect(center=(width//2,top_offset//2)) #-> get the rect that contains the text so we can pos it
    display.blit(txt,txt_rect) #-> draw the text on the screen at the centered pos
def showPresentGrid(vibrate=1):
    r=-blocks
    c=-blocks
    padding=2
    for i in range(cols):
        r+=blocks
        c=-blocks
        for j in range(rows):
            c+=blocks
            if grid[i][j].noOrbs==0:
                grid[i][j].color=border
            elif grid[i][j].noOrbs==1:
                pygame.draw.ellipse(display,grid[i][j].color,(r+blocks/2-d/2+vibrate,c+blocks/2-d/2+top_offset,d,d))
            elif grid[i][j].noOrbs==2:
                pygame.draw.ellipse(display,grid[i][j].color,(r+5,c+blocks/2-d/2-vibrate+top_offset,d,d))
                pygame.draw.ellipse(display,grid[i][j].color,(r+d/2+blocks/2-d/2+vibrate,c+blocks/2-d/2+top_offset,d,d))
            elif grid[i][j].noOrbs==3:
                #first Orb at 90 degree [top]
                angle=90
                x=r+(d/2)*cos(radians(angle))+blocks/2-d/2
                y=c+(d/2)*sin(radians(angle))+blocks/2-d/2+top_offset
                pygame.draw.ellipse(display,grid[i][j].color,(x-vibrate,y,d,d))
                #second Orb at 90+90 = 180 degree [left side]
                x=r+(d/2)*cos(radians(angle+90))+blocks/2-d/2
                y=c+(d/2)*sin(radians(angle+90))+5+top_offset
                pygame.draw.ellipse(display,grid[i][j].color,(x+vibrate,y,d,d))
                #third Orb at 90-90 = 0 degree [right side]
                x=r+(d/2)*cos(radians(angle-90))+blocks/2-d/2
                y=c+(d/2)*sin(radians(angle-90))+5+top_offset
                pygame.draw.ellipse(display,grid[i][j].color,(x-vibrate,y,d,d))
        pygame.display.update()
def addOrb(i,j,color):
    grid[i][j].noOrbs+=1 #-> add one orb to the cell
    grid[i][j].color=color #-> change the cell color to the player's color
    if grid[i][j].noOrbs>=len(grid[i][j].nghbr): #-> if the number of orbs in the cell is greater than or equal to the number of neighbors
        overFlow(grid[i][j],color)#-> add an orb to each neighboring cell (this can cause a chain reaction)
def overFlow(cell,color):
    showPresentGrid()
    cell.noOrbs=0
    for m in range(len(cell.nghbr)):
        cell.nghbr[m].noOrbs+=1
        cell.nghbr[m].color=color
        if cell.nghbr[m].noOrbs>=len(cell.nghbr[m].nghbr):
            overFlow(cell.nghbr[m],color)