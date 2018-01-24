#Samantha Stinson
#April 19,2015
#Mr.Cardinale

#Exam Project-Part 1
#Harry Potter and the Maze of Horcruzes

import pygame, sys
from pygame.locals import *
import random
import time

#boolean values
hraven=False
hscar=False
hcup=False
hlocket=False
hdiary=False
hsnake=False
hring=False
win=False


#colours
white=(255,255,255)
black=(0,0,0)
green=(4,77,55)
red=(145,3,36)
sky_blue=(111,145,237)
RED = (255,0,0)
GOLD=(214,185,21)
blue=(7,80,140)
Green=(0,225,0)
Red = (255,0,0)
brown=(59,42,8)
yellow=(222,159,11)
grey=(149,150,149)
Dgrey=(4,1,36)
backblue=(8,1,82)
brown=(84,46,8)
lbrown=(112,79,55)
gray=(245,243,235)

#pattern 1
pa_x=[100,500,100,500,110,500,550]
pa_y=[100,100,500,500,325,325,175]
#(100,100)
#(500,100)
#(100,500)
#(500,500)
#(110,325)
#(500,325)

#pattern 2
pb_x=[0,550,0,550,0,550,385]
pb_y=[0,550,325,325,575,25,435]
#(25,25)
#(575,575)
#(25,325)
#(575,325)
#(25,575)
#(575,25)

#pattern 3
pc_x=[250,100,200,350,500,425,100]
pc_y=[0,400,550,550,250,0,175]
#(250,25)
#(100,400)
#(200,575)
#(350,575)
#(500,250)
#(425,25)

#pattern 4
pd_x=[0,175,200,500,550,125,550]
pd_y=[175,175,375,400,175,550,550]
#(0,175)
#(175,175)
#(200,375)
#(500,400)
#(575,175)
#(125,575)

#pattern 5
pe_x=[0,25,50,75,100,125,150]
pe_y=[5,5,5,5,5,5,5]

#function:restriction
#@param: y1 (int), x1(int)
#@return: y1 (int), x1(int)
def restriction(y1,x1):
#restrictions
#horizontal line top
    if y1==50:
        if x1>=50 and x1<=150:
            print "You hit a wall!"
            y1=y1-20
        elif x1>=450 and x1<=600:
            print "You hit a wall!"
            y1=y1-20
        elif x1>=200 and x1<=225:
            print "You hit a wall!"
            y1=y1-20
    if y1==100:
        if x1>=300 and x1<=325:
            print "You hit a wall!"
            y1=y1-20
    if y1==125:
        if x1>=125 and x1<=225:
            print "You hit a wall!"
            y1=y1-20
        elif x1>=450 and x1<=475:
            print "You hit a wall!"
            y1=y1-20
    if y1==200:
        if x1>=0 and x1<=150:
            print "You hit a wall!"
            y1=y1-20
        elif x1>=200 and x1<=225:
            print "You hit a wall!"
            y1=y1-20
        elif x1>=375 and x1<=600:
            print "You hit a wall!"
            y1=y1-20
    if y1==275:
        if x1>=50 and x1<=75:
            print "You hit a wall!"
            y1=y1-20
        elif x1>=150 and x1<=175:
            print "You hit a wall!"
            y1=y1-20
        elif x1>=450 and x1<=475:
            print "You hit a wall!"
            y1=y1-20
    if y1==350:
        if x1>=50 and x1<=175:
            print "You hit a wall!"
            y1=y1-20
        elif x1>=475 and x1<=550:
            print "You hit a wall!"
            y1=y1-20
    if y1==375:
        if x1>=400 and x1<=475:
            print "You hit a wall!"
            y1=y1-20
    if y1==400:
        if x1>=150 and x1<=250:
            print "You hit a wall!"
            y1=y1-20
        elif x1>=325 and x1<=350:
            print "You hit a wall!"
            y1=y1-20
    if y1==400:
        if x1>=50 and x1<=75:
            print "You hit a wall!"
            y1=y1-20
    if y1==450:
        if x1>=525 and x1<=550:
            print "You hit a wall!"
            y1=y1-20
    if y1==475:
        if x1>=225 and x1<=350:
            print "You hit a wall!"
            y1=y1-20
    if y1==500:
        if x1>=150 and x1<=175:
            print "You hit a wall!"
            y1=y1-20
        elif x1>=375 and x1<=400:
            print "You hit a wall!"
            y1=y1-20
    if y1==525:
        if x1>=50  and x1<=175:
            print "You hit a wall!"
            y1=y1-20
        elif x1>=450 and x1<=550:
            print "You hit a wall!"
            y1=y1-20
    if y1==550:
        if x1>=300 and x1<=325:
            print "You hit a wall!"
            y1=y1-20
            
    #horizontal line bottom
    #y=y1-25
    if y1==25:
        if x1>=275 and x1<=300:
            print "You hit a wall!"
            y1=y1+20
    if y1==50:
        if x1>=300 and x1<=325:
            print "You hit the wall!"
            y1=y1+20
    if y1==75:
        if x1>=50 and x1<=150:
            print "You hit a wall!"
            y1=y1+20
        elif x1>=450 and x1<=550:
            print "You hit a wall!"
            y1=y1+20
    if y1==125:
        if x1>=375 and x1<=400:
            print "You hit a wall!"
            y1=y1+20
    if y1==150:
        if x1>=50 and x1<=75:
            print "You hit a wall!"
            y1=y1+20
        elif x1>=125 and x1<=225:
            print "You hit a wall!"
            y1=y1+20
        elif x1>=450 and x1<=475:
            print "You hit a wall!"
            y1=y1+20
        elif x1>=525 and x1<=550:
            print "You hit a wall!"
            y1=y1+20
    if y1==200:
        if x1>=300 and x1<=325:
            print "You hit a wall!"
            y1=y1+20
    if y1==225:
        if x1>=0 and x1<=150:
            print "You hit a wall!"
            y1=y1+20
        elif x1<=200 and x1>=225:
            print "You hit a wall!"
            y1=y1+20
        elif x1>=375 and x1<=600:
            print "You hit a wall!"
            y1=y1+20
    if y1==300:
        if x1>=525 and x1<=550:
            print "You hit a wall!"
            y1=y1+20
    if y1==375:
        if x1>=50 and x1<=175:
            print "You hit a wall!"
            y1=y1+20
        elif x1>=450 and x1<=550:
            print "You hit a wall!"
            y1=y1+20
    if y1==400:
        if x1>=400 and x1<=450:
            print "You hit a wall!"
            y1=y1+20
    if y1==425:
        if x1>=150 and x1<=250:
            print "You hit a wall!"
            y1=y1+v
    if y1==450:
        if x1>=150 and x1<=175:
            print "You hit a wall!"
            y1=y1+20
        elif x1>=400 and x1<=425:
            print "You hit a wall!"
            y1=y1+20
    if y1==500:
        if x1>=225 and x1<=350:
            print "You hit a wall!"
            y1=y1+20
    if y1==550:
        if x1>=50 and x1<=175:
            print "You hit a wall!"
            y1=y1+20
        elif x1>=225 and x1<=250:
            print "You hit a wall!"
            y1=y1+20
        elif x1>=375 and x1<=400:
            print "You hit a wall!"
            y1=y1+20
        elif x1>=400 and x1<=550:
            print "You hit a wall!"
            y1=y1+20
    #left side of lines
    if x1==50:
        if y1>=50 and y1<=150:
            print "You hit a wall!"
            x1=x1-20
        elif y1>=275 and y1<=375:
            print "You hit a wall!"
            x1=x1-20
        elif y1>=450 and y1<=550:
            print "You hit a wall!"
            x1=x1-20
    if x1==125:
        if y1>=125 and y1<=225:
            print "You hit a wall!"
            x1=x1-20
    if x1==150:
        if y1>=275 and y1<=450:
            print "You hit a wall!"
            x1=x1-20
        elif y1>=500 and y1<=600:
            print "You hit a wall!"
            x1=x1-20
    if x1==200:
        if y1>=50 and y1<=150:
            print "You hit a wall!"
            x1=x1-20
        elif y1>=200 and y1<=225:
            print "You hit a wall!"
            x1=x1-20
    if x1==225:
        if y1>=475 and y1<=550:
            print "You hit a wall!"
            x1=x1-20
    if x1==275:
        if y1>=0 and y1<=25:
            print "You hit a wall!"
            x1=x1-20
    if x1==300:
        if y1>=0 and y1<=50:
            print "You hit a wall!"
            x1=x1-20
        elif y1>=100 and y1<=200:
            print "You hit a wall!"
            x1=x1-20
        elif y1>=550 and y1<=600:
            print "You hit a wall!"
            x1=x1-20
    if x1==325:
        if y1>=400 and y1<=500:
            print "You hit a wall!"
            x1=x1-20
    if x1==375:
        if y1>=0 and y1<=125:
            print "You hit a wall!"
            x1=x1-20
        elif y1>=200 and y1<=225:
            print "You hit a wall!"
            x1=x1-20
        elif y1>=500 and y1<=550:
            print "You hit a wall!"
            x1=x1-20
    if x1==400:
        if y1>=375 and y1<=450:
            print "You hit a wall!"
            x1=x1-20
    if x1==450:
        if y1>=50 and y1<=75:
            print "You hit 1 wall!"
            x1=x1-20
        elif y1>=125 and y1<=150:
            print "You hit 2 wall!"
            x1=x1-20
        elif y1>=275 and y1<=400:
            print "You hit 3 wall!"
            x1=x1-20
        elif y1>=525 and y1<=550:
            print "You hit 4 wall!"
            x1=x1-20
    if x1==525:
        if y1>=50 and y1<=150:
            print "You hit a wall!"
            x1=x1-20
        elif y1>=200 and y1<=300:
            print "You hit a wall!"
            x1=x1-5
        elif y1>=1450 and y1<=550:
            print "You hit a wall!"
            x1=x1-20
    if x1==600:
        x1=x1-20
#right side of lines
    if x1==75:
        if y1>=50 and y1<=150:
            print "You hit a wall!"
            x1=x1+20
        elif y1>=275 and y1<=375:
            print "You hit a wall!"
            x1=x1+20
        elif y1>=450 and y1<=550:
            print "You hit a wall!"
            x1=x1+20
    if x1==150:
        if y1>=50 and y1<=75:
            print "You hit a wall!"
            x1=x1+20
        elif y1>=125 and y1<=225:
            print "You hit a wall!"
            x1=x1+20
    if x1==175:
        if y1>=275 and y1<=450:
            print "You hit a wall!"
            x1=x1+20
        elif y1>=500 and y1<=600:
            print "You hit a wall!"
            x1=x1+20
    if x1==225:
        if y1>=50 and y1<=150:
            print "You hit a wall!"
            x1=x1+20
        elif y1>=200 and y1<=225:
            print "You hit a wall!"
            x1=x1+20
    if x1==250:
        if y1>=400 and y1<=425:
            print "You hit a wall!"
            x1=x1+20
        elif y1>=475 and y1<=550:
            print "You hit a wall!"
            x1=x1+20
    if x1==300:
        if y1>=0 and y1<=25:
            print "You hit a wall!"
            x1=x1+20
    if x1==325:
        if y1>=0 and y1<=50:
            print "You hit a wall!"
            x1=x1+20
        elif y1>=100 and y1<=200:
            print "You hit a wall!"
            x1=x1+20
        elif y1>=550 and y1<=600:
            print "You hit a wall!"
            x1=x1+20
    if x1==400:
        if y1>=0 and y1<=125:
            print "You hit a wall!"
            x1=x1+20
        elif y1>=500 and y1<=550:
            print "You hit a wall!"
            x1=x1+20
    if x1==425:
        if y1>=375 and y1<=450:
            print "You hit a wall!"
            x1=x1+20
    if x1==475:
        if y1>=125 and y1<=150:
            print "You hit a wall!"
            x1=x1+20
        elif y1>=275 and y1<=400:
            print "You hit a wall!"
            x1=x1+20
    if x1==550:
        if y1>=50 and y1<=150:
            print "You hit a wall!"
            x1=x1+20
        elif y1>=200 and y1<=300:
            print "You hit a wall!"
            x1=x1+20
        elif y1>=350 and y1<=375:
            print "You hit a wall!"
            x1=x1+20
        elif y1>=450 and y1<=550:
            print "You hit a wall!"
            x1=x1+20
    #print "x1=", x1,  "and y1=", y1
    return x1,y1

#function:drawMaze
#@param: screen (int)
#@return: 
def drawMaze(screen):
    #pygame.draw.rect(screen,colour(x,y,width,height,),thickness)
    pygame.draw.rect(screen, white, (0,0,600,600),0)  
    
    gryffen_image=pygame.image.load("lion.png")
    gryffen_image=pygame.transform.scale(gryffen_image,(300,300))
    screen.blit(gryffen_image,(0,0))
    huffle_image=pygame.image.load("huffle.png")
    huffle_image=pygame.transform.scale(huffle_image,(275,300))
    screen.blit(huffle_image,(325,0))
    snake_image=pygame.image.load("slyth.png")
    snake_image=pygame.transform.scale(snake_image,(300,300))
    screen.blit(snake_image,(0,300))
    raven_image=pygame.image.load("ravenclaw.png")
    raven_image=pygame.transform.scale(raven_image,(275,300))
    screen.blit(raven_image,(325,300))
    
    #hufflepuff house area
    pygame.draw.rect(screen, black, (375,0,25,150),0)    
    pygame.draw.rect(screen, yellow, (450,50,100,25),0)
     
    pygame.draw.rect(screen, black, (525,75,25,75),0)
    pygame.draw.rect(screen, black, (450,125,25,25),0)
    pygame.draw.rect(screen, yellow, (375,200,225,25),0)
    pygame.draw.rect(screen, black, (525,200,25,100),0)
    pygame.draw.rect(screen, black, (450,275,25,25),0)
    #griffendor house area
    pygame.draw.rect(screen, red, (50,50,25,100),0)
    pygame.draw.rect(screen, red, (0,200,125,25),0)
    pygame.draw.rect(screen, yellow, (75,50,75,25),0)
    pygame.draw.rect(screen, yellow, (200,50,25,75),0)
    pygame.draw.rect(screen, red, (50,50,25,100),0)
    pygame.draw.rect(screen, yellow, (125,125,25,100),0)
    pygame.draw.rect(screen, red, (150,125,75,25),0)
    pygame.draw.rect(screen, yellow, (275,0,25,25),0)
    pygame.draw.rect(screen, red, (300,0,25,50),0)
    pygame.draw.rect(screen, yellow, (300,100,25,100),0)
    pygame.draw.rect(screen, red, (200,200,25,25),0)
    pygame.draw.rect(screen, red, (150,275,25,25),0)
    pygame.draw.rect(screen, red, (50,275,25,25),0)
    #slitherin house area
    pygame.draw.rect(screen, green, (50,300,25,75),0)
    pygame.draw.rect(screen, green, (150,300,25,150),0)
    pygame.draw.rect(screen, grey, (75,350,100,25),0)
    pygame.draw.rect(screen, grey, (175,400,75,25),0)
    pygame.draw.rect(screen, grey, (50,450,25,100),0)
    pygame.draw.rect(screen, green, (75,525,75,25),0)
    pygame.draw.rect(screen, grey, (150,500,25,100),0)
    pygame.draw.rect(screen, grey, (225,500,25,50),0)
    pygame.draw.rect(screen, grey, (150,500,25,100),0)
    pygame.draw.rect(screen, green, (225,475,75,25),0)
    #ravenclaw house are
    pygame.draw.rect(screen, blue, (300,550,25,50),0)
    pygame.draw.rect(screen, blue, (300,475,50,25),0)
    pygame.draw.rect(screen, grey, (325,400,25,75),0)
    pygame.draw.rect(screen, grey, (375,500,25,50),0)
    pygame.draw.rect(screen, blue, (450,525,100,25),0)
    pygame.draw.rect(screen, grey, (525,450,25,75),0)
    pygame.draw.rect(screen, blue, (400,400,25,50),0)
    pygame.draw.rect(screen, grey, (400,375,50,25),0)
    pygame.draw.rect(screen, blue, (450,300,25,100),0)
    pygame.draw.rect(screen, grey, (475,350,75,25),0)
    pygame.draw.rect(screen, blue, (450,525,100,25),0)

#function:drawDraws
#@param:screen (int), win(boolean), x1(int),(y1)
#@return:
def drawDoors(screen,win,x1,y1):
    pygame.draw.rect(screen, red, (275,250,50,25),0)
    pygame.draw.rect(screen, yellow, (250,250,25,25),0)
    pygame.draw.rect(screen, grey, (325,250,25,25),0)
    pygame.draw.rect(screen, black, (325,275,25,50),0)
    pygame.draw.rect(screen, grey, (325,325,25,25),0)
    pygame.draw.rect(screen, blue, (275,325,50,25),0)
    pygame.draw.rect(screen, grey, (250,325,25,25),0)
    pygame.draw.rect(screen, green, (250,275,25,50),0)
    
    if win==False:
        if y1==250:
            if x1>=250 and x1<=350:
                y1=y1-15
        if y1==350:
            if x1>=250 and x1<=350:
                y1=y1-15
        if x1==250:
            if y1>=250 and y1<=350:
                x1=x1-15
        if x1==350:
            if y1>=250 and y1<=350:
                x1=x1+15
 
#function:getSideBar
#@param: screen (int), person(string),hraven(boolean),hcup(boolean),hdiary(boolean),hring(boolean), hlocket(boolean), hsnake(boolaen), hscar(boolean), a(int),b(int),c(int),d(int),e(int),f(int),g(int),h(int),i(int),j(int),k(int),l(int),m(int),n(int)
#@return:
def drawSideBar(screen,person, hraven,hcup,hdiary,hring, hlocket, hsnake, hscar, a,b,c,d,e,f,g,h,i,j,k,l,m,n ):
    pygame.draw.rect(screen, backblue, (600,0,100,600),0)
    
    pygame.draw.line(screen,Dgrey,(600,150),(700,150),3)
    pygame.draw.line(screen,Dgrey,(600,25),(700,25),3)
    pygame.draw.line(screen,Dgrey,(600,125),(700,125),3)
    pygame.draw.line(screen,Dgrey,(600,200),(700,200),3)
    #pygame.draw.line(screen,red,(600,400),(700,400),3)
    pygame.draw.line(screen,Dgrey,(600,0),(600,600),3)
    pygame.draw.line(screen,Dgrey,(700,0),(700,700),5)
    pygame.draw.line(screen,Dgrey,(600,0),(700,0),3)
    pygame.draw.line(screen,Dgrey,(600,600),(700,600),5)
    pygame.draw.line(screen,Dgrey,(600,225),(700,225),3)

    pygame.draw.rect(screen, gray, (637.5,50,25,25),0)
    pygame.draw.rect(screen, gray, (612.5,75,25,25),0)    
    pygame.draw.rect(screen, gray, (662.5,75,25,25),0)
    pygame.draw.line(screen,backblue,(649,53),(649,70),3)
    pygame.draw.line(screen,backblue,(629,87),(616,87),3)
    pygame.draw.line(screen,backblue,(667,87),(682,87),3)
    pygame.draw.polygon(screen,backblue,[[649.5,52],[643.75,58.25],[656.25,58.25],0])
    pygame.draw.polygon(screen,backblue,[[613.75,87.5],[620,81.25],[620,93.75],0])
    pygame.draw.polygon(screen,backblue,[[684.5,87.5],[678.25,81.25],[678.25,93.75],0])
    
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("COMMANDS",True,GOLD)
    screen.blit(text, [607, 5])
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("up",True,GOLD)
    screen.blit(text, [641, 27])
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("right",True,GOLD)
    screen.blit(text, [610, 99])
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("left",True,GOLD)
    screen.blit(text, [665, 99])
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("CHARACTER",True,GOLD)
    screen.blit(text, [603, 129.5])
    
    hp_image=pygame.image.load(person)
    hp_image=pygame.transform.scale(hp_image,(50,60))
    screen.blit(hp_image,(625,150))
    
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("HORCRUXES",True,GOLD)
    screen.blit(text, [604, 205])
    
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("crown",True,GOLD)
    screen.blit(text, [658.5, 242.5])
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("cup",True,GOLD)
    screen.blit(text, [658.5, 292.5])
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("diary",True,GOLD)
    screen.blit(text, [658.5, 342.5])
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("locket",True,GOLD)
    screen.blit(text, [658.5, 392.5])
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("ring",True,GOLD)
    screen.blit(text, [658.5, 442.5])
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("snake",True,GOLD)
    screen.blit(text, [658.5, 492.5])
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("Harry",True,GOLD)
    screen.blit(text, [658.5, 562.5])
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("Potter",True,GOLD)
    screen.blit(text, [658.5, 577.5])
    font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 15)
    text = font.render("BONUS",True,GOLD)
    screen.blit(text, [628.5, 537.5])
    
    if hraven==True:
        crown_image=pygame.image.load("raven copy.png")
        crown_image=pygame.transform.scale(crown_image,(30,30))
        screen.blit(crown_image,(a,b))
        crown_image=pygame.image.load("raven.png")
        crown_image=pygame.transform.scale(crown_image,(50,50))
        screen.blit(crown_image,(600,225))
    if hscar==True:
        hpscar_image=pygame.image.load("hpscar.png")
        hpscar_image=pygame.transform.scale(hpscar_image,(75,75))
        screen.blit(hpscar_image,(579.5,525))
        hpscar_image=pygame.image.load("hpscar copy.png")
        hpscar_image=pygame.transform.scale(hpscar_image,(40,40))
        screen.blit(hpscar_image,(m,n))
    if hcup==True:
        cup_image=pygame.image.load("cup copy.png")
        cup_image=pygame.transform.scale(cup_image,(30,30))
        screen.blit(cup_image,(c,d))
        cup_image=pygame.image.load("cup.png")
        cup_image=pygame.transform.scale(cup_image,(50,50))
        screen.blit(cup_image,(600,275))
    if hlocket==True:
        locket_image=pygame.image.load("locket.png")
        locket_image=pygame.transform.scale(locket_image,(50,50))
        screen.blit(locket_image,(600,375))
        locket_image=pygame.image.load("locket copy.png")
        locket_image=pygame.transform.scale(locket_image,(30,30))
        screen.blit(locket_image,(g,h))
    if hdiary==True:
        diary_image=pygame.image.load("diary.png")
        diary_image=pygame.transform.scale(diary_image,(50,50))
        screen.blit(diary_image,(605,325))
        diary_image=pygame.image.load("diary copy.png")
        diary_image=pygame.transform.scale(diary_image,(30,30))
        screen.blit(diary_image,(e,f))
    if hsnake==True:
        snake_image=pygame.image.load("snake.png")
        snake_image=pygame.transform.scale(snake_image,(50,50))
        screen.blit(snake_image,(602.5,475))
        snake_image=pygame.image.load("snake copy.png")
        snake_image=pygame.transform.scale(snake_image,(30,30))
        screen.blit(snake_image,(k,l))
    if hring==True:
        ring_image=pygame.image.load("ring.png")
        ring_image=pygame.transform.scale(ring_image,(50,50))
        screen.blit(ring_image,(600,425))
        ring_image=pygame.image.load("ring copy.png")
        ring_image=pygame.transform.scale(ring_image,(20,20))
        screen.blit(ring_image,(i,j))
    pygame.display.update()

#function:character
#@param:
#@return:person(string)
def character():
    name=False
    while name==False:
        trio=raw_input("\nPick a character from the golden trio (Harry, Ron, Hermione):")
        if trio=='harry' or trio=='Harry':
            person="hp.png"
            name=True
        elif trio=='ron' or trio=='Ron':
            person="hp ron copy.png"
            name=True
        elif trio=='hermione' or trio=='Hermione':
            person="hp hermione.png"
            name=True
        else:
            print "That is not a character of the following to choose from...\ni.e.Harry, Ron, Hermione."
            name=False
    
    return person

#function:horcruxes
#@param:screen (int), a(int),b(int),c(int),d(int),e(int),f(int),g(int),h(int),i(int),j(int),k(int),l(int),m(int),n(int)
#@return:
def horcruxes(screen,a,b,c,d,e,f,g,h,i,j,k,l,m,n):
    
    crown_image=pygame.image.load("raven.png")
    crown_image=pygame.transform.scale(crown_image,(30,30))
    screen.blit(crown_image,(a,b))
    
    cup_image=pygame.image.load("cup.png")
    cup_image=pygame.transform.scale(cup_image,(30,30))
    screen.blit(cup_image,(c,d))
    
    diary_image=pygame.image.load("diary.png")
    diary_image=pygame.transform.scale(diary_image,(30,30))
    screen.blit(diary_image,(e,f))
    
    locket_image=pygame.image.load("locket.png")
    locket_image=pygame.transform.scale(locket_image,(30,30))
    screen.blit(locket_image,(g,h))
    
    ring_image=pygame.image.load("ring.png")
    ring_image=pygame.transform.scale(ring_image,(20,20))
    screen.blit(ring_image,(i,j))
    
    snake_image=pygame.image.load("snake.png")
    snake_image=pygame.transform.scale(snake_image,(30,30))
    screen.blit(snake_image,(k,l))
    
    hpscar_image=pygame.image.load("hpscar.png")
    hpscar_image=pygame.transform.scale(hpscar_image,(40,40))
    screen.blit(hpscar_image,(m,n))

#function:points
#@param:count(string),screen(int),a(int),b(int),c(int),d(int),e(int),f(int),g(int),h(int),i(int),j(int),k(int),l(int),m(int),n(int),hraven(boolean),hcup(boolean),hdiary(boolean),hring(boolean), hlocket(boolean), hsnake(boolean), hscar(boolean)
#@return: hraven(bolean), hcup(bolean), hdiary(bolean), hring(bolean), hlocket(bolean), hsnake(bolean), hscar(bolean), win(bolean), count(int) 
def points(count, screen,a,x1,b,y1,c,d,e,f,g,h,i,j,k,l,m,n, hraven, hcup, hdiary, hring,hlocket, hsnake, hscar,win):
   
    if (a+15)==x1 and (b+10)==y1:
        count=count+1
        #print "score=",count
        hraven=True
        
    if (c+15)==x1 and (d+10)==y1:
        count=count+1
        #print "score=",count
        hcup=True

    if (e+15)==x1 and (f+10)==y1:
        count=count+1
        #print "score=",count
        hdiary=True
        
    if (g+15)==x1 and (h+10)==y1:
        count=count+1
        #print "score=",count
        hlocket=True
        
    if (i+10)==x1 and (j+10)==y1:
        count=count+1
        #print "score=",count
        hring=True
        
    if (k+15)==x1 and (l+10)==y1:
        count=count+1
        #print "score=",count
        hsnake=True
        
    if (m+25)==x1 and (n+20)==y1:
        count=count+1
        #print "score=",count
        hscar=True
    #print "Score",count  
    if count>=7:
        broom_image=pygame.image.load("broomstick.png")
        broom_image=pygame.transform.scale(broom_image,(40,40))
        screen.blit(broom_image,(280,280))
        #print "score=",count
        #win=True
        #print "win=", win
    return  hraven, hcup, hdiary, hring,hlocket, hsnake, hscar, win, count 

#function:main
#@param:
#@return:
def main():
    #bollean values
    hraven=False
    hscar=False
    hcup=False
    hlocket=False
    hdiary=False
    hsnake=False
    hring=False
    win=False
    this =True
    
    count=0
    pygame.init()
    size = (700,600) 
    screen = pygame.display.set_mode(size)
    screen.fill(white)
    pygame.display.set_caption('Harry Potter and the Maze of Horcruxes')

    print "\n                     Harry Potter and the Maze of Horcruxes \n\n\"Well, you split your soul, you see, and hide part of it in an object outside \nthe body. Then, even if ones body is attacked or destroyed, one cannot die, \nfor part of the soul remains earthbound and undamaged.But of course, existence\nin such a form\" . . . -Horace Slughorn"
    print "\nObsessed with immortality from a young age, Lord Voldemort created a series of \nHorcruxes in an effort to escape death and become immortal. Over the ensuing\nyears, using the murders of Muggles and wizards alike,he created four more \nHorcruxes.\nThese were Marvolo Gaunt's Ring, Salazar Slytherin's Locket, Helga Hufflepuff's Cup, and Rowena Ravenclaw's Diadem.He even accidentally made Harry a horcrux."
    print "\nHelp Harry and his friends collect all the horcruxes and make it back to their\nbroomsticks in time to escape. \nYour character will go under the cloak of invisability (they will be represented by a circle), so Voldemort will not suspect them...\n"
    
    #horcruxes
    pattern=random.randint(1,4)
    #CHEAT
    #pattern=5
    if pattern==1:
        a=pa_x[0]
        b=pa_y[0]
        c=pa_x[1]
        d=pa_y[1]
        e=pa_x[2]
        f=pa_y[2]
        g=pa_x[3]
        h=pa_y[3]
        i=pa_x[4]
        j=pa_y[4]
        k=pa_x[5]
        l=pa_y[5]
        m=pa_x[6]
        n=pa_y[6-10]
    if pattern==2:
        a=pb_x[0]
        b=pb_y[0]
        c=pb_x[1]
        d=pb_y[1]
        e=pb_x[2]
        f=pb_y[2]
        g=pb_x[3]
        h=pb_y[3]
        i=pb_x[4]
        j=pb_y[4]
        k=pb_x[5]
        l=pb_y[5]
        m=pb_x[6]
        n=pb_y[6-10]
    if pattern==3:
        a=pc_x[0]
        b=pc_y[0]
        c=pc_x[1]
        d=pc_y[1]
        e=pc_x[2]
        f=pc_y[2]
        g=pc_x[3]
        h=pc_y[3]
        i=pc_x[4]
        j=pc_y[4]
        k=pc_x[5]
        l=pc_y[5]
        m=pc_x[6]
        n=pc_y[6-10]
    if pattern==4:
        a=pd_x[0]
        b=pd_y[0]
        c=pd_x[1]
        d=pd_y[1]
        e=pd_x[2]
        f=pd_y[2]
        g=pd_x[3]
        h=pd_y[3]
        i=pd_x[4]
        j=pd_y[4]
        k=pd_x[5]
        l=pd_y[5]
        m=pd_x[6]
        n=pd_y[6-10]
    if pattern==5:
        a=pe_x[0]
        b=pe_y[0]
        c=pe_x[1]
        d=pe_y[1]
        e=pe_x[2]
        f=pe_y[2]
        g=pe_x[3]
        h=pe_y[3]
        i=pe_x[4]
        j=pe_y[4]
        k=pe_x[5]
        l=pe_y[5]
        m=pe_x[6]
        n=pe_y[6-10]
    
    #To see pattern option
    #print "pattern:",pattern
    

    drawMaze(screen)
    person=character()
    
    #person icon
    corner=random.randint(0,3)
    if corner==0:
        x1=15
        y1=15
    if corner==1:
        x1=550
        y1=15
    if corner==2:
        x1=25
        y1=550
    if corner==3:
        x1=550
        y1=550
    #x1=0
    #y1=0
    #To have character move
    #hp_image=pygame.image.load(person)
    #hp_image=pygame.transform.scale(hp_image,(30,30))
    #screen.blit(hp_image,(x1,y1))
    pygame.draw.circle(screen, black,(x1,y1),10,0)
    drawDoors(screen,win,x1,y1)
    drawSideBar(screen,person, hraven, hcup, hdiary, hring,hlocket, hsnake, hscar,a,b,c,d,e,f,g,h,i,j,k,l,m,n  )
    
    print "\nAre you ready? On your marks... Get set... GO!"
    
    #calling horcruxes command
    horcruxes(screen,a,b,c,d,e,f,g,h,i,j,k,l,m,n)
    click_sound=pygame.mixer.Sound("HP.ogg")
    click_sound.play()
    pygame.display.update()

    while this==True:
        for event in pygame.event.get():
            
            if event.type==QUIT:
                sys.exit()
    
            if event.type==KEYDOWN:
                if event.key==K_LEFT:
                    x1=x1-5
                    x1,y1=restriction(y1,x1)
                    points(count, screen,a,x1,b,y1,c,d,e,f,g,h,i,j,k,l,m,n,hraven, hcup, hdiary, hring,hlocket, hsnake, hscar, win)
                elif event.key==K_RIGHT:
                    x1=x1+5
                    x1,y1=restriction(y1,x1)
                    points(count, screen,a,x1,b,y1,c,d,e,f,g,h,i,j,k,l,m,n, hraven, hcup, hdiary, hring,hlocket, hsnake, hscar,win)
                elif event.key==K_UP:
                    y1=y1-5
                    x1,y1=restriction(y1,x1)
                    points(count, screen,a,x1,b,y1,c,d,e,f,g,h,i,j,k,l,m,n, hraven, hcup, hdiary, hring,hlocket, hsnake, hscar,win)
                elif event.key==K_DOWN:
                    y1=y1+5
                    x1,y1=restriction(y1,x1)
                    points(count, screen,a,x1,b,y1,c,d,e,f,g,h,i,j,k,l,m,n, hraven, hcup, hdiary, hring,hlocket, hsnake, hscar,win)
                   
                drawMaze(screen)
                drawDoors(screen,win,x1,y1)
               

                hpscar_image=pygame.image.load("hpscar.png")
                hpscar_image=pygame.transform.scale(hpscar_image,(75,75))
                screen.blit(hpscar_image,(579.5,525))
                horcruxes(screen,a,b,c,d,e,f,g,h,i,j,k,l,m,n)
                hraven, hcup, hdiary, hring,hlocket, hsnake, hscar, win, count =points(count, screen,a,x1,b,y1,c,d,e,f,g,h,i,j,k,l,m,n,hraven, hcup, hdiary, hring,hlocket, hsnake, hscar,win)
                drawSideBar(screen,person, hraven, hcup, hdiary, hring,hlocket, hsnake, hscar,a,b,c,d,e,f,g,h,i,j,k,l,m,n )
                #screen.blit(hp_image,(x1,y1))
                pygame.draw.circle(screen, black,(x1,y1),10,0)
                pygame.display.update()
                
                if win==True:
                    print "\n\nYou have now collected all of the horcruxes!\nEscape to the broom in the middle as fast as possible!!!\nGood luck!"
                    broom_image=pygame.image.load("broomstick.png")
                    broom_image=pygame.transform.scale(broom_image,(40,40))
                    screen.blit(broom_image,(280,280))
                    #pygame.display.update()
                    if x1==300 and y1==300:
                        pygame.draw.rect(screen,backblue,(0,0,700,700),0)
                        font = pygame.font.Font("/Users/samanthastinson/Library/Fonts/HARRP___.TTF", 200)
                        text = font.render("Winner!",True,GOLD)
                        screen.blit(text, [0,150])
                        this=False
                        
                    pygame.display.update()
                   
                    
                    
    
    pygame.time.delay(10000)
    pygame.quit()

if __name__ == '__main__':
    main()