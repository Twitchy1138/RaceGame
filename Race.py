import pygame, math, random
from pygame.locals import *
from sys import exit

#Initial Game Setup#
winScreen = pygame.display.set_mode((1024, 768), 0, 32)
pygame.display.set_caption("Racing")
FPSspeed = pygame.time.Clock()
pygame.init()

#Start Page Setup#
BG = pygame.image.load('StartPage.png').convert()
CircleX = [45, 237, 430, 624, 814, 140, 337, 528, 725]
CircleY = [368, 368, 368, 368, 368, 548, 548, 548, 548]
CarsX = [105, 297, 490, 684, 874, 205, 397, 588, 778]
CarsY = [408, 408, 408, 408, 408, 584, 584, 584, 584]
Circle = pygame.image.load('Circle3.png').convert_alpha()
Circle2 = pygame.image.load('Circle.png').convert_alpha()
ones = [-1, 1]
pos_neg = random.choice(ones)
imgCar = [pygame.image.load('Windows Car.png').convert_alpha(), pygame.image.load('Apple Car.png').convert_alpha(), pygame.image.load('Linux Car.png').convert_alpha(), pygame.image.load('BM Car.png').convert_alpha(), pygame.image.load('Meme Car.png').convert_alpha(), pygame.image.load('SW car.png').convert_alpha(), pygame.image.load('HP car.png').convert_alpha(), pygame.image.load('HG car.png').convert_alpha(), pygame.image.load('Triforce car.png').convert_alpha()]
StartButton = pygame.image.load('StartButton3.png').convert_alpha()
StartButton2 = pygame.image.load('StartButton2.png').convert_alpha()

#Racing Setup#
TimerPic = pygame.image.load('TimerPic.png').convert_alpha()
fntScoreFont = pygame.font.Font('Didot.ttc', 50)
c = g = direction = speed = MapPos = MapSelect = MapXDir = MapYDir = count = PlayerSpeed = Timer = Timer2 = TimerGood = Timer2Good = 0
GO = Button = EndGame = Speedup = Slowdown = TimerGo = False
MaxSpeed = 15
MaxBackSpeed = -10
MapLoc = -1024
Map = [pygame.image.load('Narrow Track Good.bmp').convert(), pygame.image.load('Mogul Medium Good.bmp').convert(), pygame.image.load('Mogul Large Good.bmp').convert(), pygame.image.load('S Bend Track Good.bmp').convert(), pygame.image.load('Curve Track Good.bmp').convert(), pygame.image.load('Cut Track Good.bmp').convert(), pygame.image.load('Island Track Good.bmp').convert(), pygame.image.load('Weaving Track Good.bmp').convert(), pygame.image.load('Curve Track Left Good.bmp').convert(), pygame.image.load('Cut Track Left Good.bmp').convert(), pygame.image.load('Mogul Medium Left Good.bmp').convert(), pygame.image.load('Cones Track Good.bmp').convert(), pygame.image.load('Figure 8 Track Good.bmp').convert()]
Track = [pygame.image.load('Finish Track Good.bmp').convert(), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), random.choice(Map), pygame.image.load('Finish Track Good 2.bmp').convert(), pygame.image.load('Finish Track Good3.bmp').convert()]
MapX = -512
MapY = [0, MapLoc*1, MapLoc*2, MapLoc*3, MapLoc*4, MapLoc*5, MapLoc*6, MapLoc*7, MapLoc*8, MapLoc*9, MapLoc*10, MapLoc*11, MapLoc*12, MapLoc*13, MapLoc*14, MapLoc*15, MapLoc*16, MapLoc*17, MapLoc*18, MapLoc*19, MapLoc*20, MapLoc*21]
Gray = (118, 118, 118)

#End Game Setup#
PlayAgainButton = pygame.image.load('PlayAgainButton.png').convert_alpha()
PlayAgainButton2 = pygame.image.load('PlayAgainButton2.png').convert_alpha()

#Start Page!#
StartPage = True
while StartPage:
    FPSspeed.tick(60)
    #Start Button#
    MouseX, MouseY = pygame.mouse.get_pos()
    if (MouseX > 430 and MouseX < 602) and (MouseY > 290 and MouseY < 350):
        Button = True
    else:
        Button = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            StartPage = False
            RunGame = False
        if event.type == MOUSEBUTTONDOWN:
            if (MouseX > 430 and MouseX < 602) and (MouseY > 290 and MouseY < 350):
                StartPage = False
                RunGame = True
            
    winScreen.blit(BG, (0,0))
    winScreen.blit(StartButton, (430, 290))
    if Button == True:
        winScreen.blit(StartButton2, (430, 290))

    #Mouseover Circle and Selection Circle#
    m = 0
    n = 8
    while (n > -1 and m == 0):
        if math.sqrt((MouseY - (CircleY[n] + 85))**2 + (MouseX - (CircleX[n] + 85))**2) < 85:
            winScreen.blit(Circle, (CircleX[n], CircleY[n]))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    c = n
            m = 1
        else:
            n -= 1

    #Rotation#
    direction += 3 * pos_neg
    rotated = pygame.transform.rotate(imgCar[n], direction)
    rect = rotated.get_rect()
    rect.center = (CarsX[n] + 25, CarsY[n] + 46)
    
    if m != 1:
        imgCar = [pygame.image.load('Windows Car.png').convert_alpha(), pygame.image.load('Apple Car.png').convert_alpha(), pygame.image.load('Linux Car.png').convert_alpha(), pygame.image.load('BM Car.png').convert_alpha(), pygame.image.load('Meme Car.png').convert_alpha(), pygame.image.load('SW car.png').convert_alpha(), pygame.image.load('HP car.png').convert_alpha(), pygame.image.load('HG car.png').convert_alpha(), pygame.image.load('Triforce car.png').convert_alpha()]
        CarsX = [105, 297, 490, 684, 874, 203, 397, 588, 786]
        CarsY = [408, 408, 408, 408, 408, 588, 588, 588, 588]
        direction = 0
        pos_neg = random.choice(ones)
    winScreen.blit(Circle2, (CircleX[c], CircleY[c]))
    
    f = 8
    while f > -1:
        if f != n:
            winScreen.blit(imgCar[f], (CarsX[f], CarsY[f]))
        elif f == n:
            winScreen.blit(rotated, rect)
        f -= 1
        
    pygame.display.update()

#Racing Time!#
rect = 465, 500
Car = imgCar[c]
while RunGame:
    FPSspeed.tick(30)
    count += 1
    if TimerGo:
        Timer += 2
    #All Keypresses#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RunGame = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if PlayerSpeed >= 0:
                        MapXDir = PlayerSpeed
                elif PlayerSpeed < 0:
                    MapXDir = -PlayerSpeed
                rotated = pygame.transform.rotate(imgCar[c], PlayerSpeed * 2)
                rect = rotated.get_rect()
                rect.center = (490, 546)
                Car = rotated
            if event.key == K_RIGHT:
                if PlayerSpeed >= 0:
                    MapXDir = -PlayerSpeed
                elif PlayerSpeed < 0:
                    MapXDir = PlayerSpeed
                rotated = pygame.transform.rotate(imgCar[c], PlayerSpeed * -2)
                rect = rotated.get_rect()
                rect.center = (490, 546)
                Car = rotated
            if event.key == pygame.K_UP and MapY[20] < 0:
                Speedup = 1
                Slowdown = 0
                MapYDir = PlayerSpeed
                TimerGo = True
            if event.key == pygame.K_DOWN:
                Speedup = 0
                Slowdown = 1
                MapYDir = PlayerSpeed
            if c == 0:
                if event.key == K_UP:
                    Car = pygame.image.load('Windows Car BS.png').convert_alpha()
            if event.key == K_ESCAPE:
                RunGame = False
                GO = True
            if event.key == K_w:
                EndBG = pygame.image.load('EndPageWin.png').convert()
                RunGame = False
                EndGame = True
            if event.key == K_l:
                EndBG = pygame.image.load('EndPageLose.png').convert()
                RunGame = False
                EndGame = True
        elif event.type == KEYUP:
            Car = imgCar[c]
            rect = 465, 500
            if event.key == pygame.K_LEFT:
                MapXDir = 0
            if event.key == pygame.K_RIGHT:
                MapXDir = 0

    if MapX > -45:
        MapXDir = 0
        MapX = -45
    elif MapX < -1020:
        MapXDir = 0
        MapX = -1020

    
    #Timer#
    if Timer == 60:
        Timer2 += 1
        Timer = 0
    if Timer < 10:
        TimerGood = "0" + str(Timer)
    else: TimerGood = Timer
    if Timer2 < 10:
        Timer2Good = "0" + str(Timer2)
    else: Timer2Good = Timer2
    TimerLabel = fntScoreFont.render(str(Timer2Good) + ":" + str(TimerGood), 1, (0, 0, 0))

    #Collision#
    if (winScreen.get_at((468, 498)) != Gray or winScreen.get_at((509, 498)) != Gray) and MapY[20] < 0:
        MaxSpeed = 8
    else: MaxSpeed = 15
    
    
    #Accelleration#
    if MapY[20] > 0:
        MaxBackSpeed = 0
        Slowdown = 1
        Speedup = 0
        TimerGo = False
    if count == 5:
        if Speedup == 1:
            PlayerSpeed += 1
        elif Slowdown == 1:
            PlayerSpeed -= 1
        count = 0
    
    if PlayerSpeed > MaxSpeed:
        PlayerSpeed = MaxSpeed
    if PlayerSpeed < MaxBackSpeed:
        PlayerSpeed = MaxBackSpeed
    MapYDir = PlayerSpeed
    if MapY[0] < 0:
        PlayerSpeed = 0

    if PlayerSpeed == 0 and MapY[20] > 0:
        if Timer2 < 50:
            EndBG = pygame.image.load('EndPageWin.png').convert()
        else: EndBG = pygame.image.load('EndPageLose.png').convert()
        RunGame = False
        EndGame = True

    
    MapX += MapXDir
    d = 21
    while d > -1:
        MapY[d] += MapYDir
        winScreen.blit(Track[d], (MapX, MapY[d]))
        d -= 1
    winScreen.blit(TimerPic, (845, 8))
    winScreen.blit(TimerLabel, (870, 8))
    winScreen.blit(Car, rect)
    pygame.display.update()

#End Game Page!#
Button = False
while EndGame:
    FPSspeed.tick(60)
    #Buttons and KeyPresses#
    MouseX, MouseY = pygame.mouse.get_pos()
    if (MouseX > 390 and MouseX < 628) and (MouseY > 485 and MouseY < 545):
        Button = True
    else:
        Button = False
    CarsX = [125, 225, 325, 425, 525, 625, 725, 825]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EndGame = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                EndGame = False
                GO = True
        if event.type == MOUSEBUTTONDOWN:
            if (MouseX > 390 and MouseX < 628) and (MouseY > 485 and MouseY < 545):
                GO = True
                EndGame = False

    winScreen.blit(EndBG, (0,0))
    winScreen.blit(PlayAgainButton, (390, 485))
    if Button == True:
        winScreen.blit(PlayAgainButton2, (390, 485))
    
    direction += 3 * pos_neg
    rotated = pygame.transform.rotate(imgCar[c], direction)
    rect = rotated.get_rect()
    rect.center = (507, 385)
    
    f = 8
    while f > -1:
        if f > c:
            winScreen.blit(imgCar[f], (CarsX[f-1], 600))
        elif f < c:
            winScreen.blit(imgCar[f], (CarsX[f], 600))
        elif f == c:
            winScreen.blit(rotated, rect)
        f -= 1    

    pygame.display.update()

pygame.quit()
if GO == True:
    exec file('Race.py')
    
