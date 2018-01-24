#x=[]
#y=[]
#xpoint=0
##line A
#for count in range(1,150):
#    xpoint=xpoint+1
#    x.append((xpoint,200))
##line B
#for count in range(1,150):
#    xpoint=xpoint+1
#    x.append((xpoint,225))
##line C
#for count in range(1,150):
#    xpoint=xpoint+1
#    x.append(xpoint)
#    y.append(200)
#print x



#horizptal line top
if y>=0 and y<=200:
    if y==50:
        if x>=50 and x<=150:
            y=y-5
        elif x>=450 and x<=600:
            y=y-5
        elif x>=200 and x<=225:
            y=y-5
    elif y==100:
        if x>=300 and x<=325:
            y=y-5
    elif y==125:
        if x>=125 and x<=250:
            y=y-5
        elif x>=450 and x<=475:
            y=y-5
    elif y==200:
        if x>=0 and x<=150:
            y=y-5
        elif x>=200 and x<=225:
            y=y-5
        elif x>=375 and x<=600:
            y=y-5
    elif y==250:
        if x>=250 and x<=350:
            y=y-5
    elif y==275:
        if x>=50 and x<=75:
            y=y-5
        elif x>=150 and x<=175:
            y=y-5
        elif x>=450 and x<=475:
            y=y-5
    elif y==350:
        if x>=50 and x<=175:
            y=y-5
        elif x>=450 and x<=600:
            y=y-5
    elif y==375:
        if x>=400 and x<=475:
            y=y-5
    elif y==400:
        if x>=150 and x<=250:
            y=y-5
        elif x>=325 and x<=350:
            y=y-5
    elif y==400:
        if x>=50 and x<=75:
            y=y-5
        elif x>=525 and x<=550:
            y=y-5
    elif y==475:
        if x>=225 and x<=350:
            y=y-5
    elif y==500:
        if x>=150 and x<=175:
            y=y-5
        elif x>=375 and x<=400:
            y=y-5
    elif y==525:
        if x>=50  and x<=175:
            y=y-5
        elif x>=450 and x<=550:
            y=y-5
    elif y==550:
        if x>=300 and x<=325:
            y=y-5
            
#horizontal line bottom
    elif y==25:
        if x>=275 and x<=300:
            y=y+5
    elif y==50:
        if x>=300 and x<=325:
            y=y+5
    elif y==75:
        if x>=50 and x<=150:
            y=y+5
        elif x>=450 and x<=550:
            y=y+5
    elif y==125:
        if x>=375 and x<=400:
            y=y+5
    elif y==150:
        if x>=50 and x<=75:
            y=y+5
        elif x>=125 and x<=225:
            y=y+5
        elif X>=450 and x<=475:
            y=y+5
        elif x>=525 and x<=550:
            y=y+5
    elif y==200:
        if x>=300 and x<=325:
            y=y+5
    elif y==225:
        if x>=0 and x<=150:
            y=y+5
        elif x<=200 and x>=225:
            y=y+5
        elif x>=375 and x<=600:
            y=y+5
    elif y==300:
        if x>=525 and x<=550:
            y=y+5
    elif y==350:
        if x>=250 and x<=350:
            y=y+5
    elif y==375:
        if x>=50 and x<=175:
            y=y+5
        elif x>=450 and x<=550:
            y=y+5
    elif y==400:
        if x>=400 and x<=450:
            y=y+5
    elif y==425:
        if x>=150 and x<=250:
            y=y+5
    elif y==450:
        if x>=150 and x<=175:
            y=y+5
        elif x>=400 and x<=425:
            y=y+5
    elif y==500:
        if x>=225 and x<=350:
            y=y+5
    elif y==550:
        if x>=50 and x<=175:
            y=y+5
        elif x>=225 and x<=250:
            y=y+5
        elif x>=375 and x<=400:
            y=y+5
        elif x>=400 and x<=550:
            y=y+5
#left side of lines
if x<=0 and x<=600:
    if x==50:
        if y>=50 and y<=150:
            x=x-5
        elif y>=275 and y<=375:
            x=x-5
        elif  y>=450 and y<=550:
            x=x-5
    elif x==125:
        if y>=125 and y<=225:
            x=x-5
    elif x==150:
        if y>=275 and y<=450:
            x=x-5
        elif y>=500 and y<=600:
            x=x-5
    elif x==200:
        if y>=50 and y<=150:
            x=x-5
        elif y>=200 and y<=225:
            x=x-5
    elif x==225:
        if y>=475 and y<=550:
            x=x-5
    elif x==250:
        if y>=250 and y<=350:
            x=x-5
    elif x==275:
        if y>=0 and y<=25:
            x=x-5
    elif x==300:
        if y>=0 and y<=50:
            x=x-5
        elif y>=100 and y<=200:
            x=x-5
        elif y>=550 and y<=600:
            x=x-5
    elif x==325:
        if y>=400 and y<=500:
            x=x-5
    elif x==375:
        if y>=0 and y<=125:
            x=x-5
        elif y>=200 and y<=225:
            x=x-5
        elif y>=500 and y<=550:
            x=x-5
    elif x==400:
        if y>=375 and y<=450:
            x=x-5
    elif x==450:
        if y>=50 and y<=75:
            x=x-5
        elif y<=125 and y<=150:
            x=x-5
        elif y>=275 and y<=400:
            x=x-5
        elif y>=525 and y<=550:
            x=x-5
    elif x==525:
        if y>=50 and y<=150:
            x=x-5
        elif y>=200 and y<=300:
            x=x-5
        elif y>=450 and y<=550:
            x=x-5
    elif x==600:
        x=x-5
#right side of lines
    elif x==75:
        if y>=50 and y<=150:
            x=x+5
        elif y>=275 and y<=375:
            x=x+5
        elif y>=450 and y<=550:
            x=x+5
    elif x==150:
        if y>=50 and y<=75:
            x=x+5
        elif y>=125 and y<=225:
            x=x+5
    elif x==175:
        if y>=275 and y<=450:
            x=x+5
        elif y>=500 and y<=600:
            x=x+5
    elif x==225:
        if y>=50 and y<=150:
            x=x+5
        elif y>=200 and y<=225:
            x=x+5
    elif x==250:
        if y>=400 and y<=425:
            x=x+5
        elif y>=475 and y<=550:
            x=x+5
    elif x==300:
        if y>=0 and y<=25:
            x=x+5
    elif x==325:
        if y>=0 and y<=50:
            x=x+5
        elif y>=100 and y<=200:
            x=x+5
        elif y>=550 and y<=600:
            x=x+5
    elif x==350:
        if y>=250 and y<=350:
            x=x+5
        elif y>=400 and y<=500:
            x=x+5
    elif x==400:
        if y>=0 and y<=125:
            x=x+5
        elif y>=500 and y<=550:
            x=x+5
    elif x==425:
        if y>=375 and y<=450:
            x=x+5
    elif x==475:
        if y>=125 and y<=150:
            x=x+5
        elif y>=275 and y<=400:
            x=x+5
    elif x==550:
        if y>=50 and y<=150:
            x=x+5
        elif y>=200 and y<=300:
            x=x+5
        elif y>=350 and y<=375:
            x=x+5
        elif y>=450 and y<=550:
            x=x+5
