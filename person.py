import pygame, sys
from pygame.locals import *
import random
import time


white=(255,255,255)
black=(0,0,0)
#green=(9,66,13)
green=(4,77,55)
#red = (220,0,0)
red=(145,3,36)
sky_blue=(111,145,237)
RED = (255,0,0)
GOLD=(214,185,21)
#blue=(0,0,100)
blue=(7,80,140)
Green=(0,225,0)
Red = (255,0,0)
brown=(59,42,8)
#yellow=(250,234,57)
yellow=(222,159,11)
grey=(149,150,149)
Dgrey=(4,1,36)
backblue=(8,1,82)
brown=(84,46,8)
lbrown=(112,79,55)
gray=(245,243,235)

pygame.init()
size = (700,600) 
screen = pygame.display.set_mode(size)
screen.fill(white)
pygame.display.set_caption('Harry Potter and the Maze of Horcruxes')




def main():
    
    
    
    name=False
    while name==False:
        trio=raw_input("\nPick a character from the golden trio (Harry, Ron, Hermione):")
        if trio=='harry' or trio=='Harry':
            person="hp.png"
            name=True
        elif trio=='ron' or trio=='Ron':
            person="hp ron.png"
            name=True
        elif trio=='hermione' or trio=='Hermione':
            person="hp hermione.png"
            name=True
        else:
            print "That is not a character of the following to choose from...\ni.e.Harry, Ron, Hermione."
            name=False
    
    
    
    
    
    #person icon
    corner=random.randint(0,3)
    x1=0
    y1=0
    hp_image=pygame.image.load(person)
    hp_image=pygame.transform.scale(hp_image,(20,20))
    screen.blit(hp_image,(x1,y1))
    pygame.draw.rect(screen, blue,(x1,y1,20,20),3)


    while True:
        for event in pygame.event.get():
            
            if event.type==QUIT:
                sys.exit()
    
            if event.type==KEYDOWN: #pushed a key/button
                if event.key==K_LEFT:
                    x1=x1-50
                   # restriction(y1,x1)
                    #x1,y1=restriction(y1,x1)
                    pygame.display.update()
                elif event.key==K_RIGHT:
                    x1=x1+50
                    #x1,y1=restriction(y1,x1)
                    pygame.display.update()
                elif event.key==K_UP:
                    y1=y1-50
                   # restriction(y1,x1)
                    #x1,y1=restriction(y1,x1)
                    pygame.display.update()
                elif event.key==K_DOWN:
                    y1=y1+50
                    #restriction(y1,x1)
                    #x1,y1=restriction(y1,x1)
                    pygame.display.update()
                    
                #drawMaze(screen)
                #drawDoors(screen)
                #drawSideBar(screen)
                #horcruxes(screen,a,b,c,d,e,f,g,h,i,j,k,l,m,n)
                pygame.draw.rect(screen,white,(0,0,700,600),0)
                screen.blit(hp_image,(x1,y1))
                pygame.draw.rect(screen, blue,(x1,y1,60,50),3)
                print 'x1=',x1
                print 'y1=',y1                
            pygame.display.update()

if __name__ == '__main__':
    main()
