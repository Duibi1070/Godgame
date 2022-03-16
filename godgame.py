#30918蔡明蓁
#30924張量鈞
'''
迷宮模式:撿到鑰匙可以開寶箱，打開寶箱得到的翅膀和武器可以提升玩家的移動速度和攻擊速度，撞到怪物進入戰鬥，
只要死掉就要重頭玩，進入BOSS房間並打倒BOSS便通關

PVE模式:打倒怪物就能進入下一等級，怪物的難度隨著等級提升，死掉可以同一關重玩，打完25等就通關

PVP模式:兩個玩家對打
'''


import pygame, random, sys, time
from pygame.locals import *

#設定常數

WINDOWWIDTH = 800 #視窗寬
WINDOWHEIGHT = 600 #視窗長
FPS = 100

goflag = False

modetype = 0

playertime = 0
playerlife = 10

player1life = 10
player2life = 10

playersize = 60 #玩家物件大小
playerspeed = 2 #玩家速度

addattackrate = 40
attackspeed = 3.5

attackdesx = 0
attackdesy = 0
attacksize = 12

addattack2rate = 75#怪物攻擊
attack2speed = 2
attack2size = 12

bosstime = 0
monsterlife = 10
monsterspeed = 2

level = 1


#設定影像物件

PVE = pygame.image.load('PVE.png')
PVERect = pygame.Rect(150, 410, 200, 100)

PVP = pygame.image.load('PVP.png')
PVPRect = pygame.Rect(450, 410, 200, 100)

MAZE = pygame.image.load('maze.png')
MAZERect = pygame.Rect(240, 220, 320, 160)

knimage = pygame.image.load('knface1.png')
knimage = pygame.transform.scale(knimage, (150, 150))
knRect = pygame.Rect(25, 300, 150, 150)

kzimage = pygame.image.load('kzface1.png')
kzimage = pygame.transform.scale(kzimage, (150, 150))
kzRect = pygame.Rect(225, 300, 150, 150)

knsgimage = pygame.image.load('knsgface1.png')
knsgimage = pygame.transform.scale(knsgimage, (150, 150))
knsgRect = pygame.Rect(425, 300, 150, 150)

snyaimage = pygame.image.load('snyaface1.png')
snyaimage = pygame.transform.scale(snyaimage, (150, 150))
snyaRect = pygame.Rect(625, 300, 150, 150)

player1image = pygame.image.load('htknface1.png')
player1Rect = player1image.get_rect()

player2image = pygame.image.load('htkzface1.png')
player2Rect = player2image.get_rect()

bgmode = pygame.image.load('bgmode.png')
bggame = pygame.image.load('bggame.png')
bgchar = pygame.image.load('bgchar.png')
bgstart1 = pygame.image.load('bgstart1.png')
bgstart2 = pygame.image.load('bgstart2.png')
bgstart3 = pygame.image.load('bgstart3.png')
bggameover = pygame.image.load('bggameover.png')
bgnextlevel = pygame.image.load('bgnextlevel.png')
bg1pwin = pygame.image.load('bg1pwin.png')
bg2pwin = pygame.image.load('bg2pwin.png')
bgdraw = pygame.image.load('bgdraw.png')
bgclear = pygame.image.load('bgclear.png')
bgmap = pygame.image.load('map.png')
mapRect = bgmap.get_rect()
bgbossroute = pygame.image.load('bossroute.png')
bgbossroom = pygame.image.load('bossroom.png')
bgmazewin = pygame.image.load('mazewin.png')


start = pygame.image.load('start.png')
startRect = pygame.Rect(285, 425, 230, 80)

go = pygame.image.load('go.png')
goRect = pygame.Rect(270, 300, 260, 160)

againimage = pygame.image.load('again.png')
againRect = pygame.Rect(262, 400, 276, 96)

homeimage = pygame.image.load('home.png')
homeRect = pygame.Rect(340, 530, 120, 48)

homesmall = pygame.transform.scale(homeimage,(80, 32))
homesmallRect = pygame.Rect(710, 14, 80, 32)

mouse = pygame.image.load('mouse.png')
mouseRect = mouse.get_rect()

attackimage = pygame.image.load('attack.png')
attack2image = pygame.image.load('attack2.png')

choose = pygame.image.load('choose.png')

heartleft = pygame.image.load('heartleft.png')
heartleftRect = heartleft.get_rect()
heartright = pygame.image.load('heartright.png')
heartrightRect = heartright.get_rect()

bossheart1 = pygame.image.load('bossheart1.png')
bossheart1Rect = bossheart1.get_rect()
bossheart2 = pygame.image.load('bossheart2.png')
bossheart2Rect = bossheart2.get_rect()
bossheart3 = pygame.image.load('bossheart3.png')
bossheart3Rect = bossheart3.get_rect()
bossheart4 = pygame.image.load('bossheart4.png')
bossheart4Rect = bossheart4.get_rect()


levelRect = pygame.Rect(325, 10, 150, 40)

levelimage = [pygame.image.load('level1.png'),
              pygame.image.load('level2.png'),
              pygame.image.load('level3.png'),
              pygame.image.load('level4.png'),
              pygame.image.load('level5.png'),
              pygame.image.load('level6.png'),
              pygame.image.load('level7.png'),
              pygame.image.load('level8.png'),
              pygame.image.load('level9.png'),
              pygame.image.load('level10.png'),
              pygame.image.load('level11.png'),
              pygame.image.load('level12.png'),
              pygame.image.load('level13.png'),
              pygame.image.load('level14.png'),
              pygame.image.load('level15.png'),
              pygame.image.load('level16.png'),
              pygame.image.load('level17.png'),
              pygame.image.load('level18.png'),
              pygame.image.load('level19.png'),
              pygame.image.load('level20.png'),
              pygame.image.load('level21.png'),
              pygame.image.load('level22.png'),
              pygame.image.load('level23.png'),
              pygame.image.load('level24.png'),
              pygame.image.load('level25.png'),]


#設定音效



#定義函式

def terminate():#程式結束
    pygame.quit()
    sys.exit()

def choosemode():#選模式

    windowSurface.blit(bgmode, (0, 0))
    windowSurface.blit(PVE, PVERect)
    windowSurface.blit(PVP, PVPRect)
    windowSurface.blit(MAZE, MAZERect)
    pygame.display.update()

    goflagmode = False

    global modetype
    
    while goflagmode == False:

        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

            if event.type == MOUSEMOTION:
                mouseRect.centerx = event.pos[0]
                mouseRect.centery = event.pos[1]

            if event.type == MOUSEBUTTONDOWN:

                if mouseRect.colliderect(PVERect):
                    modetype = 1

                if mouseRect.colliderect(PVPRect):
                    modetype = 2

                if mouseRect.colliderect(MAZERect):
                    modetype = 3

            if event.type == MOUSEBUTTONUP and modetype == 1:
                goflagmode = True

            if event.type == MOUSEBUTTONUP and modetype == 2:
                goflagmode = True

            if event.type == MOUSEBUTTONUP and modetype == 3:
                goflagmode = True

def choosechar():#選角色

    windowSurface.blit(bgchar, (0, 0))
    windowSurface.blit(knimage, knRect)
    windowSurface.blit(kzimage, kzRect)
    windowSurface.blit(knsgimage, knsgRect)
    windowSurface.blit(snyaimage, snyaRect)
    pygame.display.update()
    
    global playerface1
    global playerface2
    global playerleft1
    global playerleft2
    global playerright1
    global playerright2
    global playerback1
    global playerback2
    
    goflagchar = False
    onchar = False

    chooseRect = choose.get_rect()
    
    while goflagchar == False:
        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

            if event.type == MOUSEMOTION:
                mouseRect.centerx = event.pos[0]
                mouseRect.centery = event.pos[1]

            if  event.type == MOUSEBUTTONDOWN:
                if mouseRect.colliderect(knRect):
                    onchar = True
                    chooseRect = (21, 296, 158, 158)
                    playerface1 = 'knface1.png'
                    playerface2 = 'knface2.png'
                    playerleft1 = 'knleft1.png'
                    playerleft2 = 'knleft2.png'
                    playerright1 = 'knright1.png'
                    playerright2 = 'knright2.png'
                    playerback1 = 'knback1.png'
                    playerback2 = 'knback2.png'
                    windowSurface.blit(choose, chooseRect)
                    pygame.display.update()

                if mouseRect.colliderect(kzRect):
                    onchar = True
                    chooseRect = (221, 296, 158, 158)
                    playerface1 = 'kzface1.png'
                    playerface2 = 'kzface2.png'
                    playerleft1 = 'kzleft1.png'
                    playerleft2 = 'kzleft2.png'
                    playerright1 = 'kzright1.png'
                    playerright2 = 'kzright2.png'
                    playerback1 = 'kzback1.png'
                    playerback2 = 'kzback2.png'
                    windowSurface.blit(choose, chooseRect)
                    pygame.display.update()

                if mouseRect.colliderect(knsgRect):
                    onchar = True
                    chooseRect = (421, 296, 158, 158)
                    playerface1 = 'knsgface1.png'
                    playerface2 = 'knsgface2.png'
                    playerleft1 = 'knsgleft1.png'
                    playerleft2 = 'knsgleft2.png'
                    playerright1 = 'knsgright1.png'
                    playerright2 = 'knsgright2.png'
                    playerback1 = 'knsgback1.png'
                    playerback2 = 'knsgback2.png'
                    windowSurface.blit(choose, chooseRect)
                    pygame.display.update()

                if mouseRect.colliderect(snyaRect):
                    onchar = True
                    chooseRect = (621, 296, 158, 158)
                    playerface1 = 'snyaface1.png'
                    playerface2 = 'snyaface2.png'
                    playerleft1 = 'snyaleft1.png'
                    playerleft2 = 'snyaleft2.png'
                    playerright1 = 'snyaright1.png'
                    playerright2 = 'snyaright2.png'
                    playerback1 = 'snyaback1.png'
                    playerback2 = 'snyaback2.png'
                    windowSurface.blit(choose, chooseRect)
                    pygame.display.update()


            if event.type == MOUSEBUTTONUP and onchar == True:
                goflagchar = True



def startmode1():#按開始1
    windowSurface.blit(bgstart1, (0, 0))
    windowSurface.blit(start,startRect)

    charimage = pygame.image.load(playerright1)
    charimage = pygame.transform.scale(charimage,(250, 250))
    windowSurface.blit(charimage,(75,100))
    
    pygame.display.update()

    goflagstart1 = False
    onstart1 = False

    while goflagstart1 == False:

        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

            if event.type == MOUSEMOTION:
                mouseRect.centerx = event.pos[0]
                mouseRect.centery = event.pos[1]

            if  event.type == MOUSEBUTTONDOWN:
                if mouseRect.colliderect(startRect):
                    onstart1 = True

            if event.type == MOUSEBUTTONUP and onstart1 == True:
                goflagstart1 = True

def startmode2():#按開始2
    windowSurface.blit(bgstart2, (0, 0))
    windowSurface.blit(pygame.transform.scale(start,(184, 64)), pygame.Rect(330, 320, 184, 64))

    image1P = pygame.image.load('htknright1.png')
    image2P = pygame.image.load('htkzleft2.png')

    image1P = pygame.transform.scale(image1P,(200, 200))
    image2P = pygame.transform.scale(image2P,(200, 200))

    windowSurface.blit(image1P, (75, 150))
    windowSurface.blit(image2P, (525, 150))
    
    pygame.display.update()

    goflagstart2 = False
    onstart2 = False

    while goflagstart2 == False:

        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

            if event.type == MOUSEMOTION:
                mouseRect.centerx = event.pos[0]
                mouseRect.centery = event.pos[1]

            if  event.type == MOUSEBUTTONDOWN:
                if mouseRect.colliderect(pygame.Rect(330, 320, 184, 64)):
                    onstart2 = True

            if event.type == MOUSEBUTTONUP and onstart2 == True:
                goflagstart2 = True

def startmode3():#按開始3
    windowSurface.blit(bgstart3, (0, 0))
    windowSurface.blit(start,startRect)

    charimage = pygame.image.load(playerright1)
    charimage = pygame.transform.scale(charimage,(250, 250))
    windowSurface.blit(charimage,(75, 100))
    
    pygame.display.update()

    goflagstart3 = False
    onstart3 = False

    while goflagstart3 == False:

        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

            if event.type == MOUSEMOTION:
                mouseRect.centerx = event.pos[0]
                mouseRect.centery = event.pos[1]

            if  event.type == MOUSEBUTTONDOWN:
                if mouseRect.colliderect(startRect):
                    onstart3 = True

            if event.type == MOUSEBUTTONUP and onstart3 == True:
                goflagstart3 = True

def gonextlevel():

    global modetype
    global monsterspeed
    global addattack2rate
    global attack2speed
    global level
    
    time = 0        

    goflaggo = False
    ongo = False

    goflaghome = False
    onhome = False

    while goflaggo == False and goflaghome == False:
        
        time += 1
        mainClock.tick(FPS)

        if time > 100:
            windowSurface.blit(go, goRect)
            windowSurface.blit(homeimage, homeRect)
            pygame.display.update()
            
        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

            if event.type == MOUSEMOTION:
                mouseRect.centerx = event.pos[0]
                mouseRect.centery = event.pos[1]

            if  event.type == MOUSEBUTTONDOWN and time > 100:

                if mouseRect.colliderect(goRect):
                    ongo = True

                if mouseRect.colliderect(homeRect):
                    onhome = True
                    
            if event.type == MOUSEBUTTONUP and time > 100:

                if ongo == True:

                    monsterspeed += 0.02
                    addattack2rate -= 3
                    attack2speed += 0.2
                    level += 1

                    goflaggo = True

                if onhome == True:
                    modetype = 0
                    goflaghome = True

def again():
    
    global modetype
        
    time = 0

    goflagagain = False
    onagain = False

    goflaghome = False
    onhome = False

    while goflagagain == False and goflaghome == False:

        time += 1
        mainClock.tick(FPS)

        if time > 100:
            windowSurface.blit(againimage, againRect)
            windowSurface.blit(homeimage, homeRect)
            pygame.display.update()

        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

            if event.type == MOUSEMOTION:
                mouseRect.centerx = event.pos[0]
                mouseRect.centery = event.pos[1]

            if  event.type == MOUSEBUTTONDOWN and time > 100:

                if mouseRect.colliderect(againRect):
                    onagain = True

                if mouseRect.colliderect(homeRect):
                    onhome = True
                    
            if event.type == MOUSEBUTTONUP and time > 100:

                if onagain == True:
                    goflagagain = True

                if onhome == True:
                    modetype = 0
                    goflaghome = True

def home():
    
    global modetype
        
    time = 0

    goflaghome = False
    onhome = False

    while goflaghome == False:

        time += 1
        mainClock.tick(FPS)

        if time > 100:
            windowSurface.blit(homeimage, homeRect)
            pygame.display.update()

        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

            if event.type == MOUSEMOTION:
                mouseRect.centerx = event.pos[0]
                mouseRect.centery = event.pos[1]

            if  event.type == MOUSEBUTTONDOWN and time > 100:

                if mouseRect.colliderect(homeRect):
                    onhome = True
                    
            if event.type == MOUSEBUTTONUP and time > 100:

                if onhome == True:
                    modetype = 0
                    goflaghome = True     

def vector(desx, desy, playerx, playery, attackspeed):

    x = desx - playerx
    y = desy - playery

    
    tt = ((x**2) + (y**2))/(attackspeed**2)
    rx = ((x**2)/tt)**(0.5)
    ry = ((y**2)/tt)**(0.5)

    if x < 0:
        rx = -1 * rx

    if y < 0:
        ry = -1 * ry

    return (rx, ry)    
    

#初始化pygame和設定視窗

pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('神作')

while True:
    #選mode

    choosemode()

    #mode1選角色& START
    if modetype == 1:
        
        choosechar()

        playerimage = pygame.image.load(playerface1)
        playerRect = playerimage.get_rect()

        monsterspeed = 2
        addattack2rate = 75
        attack2speed = 3
        level = 1

        startmode1()

    #mode2START
    if modetype == 2:

        startmode2()

    #mode3選角色& START
    if modetype == 3:

        choosechar()

        playerimage = pygame.image.load(playerface1)
        playerRect = playerimage.get_rect()

        startmode3()


    #主程式mode1
    while modetype == 1:

        moveUp = moveDown = moveLeft = moveRight = False

        attack = []#攻擊物件串列
        cooltime = addattackrate
        attackflag = False

        attack2 = []
        attack2counter = 0

        monsterimage = pygame.image.load('bossface1.png')
        monsterRect = monsterimage.get_rect()


        playerRect.topleft = (100, 270)#玩家起始位置
        monsterRect.topleft = (640, 270)#怪物起始位置

        playerlife = 10
        monsterlife = 10
        playerspeed = 2
        addattackrate = 40
        attackspeed = 3.5


        while playerlife > 0 and monsterlife > 0: #生命值大於0

            playertime += 1
            if playertime > 40:
                playertime = 0

            bosstime += 1
            if bosstime > 40:
                bosstime = 0

            if cooltime < addattackrate:
                cooltime += 1

            #偵測事件
            for event in pygame.event.get():
                if event.type == QUIT:#關閉視窗
                    terminate()

                #鍵盤移動
                if event.type == KEYDOWN:

                    if event.key == K_w:#上
                        moveUp = True

                    if event.key == K_a:#左
                        moveLeft = True

                    if event.key == K_s:#下
                        moveDown = True

                    if event.key == K_d:#右
                        moveRight = True

                if event.type == KEYUP:
                    
                    if event.key == K_w:#上
                        moveUp = False

                    if event.key == K_a:#左
                        moveLeft = False

                    if event.key == K_s:#下
                        moveDown = False

                    if event.key == K_d:#右
                        moveRight = False

                    if event.key == K_ESCAPE:#ESC
                        terminate()

                #滑鼠
                if event.type == MOUSEMOTION:
                    mouseRect.centerx = event.pos[0]
                    mouseRect.centery = event.pos[1]

                if event.type == MOUSEBUTTONDOWN:
                    attackdesx = event.pos[0]
                    attackdesy = event.pos[1]

                    if cooltime == addattackrate:

                        newattack = {'rect' : pygame.Rect(playerRect.centerx, playerRect.centery, attacksize, attacksize),
                                     'speed' : (vector(attackdesx, attackdesy, playerRect.centerx, playerRect.centery, attackspeed))}

                        attack.append(newattack)

                        cooltime = 0                        


            #偵測結束，移動玩家，換圖片
            if moveLeft and playerRect.left > 0:
                playerRect.move_ip(-1*playerspeed, 0)

                if playertime > 20:
                    playerimage = pygame.image.load(playerleft1)
                else:
                    playerimage = pygame.image.load(playerleft2)

            if moveRight and playerRect.right < WINDOWWIDTH:
                playerRect.move_ip(playerspeed, 0)

                if playertime > 20:
                    playerimage = pygame.image.load(playerright1)
                else:
                    playerimage = pygame.image.load(playerright2)

            if moveUp and playerRect.top > 60:
                playerRect.move_ip(0, -1*playerspeed)

                if playertime > 20:
                    playerimage = pygame.image.load(playerback1)
                else:
                    playerimage = pygame.image.load(playerback2)

            if moveDown and playerRect.bottom < WINDOWHEIGHT:
                playerRect.move_ip(0, playerspeed)

                if playertime > 20:
                    playerimage = pygame.image.load(playerface1)
                else:
                    playerimage = pygame.image.load(playerface2)

            #新增攻擊
            for a in attack:
                a['rect'].move_ip(a['speed'])

            for a in attack:
                if a['rect'].colliderect(monsterRect):
                    monsterlife -= 1
                    attack.remove(a)

                if a['rect'].top > WINDOWHEIGHT or a['rect'].bottom < (60 + attacksize) or a['rect'].right < 0 or a['rect'].left > WINDOWWIDTH:
                    attack.remove(a)

            #怪物移動
            monsterRect.move_ip(vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, monsterspeed))

            rx = vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, monsterspeed)[0]
            ry = vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, monsterspeed)[1]
            if rx > 0:
                if bosstime > 20:
                    monsterimage = pygame.image.load('bossright1.png')
                else:
                    monsterimage = pygame.image.load('bossright2.png')
            if rx < 0:
                if bosstime > 20:
                    monsterimage = pygame.image.load('bossleft1.png')
                else:
                    monsterimage = pygame.image.load('bossleft2.png')
            if ry > 0 and rx < monsterspeed**(0.5) and rx > -1*monsterspeed**(0.5):
                if bosstime > 20:
                    monsterimage = pygame.image.load('bossface1.png')
                else:
                    monsterimage = pygame.image.load('bossface2.png')
            if ry < 0 and rx < monsterspeed**(0.5) and rx > -1*monsterspeed**(0.5):
                if bosstime > 20:
                    monsterimage = pygame.image.load('bossback1.png')
                else:
                    monsterimage = pygame.image.load('bossback2.png')

            #怪物攻擊
            attack2counter += 1
            if attack2counter == addattack2rate:
                attack2counter = 0
                newattack2 = {'rect' : pygame.Rect(monsterRect.centerx, monsterRect.centery, attacksize, attacksize),
                                'speed' : (vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, attack2speed))}

                attack2.append(newattack2)

            for a2 in attack2:
                a2['rect'].move_ip(a2['speed'])
                      
            for a2 in attack2:
                if a2['rect'].colliderect(playerRect):
                    playerlife -= 1
                    attack2.remove(a2)

                if a2['rect'].top > WINDOWHEIGHT or a2['rect'].bottom < (60 + attack2size) or a2['rect'].right < 0 or a2['rect'].left > WINDOWWIDTH:
                    attack2.remove(a2)

            #怪物撞擊
            if monsterRect.colliderect(playerRect):
                playerlife -= 1
                monsterRect.move_ip(-25*vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, monsterspeed)[0],
                                    -25*vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, monsterspeed)[1])

                    
            
            #繪製物件
            windowSurface.blit(bggame,(0,0))

            for a in attack:
                windowSurface.blit(attackimage, a['rect'])

            for a2 in attack2:
                windowSurface.blit(attack2image, a2['rect'])

            for h1 in range(0, playerlife):

                if h1 % 2 == 0:
                    heartleftRect = (10 + (60*(h1//2)), 10, 44, 40)
                    windowSurface.blit(heartleft, heartleftRect)

                if h1 % 2 == 1:
                    heartrightRect = (10 + (60*(h1//2)), 10, 44, 40)
                    windowSurface.blit(heartright, heartrightRect)

            for h2 in range(0, monsterlife):
                
                if h2 % 2 == 0:
                    heartrightRect = (746 - (60*(h2//2)), 10, 44, 40)
                    windowSurface.blit(heartright, heartrightRect)

                if h2 % 2 == 1:
                    heartleftRect = (746 - (60*(h2//2)), 10, 44, 40)
                    windowSurface.blit(heartleft, heartleftRect)

            
            windowSurface.blit(levelimage[level-1], levelRect)
            windowSurface.blit(playerimage, playerRect)
            windowSurface.blit(monsterimage, monsterRect)
            pygame.display.update()
            mainClock.tick(FPS)

        #Clear
        if playerlife > 0 and level == 25:

            windowSurface.blit(bgclear, (0, 0))
            pygame.display.update()

            home()

            break

        #Level Up
        if playerlife > 0:

            windowSurface.blit(bgnextlevel, (0, 0))
            pygame.display.update()

            gonextlevel()

        #Play Again
        if playerlife == 0 :

            windowSurface.blit(bggameover, (0, 0))
            pygame.display.update()
            
            again()   
            


    #主程式mode2
    while modetype == 2:

        moveUp1 = moveDown1 = moveLeft1 = moveRight1 = False
        moveUp2 = moveDown2 = moveLeft2 = moveRight2 = False

        attack1 = []
        cooltime1 = addattackrate
        attack1flag = False

        attack2 = []
        cooltime2 = addattackrate
        attack2flag = False

        player1Rect.topleft = (100, 270)#玩家1起始位置
        player2Rect.topleft = (620, 260)#玩家2起始位置

        player1life = 10
        player2life = 10
        playerspeed = 2
        addattackrate = 40
        attackspeed = 3.5

        while player1life > 0 and player2life > 0:

            playertime += 1
            if playertime > 40:
                playertime = 0

            if cooltime1 < addattackrate:
                cooltime1 += 1

            if cooltime2 < addattackrate:
                cooltime2 += 1

            #偵測事件
            for event in pygame.event.get():
                if event.type == QUIT:#關閉視窗
                    terminate()

                #鍵盤控制
                if event.type == KEYDOWN:

                    if event.key == K_w:#1P上
                        moveUp1 = True

                    if event.key == K_a:#1P左
                        moveLeft1 = True

                    if event.key == K_s:#1P下
                        moveDown1 = True

                    if event.key == K_d:#1P右
                        moveRight1 = True

                    if event.key == K_UP:#2P上
                        moveUp2 = True

                    if event.key == K_LEFT:#2P左
                        moveLeft2 = True

                    if event.key == K_DOWN:#2P下
                        moveDown2 = True

                    if event.key == K_RIGHT:#2P右
                        moveRight2 = True

                    if event.key == K_g:#1P攻擊

                        if cooltime1 == addattackrate:

                            newattack1 = {'rect' : pygame.Rect(player1Rect.centerx, player1Rect.centery, attacksize, attacksize),
                                            'speed' : (vector(player2Rect.centerx, player2Rect.centery, player1Rect.centerx, player1Rect.centery, attackspeed))}

                            attack1.append(newattack1)

                            cooltime1 = 0

                    if event.key == K_KP_ENTER:#2P攻擊

                        if cooltime2 == addattackrate:

                            newattack2 = {'rect' : pygame.Rect(player2Rect.centerx, player2Rect.centery, attacksize, attacksize),
                                            'speed' : (vector(player1Rect.centerx, player1Rect.centery, player2Rect.centerx, player2Rect.centery, attackspeed))}

                            attack2.append(newattack2)

                            cooltime2 = 0                    

                if event.type == KEYUP:
                    
                    if event.key == K_w:#1P上
                        moveUp1 = False

                    if event.key == K_a:#1P左
                        moveLeft1 = False

                    if event.key == K_s:#1P下
                        moveDown1 = False

                    if event.key == K_d:#1P右
                        moveRight1 = False

                    if event.key == K_UP:#2P上
                        moveUp2 = False

                    if event.key == K_LEFT:#2P左
                        moveLeft2 = False

                    if event.key == K_DOWN:#2P下
                        moveDown2 = False

                    if event.key == K_RIGHT:#2P右
                        moveRight2 = False                        

                    if event.key == K_ESCAPE:#ESC
                        terminate()


            #1P移動
            if moveLeft1 and player1Rect.left > 0:
                player1Rect.move_ip(-1*playerspeed, 0)

                if playertime > 20:
                    player1image = pygame.image.load('htknleft1.png')
                else:
                    player1image = pygame.image.load('htknleft2.png')

            if moveRight1 and player1Rect.right < WINDOWWIDTH:
                player1Rect.move_ip(playerspeed, 0)

                if playertime > 20:
                    player1image = pygame.image.load('htknright1.png')
                else:
                    player1image = pygame.image.load('htknright2.png')

            if moveUp1 and player1Rect.top > 60:
                player1Rect.move_ip(0, -1*playerspeed)

                if playertime > 20:
                    player1image = pygame.image.load('htknback1.png')
                else:
                    player1image = pygame.image.load('htknback2.png')

            if moveDown1 and player1Rect.bottom < WINDOWHEIGHT:
                player1Rect.move_ip(0, playerspeed)

                if playertime > 20:
                    player1image = pygame.image.load('htknface1.png')
                else:
                    player1image = pygame.image.load('htknface2.png')

            #2P移動
            if moveLeft2 and player2Rect.left > 0:
                player2Rect.move_ip(-1*playerspeed, 0)

                if playertime > 20:
                    player2image = pygame.image.load('htkzleft1.png')
                else:
                    player2image = pygame.image.load('htkzleft2.png')

            if moveRight2 and player2Rect.right < WINDOWWIDTH:
                player2Rect.move_ip(playerspeed, 0)

                if playertime > 20:
                    player2image = pygame.image.load('htkzright1.png')
                else:
                    player2image = pygame.image.load('htkzright2.png')

            if moveUp2 and player2Rect.top > 60:
                player2Rect.move_ip(0, -1*playerspeed)

                if playertime > 20:
                    player2image = pygame.image.load('htkzback1.png')
                else:
                    player2image = pygame.image.load('htkzback2.png')

            if moveDown2 and player2Rect.bottom < WINDOWHEIGHT:
                player2Rect.move_ip(0, playerspeed)

                if playertime > 20:
                    player2image = pygame.image.load('htkzface1.png')
                else:
                    player2image = pygame.image.load('htkzface2.png')

            #新增1P攻擊
            for a1 in attack1:
                a1['rect'].move_ip(a1['speed'])

            for a1 in attack1:
                if a1['rect'].colliderect(player2Rect):
                    player2life -= 1
                    attack1.remove(a1)

                if a1['rect'].top > WINDOWHEIGHT or a1['rect'].bottom < (60 + attacksize) or a1['rect'].right < 0 or a1['rect'].left > WINDOWWIDTH:
                    attack1.remove(a1)

            #新增2P攻擊
            for a2 in attack2:
                a2['rect'].move_ip(a2['speed'])

            for a2 in attack2:
                if a2['rect'].colliderect(player1Rect):
                    player1life -= 1
                    attack2.remove(a2)

                if a2['rect'].top > WINDOWHEIGHT or a2['rect'].bottom < (60 + attacksize) or a2['rect'].right < 0 or a2['rect'].left > WINDOWWIDTH:
                    attack2.remove(a2)

            #撞擊
            if player1Rect.colliderect(player2Rect):

                player1life -= 1
                player2life -= 1
                
                player1Rect.move_ip(-15*vector(player2Rect.centerx, player2Rect.centery, player1Rect.centerx, player1Rect.centery, playerspeed)[0],
                                    -15*vector(player2Rect.centerx, player2Rect.centery, player1Rect.centerx, player1Rect.centery, playerspeed)[1])

                player2Rect.move_ip(-15*vector(player1Rect.centerx, player1Rect.centery, player2Rect.centerx, player2Rect.centery, playerspeed)[0],
                                    -15*vector(player1Rect.centerx, player1Rect.centery, player2Rect.centerx, player2Rect.centery, playerspeed)[1])

            #繪製物件
            windowSurface.blit(bggame,(0,0))

            for a1 in attack1:
                windowSurface.blit(attackimage, a1['rect'])

            for a2 in attack2:
                windowSurface.blit(attack2image, a2['rect'])

            for h1 in range(0, player1life):

                if h1 % 2 == 0:
                    heartleftRect = (10 + (60*(h1//2)), 10, 44, 40)
                    windowSurface.blit(heartleft, heartleftRect)

                if h1 % 2 == 1:
                    heartrightRect = (10 + (60*(h1//2)), 10, 44, 40)
                    windowSurface.blit(heartright, heartrightRect)

            for h2 in range(0, player2life):
                
                if h2 % 2 == 0:
                    heartrightRect = (746 - (60*(h2//2)), 10, 44, 40)
                    windowSurface.blit(heartright, heartrightRect)

                if h2 % 2 == 1:
                    heartleftRect = (746 - (60*(h2//2)), 10, 44, 40)
                    windowSurface.blit(heartleft, heartleftRect)
            
            windowSurface.blit(player1image, player1Rect)
            windowSurface.blit(player2image, player2Rect)
            pygame.display.update()
            mainClock.tick(FPS)


        if player1life > 0:
            windowSurface.blit(bg1pwin, (0, 0))
            windowSurface.blit(bg1pwin, (0, 0))
            windowSurface.blit(bg1pwin, (0, 0))
            
        if player2life > 0:
            windowSurface.blit(bg2pwin, (0, 0))
            windowSurface.blit(bg1pwin, (0, 0))
            windowSurface.blit(bg1pwin, (0, 0))

        if player1life == 0 and player2life == 0:
            windowSurface.blit(bgdraw, (0, 0))

        pygame.display.update()

        again()


    #迷宮
    while modetype == 3:

        playerRect.topleft = (100, 270)
        mapRect.topleft = (0, -600)

        attack = []#攻擊物件串列
        cooltime = addattackrate
        attackflag = False

        attack2 = []
        attack2counter = 0

        playerlife = 10
        playerspeed = 2
        addattackrate = 40
        attackspeed = 3.5

        moveUp = moveDown = moveLeft = moveRight = False
        fightflag = False
        doorflag = False

        lines = []
        line1 = {'rect':pygame.Rect(0, -505, 500, 5), 'originRect':pygame.Rect(0, -505, 500, 5)}
        line2 = {'rect':pygame.Rect(600, -505, 1800, 5), 'originRect':pygame.Rect(600, -505, 1800, 5)}
        line3 = {'rect':pygame.Rect(505, -205, 190, 5), 'originRect':pygame.Rect(505, -205, 190, 5)}
        line4 = {'rect':pygame.Rect(1000, -105, 295, 5), 'originRect':pygame.Rect(1000, -105, 295, 5)}
        line5 = {'rect':pygame.Rect(0, 195, 295, 5), 'originRect':pygame.Rect(0, 195, 295, 5)}
        line6 = {'rect':pygame.Rect(505, 495, 90, 5), 'originRect':pygame.Rect(505, 495, 90, 5)}
        line7 = {'rect':pygame.Rect(600, 395, 95, 5), 'originRect':pygame.Rect(600, 395, 95, 5)}
        line8 = {'rect':pygame.Rect(905, 195, 595, 5), 'originRect':pygame.Rect(905, 195, 595, 5)}
        line9 = {'rect':pygame.Rect(905, 495, 295, 5), 'originRect':pygame.Rect(905, 495, 295, 5)}
        line10 = {'rect':pygame.Rect(1505, 795, 390, 5), 'originRect':pygame.Rect(1505, 795, 390, 5)}
        line11 = {'rect':pygame.Rect(1805, 195, 595, 5), 'originRect':pygame.Rect(1805, 195, 595, 5)}#
        line12 = {'rect':pygame.Rect(0, -100, 200, 5), 'originRect':pygame.Rect(0, -100, 200, 5)}
        line13 = {'rect':pygame.Rect(0, 400, 295, 5), 'originRect':pygame.Rect(0, 400, 295, 5)}
        line14 = {'rect':pygame.Rect(505, 0, 190, 5), 'originRect':pygame.Rect(505, 0, 190, 5)}
        line15 = {'rect':pygame.Rect(600, -300, 95, 5), 'originRect':pygame.Rect(600, -300, 95, 5)}
        line16 = {'rect':pygame.Rect(205, -300, 90, 5), 'originRect':pygame.Rect(205, -300, 90, 5)}
        line17 = {'rect':pygame.Rect(300, 700, 695, 5), 'originRect':pygame.Rect(300, 700, 695, 5)}
        line18 = {'rect':pygame.Rect(905, 400, 390, 5), 'originRect':pygame.Rect(905, 400, 390, 5)}
        line19 = {'rect':pygame.Rect(1000, 100, 500, 5), 'originRect':pygame.Rect(1000, 100, 500, 5)}
        line20 = {'rect':pygame.Rect(905, -300, 390, 5), 'originRect':pygame.Rect(905, -300, 390, 5)}
        line21 = {'rect':pygame.Rect(1505, -300, 90, 5), 'originRect':pygame.Rect(1505, -300, 90, 5)}
        line22 = {'rect':pygame.Rect(1805, -300, 595, 5), 'originRect':pygame.Rect(1805, -300, 595, 5)}
        line23 = {'rect':pygame.Rect(1000, 900, 200, 5), 'originRect':pygame.Rect(1000, 900, 200, 5)}
        line24 = {'rect':pygame.Rect(1600, 600, 200, 5), 'originRect':pygame.Rect(1600, 600, 200, 5)}
        line25 = {'rect':pygame.Rect(1805, 400, 90, 5), 'originRect':pygame.Rect(1805, 400, 90, 5)}
        line26 = {'rect':pygame.Rect(2105, 400, 295, 5), 'originRect':pygame.Rect(2105, 400, 295, 5)}
        line27 = {'rect':pygame.Rect(1905, 1000, 195, 5), 'originRect':pygame.Rect(1905, 1000, 195, 5)}
        line28 = {'rect':pygame.Rect(1300, 1000, 395, 5), 'originRect':pygame.Rect(1300, 1000, 395, 5)}
        line000 = {'rect':pygame.Rect(1700, 1100, 200, 5), 'originRect':pygame.Rect(1700, 1100, 200, 5)}#
        line29 = {'rect':pygame.Rect(200, -295, 5, 195), 'originRect':pygame.Rect(200, -295, 5, 195)}
        line30 = {'rect':pygame.Rect(500, -500, 5, 295), 'originRect':pygame.Rect(500, -500, 5, 295)}
        line31 = {'rect':pygame.Rect(500, 5, 5, 490), 'originRect':pygame.Rect(500, 5, 5, 490)}
        line32 = {'rect':pygame.Rect(1200, 500, 5, 600), 'originRect':pygame.Rect(1200, 500, 5, 600)}
        line33 = {'rect':pygame.Rect(900, 405, 5, 90), 'originRect':pygame.Rect(900, 405, 5, 90)}
        line34 = {'rect':pygame.Rect(900, -295, 5, 490), 'originRect':pygame.Rect(900, -295, 5, 490)}
        line35 = {'rect':pygame.Rect(1500, -295, 5, 395), 'originRect':pygame.Rect(1500, -295, 5, 395)}
        line36 = {'rect':pygame.Rect(1500, 200, 5, 595), 'originRect':pygame.Rect(1500, 200, 5, 595)}
        line37 = {'rect':pygame.Rect(2100, 405, 5, 595), 'originRect':pygame.Rect(2100, 405, 5, 595)}
        line38 = {'rect':pygame.Rect(1800, 405, 5, 195), 'originRect':pygame.Rect(1800, 405, 5, 195)}
        line39 = {'rect':pygame.Rect(1800, -295, 5, 490), 'originRect':pygame.Rect(1800, -295, 5, 490)}
        line40 = {'rect':pygame.Rect(1900, 1005, 5, 95), 'originRect':pygame.Rect(1900, 1005, 5, 95)}#
        line41 = {'rect':pygame.Rect(295, -295, 5, 490), 'originRect':pygame.Rect(295, -295, 5, 490)}
        line42 = {'rect':pygame.Rect(295, 405, 5, 295), 'originRect':pygame.Rect(295, 405, 5, 295)}
        line43 = {'rect':pygame.Rect(595, -500, 5, 200), 'originRect':pygame.Rect(595, -500, 5, 200)}
        line44 = {'rect':pygame.Rect(695, -295, 5, 90), 'originRect':pygame.Rect(695, -295, 5, 90)}
        line45 = {'rect':pygame.Rect(695, 5, 5, 390), 'originRect':pygame.Rect(695, 5, 5, 390)}
        line46 = {'rect':pygame.Rect(1295, -295, 5, 190), 'originRect':pygame.Rect(1295, -295, 5, 190)}
        line47 = {'rect':pygame.Rect(995, 705, 5, 190), 'originRect':pygame.Rect(995, 705, 5, 190)}
        line48 = {'rect':pygame.Rect(1295, 405, 5, 595), 'originRect':pygame.Rect(1295, 405, 5, 595)}
        line49 = {'rect':pygame.Rect(1595, -295, 5, 895), 'originRect':pygame.Rect(1595, -295, 5, 895)}
        line50 = {'rect':pygame.Rect(1695, 1005, 5, 95), 'originRect':pygame.Rect(1695, 1005, 5, 95)}
        line51 = {'rect':pygame.Rect(1895, 405, 5, 390), 'originRect':pygame.Rect(1895, 405, 5, 390)}
        line52 = {'rect':pygame.Rect(595, 400, 5, 95), 'originRect':pygame.Rect(595, 400, 5, 95)}
        line53 = {'rect':pygame.Rect(995, -100, 5, 200), 'originRect':pygame.Rect(995, -100, 5, 200)}
        
        lines.append(line1)
        lines.append(line2)
        lines.append(line3)
        lines.append(line4)
        lines.append(line5)
        lines.append(line6)
        lines.append(line7)
        lines.append(line8)
        lines.append(line9)
        lines.append(line10)
        lines.append(line11)
        lines.append(line12)
        lines.append(line13)
        lines.append(line14)
        lines.append(line15)
        lines.append(line16)
        lines.append(line17)
        lines.append(line18)
        lines.append(line19)
        lines.append(line20)
        lines.append(line21)
        lines.append(line22)
        lines.append(line23)
        lines.append(line24)
        lines.append(line25)
        lines.append(line26)
        lines.append(line27)
        lines.append(line28)
        lines.append(line000)
        lines.append(line29)
        lines.append(line30)
        lines.append(line31)
        lines.append(line32)
        lines.append(line33)
        lines.append(line34)
        lines.append(line35)
        lines.append(line36)
        lines.append(line37)
        lines.append(line38)
        lines.append(line39)
        lines.append(line40)
        lines.append(line41)
        lines.append(line42)
        lines.append(line43)
        lines.append(line44)
        lines.append(line45)
        lines.append(line46)
        lines.append(line47)
        lines.append(line48)
        lines.append(line49)
        lines.append(line50)
        lines.append(line51)
        lines.append(line52)
        lines.append(line53)

        monsters = []
        monster1 = {'rect':pygame.Rect(200, -450, 100, 100), 'originRect':pygame.Rect(200, -450, 100, 100),'image':pygame.transform.scale(pygame.image.load('GGright.png'),(100, 100)),'show': 1,
                    'face':'GGface.png', 'back':'GGback.png', 'left':'GGleft.png', 'right':'GGright.png',
                    'speed': 2,'rate': 50,'attackspeed': 4,'attackimage':pygame.image.load('attack2.png'), 'bg':pygame.image.load('bggame.png')}
        monster2 = {'rect':pygame.Rect(550, -150, 100, 100), 'originRect':pygame.Rect(550, -150, 100, 100),'image':pygame.transform.scale(pygame.image.load('m3left.png'),(100, 100)),'show': 1,
                    'face':'m3face.png', 'back':'m3back.png', 'left':'m3left.png', 'right':'m3right.png',
                    'speed': 2,'rate': 75,'attackspeed': 3,'attackimage':pygame.image.load('attack2.png'), 'bg':pygame.image.load('bggame.png')}
        monster3 = {'rect':pygame.Rect(500, 550, 100, 100), 'originRect':pygame.Rect(500, 550, 100, 100),'image':pygame.transform.scale(pygame.image.load('m2left.png'),(100, 100)),'show': 1,
                    'face':'m2face.png', 'back':'m2back.png', 'left':'m2left.png', 'right':'m2right.png',
                    'speed': 2,'rate': 75,'attackspeed': 3,'attackimage':pygame.image.load('attack2.png'), 'bg':pygame.image.load('bggame.png')}
        monster4 = {'rect':pygame.Rect(1350, -250, 100, 100), 'originRect':pygame.Rect(1350, -250, 100, 100),'image':pygame.transform.scale(pygame.image.load('GGback.png'),(100, 100)),'show': 1,
                    'face':'GGface.png', 'back':'GGback.png', 'left':'GGleft.png', 'right':'GGright.png',
                    'speed': 2,'rate': 50,'attackspeed': 3,'attackimage':pygame.image.load('attack2.png'), 'bg':pygame.image.load('bggame.png')}
        monster5 = {'rect':pygame.Rect(1050, 250, 100, 100), 'originRect':pygame.Rect(1050, 250, 100, 100),'image':pygame.transform.scale(pygame.image.load('m2left.png'),(100, 100)),'show': 1,
                    'face':'m2face.png', 'back':'m2back.png', 'left':'m2left.png', 'right':'m2right.png',
                    'speed': 2,'rate': 75,'attackspeed': 3,'attackimage':pygame.image.load('attack2.png'), 'bg':pygame.image.load('bggame.png')}
        monster6 = {'rect':pygame.Rect(900, 550, 100, 100), 'originRect':pygame.Rect(900, 550, 100, 100),'image':pygame.transform.scale(pygame.image.load('m3left.png'),(100, 100)),'show': 1,
                    'face':'m3face.png', 'back':'m3back.png', 'left':'m3left.png', 'right':'m3right.png',
                    'speed': 2,'rate': 50,'attackspeed': 3,'attackimage':pygame.image.load('attack2.png'), 'bg':pygame.image.load('bggame.png')}
        monster7 = {'rect':pygame.Rect(1900, -450, 100, 100), 'originRect':pygame.Rect(1900, -450, 100, 100),'image':pygame.transform.scale(pygame.image.load('GGleft.png'),(100, 100)),'show': 1,
                    'face':'GGface.png', 'back':'GGback.png', 'left':'GGleft.png', 'right':'GGright.png',
                    'speed': 2,'rate': 50,'attackspeed': 3,'attackimage':pygame.image.load('attack2.png'), 'bg':pygame.image.load('bggame.png')}
        monster8 = {'rect':pygame.Rect(1950, 550, 100, 100), 'originRect':pygame.Rect(1950, 550, 100, 100),'image':pygame.transform.scale(pygame.image.load('m3face.png'),(100, 100)),'show': 1,
                    'face':'m3face.png', 'back':'m3back.png', 'left':'m3left.png', 'right':'m3right.png',
                    'speed': 2,'rate': 75,'attackspeed': 3,'attackimage':pygame.image.load('attack2.png'), 'bg':pygame.image.load('bggame.png')}

        monsters.append(monster1)
        monsters.append(monster2)
        monsters.append(monster3)
        monsters.append(monster4)
        monsters.append(monster5)
        monsters.append(monster6)
        monsters.append(monster7)
        monsters.append(monster8)
        
        items = []
        heart1 = {'rect':pygame.Rect(628, -420, 44, 40),'originRect':pygame.Rect(628, -420, 44, 40), 'image': pygame.image.load('heart.png'), 'show': 1}
        heart2 = {'rect':pygame.Rect(628, 430, 44, 40),'originRect':pygame.Rect(628, 430, 44, 40), 'image': pygame.image.load('heart.png'), 'show': 1}
        heart3 = {'rect':pygame.Rect(1778, 1030, 44, 40),'originRect':pygame.Rect(1778, 1030, 44, 40), 'image': pygame.image.load('heart.png'), 'show': 1}
        heart4 = {'rect':pygame.Rect(1678, 480, 44, 40),'originRect':pygame.Rect(1678, 480, 44, 40), 'image': pygame.image.load('heart.png'), 'show': 1}
        door = {'rect': pygame.Rect(2360, 280, 40, 40), 'rect2':pygame.Rect(10, 280, 40, 40),'originRect': pygame.Rect(2360, 280, 40, 40), 'image':pygame.image.load('door.png'), 'show': 1}
        goldbox = {'rect':pygame.Rect(2100, -430, 60, 60),'originRect':pygame.Rect(2100, -430, 60, 60),'image':pygame.image.load('goldbox.png'),'show': 1}
        goldkey = {'rect':pygame.Rect(86, -250, 18, 34),'originRect':pygame.Rect(86, -250, 18, 34),'image':pygame.transform.scale(pygame.image.load('goldkey.png'),(27, 51)),'show': 1}
        sliverbox = {'rect':pygame.Rect(1070, 750, 60, 60),'originRect':pygame.Rect(1070, 750, 60, 60),'image':pygame.image.load('sliverbox.png'),'show': 1}
        sliverkey = {'rect':pygame.Rect(1086, -26, 18, 34),'originRect':pygame.Rect(1086, -26, 18, 34),'image':pygame.transform.scale(pygame.image.load('sliverkey.png'),(27, 51)),'show': 1}
        weapon = {'rect':pygame.Rect(2200, -420, 40, 40),'originRect':pygame.Rect(2200, -420, 40, 40),'image':pygame.image.load('weapon.png'),'show': 0}
        wing = {'rect':pygame.Rect(1080, 800, 40, 40),'originRect':pygame.Rect(1080, 800, 40, 40),'image':pygame.image.load('wing.png'),'show': 0}
                
        items.append(heart1)
        items.append(heart2)
        items.append(heart3)
        items.append(heart4)
        items.append(door)
        items.append(wing)
        items.append(goldbox)
        items.append(goldkey)
        items.append(sliverbox)
        items.append(sliverkey)
        items.append(weapon)
        #items.append()

        smallitems = []
        smallgoldkey = {'rect':pygame.Rect(682, 13, 18, 34), 'image':pygame.image.load('goldkey.png'), 'show' : 0}
        smallsliverkey = {'rect':pygame.Rect(654, 13, 18, 34), 'image':pygame.image.load('sliverkey.png'), 'show' : 0}
        smallwing = {'rect':pygame.Rect(304, 10, 40, 40), 'image':pygame.image.load('wing.png'), 'show' : 0}
        smallweapon = {'rect':pygame.Rect(354, 10, 40, 40), 'image':pygame.image.load('weapon.png'), 'show' : 0}
        smallitems.append(smallgoldkey)
        smallitems.append(smallsliverkey)
        smallitems.append(smallwing)
        smallitems.append(smallweapon)


        door2 = {'rect1':pygame.Rect(780, 240, 2, 120), 'rect2':(0, 260, 2, 80)}
        

        boss = {'life': 20, 'rate':40, 'speed': 2,'attackspeed': 5,
                'face1':'bossface1.png', 'face2':'bossface2.png', 'back1':'bossback1.png', 'back2':'bossback2.png',
                'left1':'bossleft1.png', 'left2':'bossleft2.png', 'right1':'bossright1.png', 'right2':'bossright2.png',
                'attackimage':pygame.image.load('attack2.png'), 'bg':pygame.image.load('bossroom.png')}

        while True:

            originplayerRectx = playerRect.x
            originplayerRecty = playerRect.y
            
            mapplayerx = playerRect.x - mapRect.x +30
            mapplayery = playerRect.y - mapRect.y +30

            playertime += 1
            if playertime > 40:
                playertime = 0

            for event in pygame.event.get():
                if event.type == QUIT:#關閉視窗
                    terminate()

                #鍵盤移動
                if event.type == KEYDOWN:

                    if event.key == K_w:#上
                        moveUp = True
                        for i in range(0, 11):
                            if playerRect.colliderect(lines[i]['rect']):
                                moveUp = False

                    if event.key == K_a:#左
                        moveLeft = True
                        for i in range(41, 54):
                            if playerRect.colliderect(lines[i]['rect']):
                                moveLeft = False

                    if event.key == K_s:#下
                        moveDown = True
                        for i in range(11, 29):
                            if playerRect.colliderect(lines[i]['rect']):
                                moveDown = False

                    if event.key == K_d:#右
                        moveRight = True
                        for i in range(29, 41):
                            if playerRect.colliderect(lines[i]['rect']):
                                moveRight = False

                if event.type == KEYUP:
                    
                    if event.key == K_w:#上
                        moveUp = False

                    if event.key == K_a:#左
                        moveLeft = False

                    if event.key == K_s:#下
                        moveDown = False

                    if event.key == K_d:#右
                        moveRight = False

                    if event.key == K_ESCAPE:#ESC
                        terminate()

                #滑鼠
                if event.type == MOUSEMOTION:
                    mouseRect.centerx = event.pos[0]
                    mouseRect.centery = event.pos[1]

                if event.type == MOUSEBUTTONDOWN:
                    if mouseRect.colliderect(homesmallRect):#home鍵
                        modetype = 0
                        
            
            #移動
            if moveLeft:
                if playerRect.left > 0:

                    if mapplayerx < (WINDOWWIDTH / 2):
                        mapRect.x = 0
                        for m in monsters:
                            m['rect'].x = m['originRect'].x
                        for l in lines:
                            l['rect'].x = l['originRect'].x
                        for i in items:
                            i['rect'].x = i['originRect'].x
                        playerRect.move_ip(-1*playerspeed, 0)

                    elif mapplayerx > (2400 - (WINDOWWIDTH / 2)):
                        mapRect.x = -1600
                        for m in monsters:
                            m['rect'].x = m['originRect'].x - 1600
                        for l in lines:
                            l['rect'].x = l['originRect'].x - 1600
                        for i in items:
                            i['rect'].x = i['originRect'].x - 1600
                        playerRect.move_ip(-1*playerspeed, 0)

                    else:
                        mapRect.move_ip(playerspeed, 0)
                        for l in lines:
                            l['rect'].move_ip(playerspeed, 0)
                        for m in monsters:
                            m['rect'].move_ip(playerspeed, 0)
                        for i in items:
                            i['rect'].move_ip(playerspeed, 0)

                if playertime > 20:
                    playerimage = pygame.image.load(playerleft1)
                else:
                    playerimage = pygame.image.load(playerleft2)

            if moveRight:
                if playerRect.right < WINDOWWIDTH:

                    if mapplayerx < (WINDOWWIDTH / 2):
                        mapRect.x = 0
                        for m in monsters:
                            m['rect'].x = m['originRect'].x
                        for l in lines:
                            l['rect'].x = l['originRect'].x
                        for i in items:
                            i['rect'].x = i['originRect'].x
                        playerRect.move_ip(playerspeed, 0)

                    elif mapplayerx > (2400 - (WINDOWWIDTH / 2)):
                        mapRect.x = -1600
                        for m in monsters:
                            m['rect'].x = m['originRect'].x - 1600
                        for l in lines:
                            l['rect'].x = l['originRect'].x - 1600
                        for i in items:
                            i['rect'].x = i['originRect'].x - 1600
                        playerRect.move_ip(playerspeed, 0)

                    else:
                        mapRect.move_ip(-1*playerspeed, 0)
                        for l in lines:
                            l['rect'].move_ip(-1*playerspeed, 0)
                        for m in monsters:
                            m['rect'].move_ip(-1*playerspeed, 0)
                        for i in items:
                            i['rect'].move_ip(-1*playerspeed, 0)

                if playertime > 20:
                    playerimage = pygame.image.load(playerright1)
                else:
                    playerimage = pygame.image.load(playerright2)

            if moveUp:
                if playerRect.top > 60:

                    if mapplayery < (WINDOWHEIGHT / 2):
                        mapRect.y = 0
                        for m in monsters:
                            m['rect'].y = m['originRect'].y + 600
                        for l in lines:
                            l['rect'].y = l['originRect'].y + 600
                        for i in items:
                            i['rect'].y = i['originRect'].y + 600
                        playerRect.move_ip(0, -1*playerspeed)

                    elif mapplayery > (1800 - (WINDOWHEIGHT / 2)):
                        mapRect.y = -1200
                        for m in monsters:
                            m['rect'].y = m['originRect'].y - 600
                        for l in lines:
                            l['rect'].y = l['originRect'].y - 600
                        for i in items:
                            i['rect'].y = i['originRect'].y - 600
                        playerRect.move_ip(0, -1*playerspeed)

                    else:
                        mapRect.move_ip(0, playerspeed)
                        for l in lines:
                            l['rect'].move_ip(0, playerspeed)
                        for m in monsters:
                            m['rect'].move_ip(0, playerspeed)
                        for i in items:
                            i['rect'].move_ip(0, playerspeed)

                if playertime > 20:
                    playerimage = pygame.image.load(playerback1)
                else:
                    playerimage = pygame.image.load(playerback2)

            if moveDown:
                if playerRect.bottom < WINDOWHEIGHT:

                    if mapplayery < (WINDOWHEIGHT / 2):
                        mapRect.y = 0
                        for m in monsters:
                            m['rect'].y = m['originRect'].y + 600
                        for l in lines:
                            l['rect'].y = l['originRect'].y + 600
                        for i in items:
                            i['rect'].y = i['originRect'].y + 600
                        playerRect.move_ip(0, playerspeed)

                    elif mapplayery > (1800 - (WINDOWHEIGHT / 2)):
                        mapRect.y = -1200
                        for m in monsters:
                            m['rect'].y = m['originRect'].y - 600
                        for l in lines:
                            l['rect'].y = l['originRect'].y - 600
                        for i in items:
                            i['rect'].y = i['originRect'].y - 600
                        playerRect.move_ip(0, playerspeed)

                    else:
                        mapRect.move_ip(0, -1*playerspeed)
                        for l in lines:
                            l['rect'].move_ip(0, -1*playerspeed)
                        for m in monsters:
                            m['rect'].move_ip(0, -1*playerspeed)
                        for i in items:
                            i['rect'].move_ip(0, -1*playerspeed)

                if playertime > 20:
                    playerimage = pygame.image.load(playerface1)
                else:
                    playerimage = pygame.image.load(playerface2)

            #牆
            for i in range(0, 11):
                if playerRect.colliderect(lines[i]['rect']):
                    moveUp = False
            for i in range(11, 29):
                if playerRect.colliderect(lines[i]['rect']):
                    moveDown = False
            for i in range(41, 54):
                if playerRect.colliderect(lines[i]['rect']):
                    moveLeft = False
            for i in range(29, 41):
                if playerRect.colliderect(lines[i]['rect']):
                    moveRight = False

            #撿愛心
            if playerRect.colliderect(heart1['rect']) and heart1['show'] == 1:
                heart1['show'] = 0
                if playerlife >= 8:
                    playerlife = 10
                else:
                    playerlife += 2
            if playerRect.colliderect(heart2['rect']) and heart2['show'] == 1:
                heart2['show'] = 0
                if playerlife >= 8:
                    playerlife = 10
                else:
                    playerlife += 2
            if playerRect.colliderect(heart3['rect']) and heart3['show'] == 1:
                heart3['show'] = 0
                if playerlife >= 8:
                    playerlife = 10
                else:
                    playerlife += 2
            if playerRect.colliderect(heart4['rect']) and heart4['show'] == 1:
                heart4['show'] = 0
                if playerlife >= 8:
                    playerlife = 10
                else:
                    playerlife += 2

            #撿鑰匙
            if playerRect.colliderect(goldkey['rect']) and goldkey['show'] == 1:
                goldkey['show'] = 0
                smallgoldkey['show'] = 1
            if playerRect.colliderect(sliverkey['rect']) and sliverkey['show'] == 1:
                sliverkey['show'] = 0
                smallsliverkey['show'] = 1

            #寶箱
            if playerRect.colliderect(goldbox['rect']) and goldbox['show'] == 1 and goldkey['show'] == 0:
                goldbox['show'] = 0
                weapon['show'] = 1
                smallgoldkey['show'] = 0
            if playerRect.colliderect(sliverbox['rect']) and sliverbox['show'] == 1 and sliverkey['show'] == 0:
                sliverbox['show'] = 0
                wing['show'] = 1
                smallsliverkey['show'] = 0

            #翅膀
            if playerRect.colliderect(wing['rect']) and wing['show'] == 1:
                wing['show'] = 0
                playerspeed += 1
                smallwing['show'] = 1

            #武器
            if playerRect.colliderect(weapon['rect']) and weapon['show'] == 1:
                weapon['show'] = 0
                addattackrate -= 15
                attackspeed = 5
                smallweapon['show'] = 1

            #撞怪物
            for m in monsters:
                if playerRect.colliderect(m['rect']) and m['show'] == 1:
                    fightflag = True
                    m['show'] = 0
                    

                    #進入戰鬥
                    while fightflag == True:

                        moveUp = moveDown = moveLeft = moveRight = False

                        attack = []#攻擊物件串列
                        cooltime = addattackrate
                        attackflag = False

                        attack2 = []
                        attack2counter = 0

                        monsterimage = pygame.image.load(m['face'])
                        monsterRect = monsterimage.get_rect()

                        playerRect.topleft = (100, 270)#玩家起始位置
                        monsterRect.topleft = (620, 260)#怪物起始位置

                        monsterlife = 10
                        
                        

                        while playerlife > 0 and monsterlife > 0: #生命值大於0

                            playertime += 1
                            if playertime > 40:
                                playertime = 0

                            if cooltime < addattackrate:
                                cooltime += 1

                            #偵測事件
                            for event in pygame.event.get():
                                if event.type == QUIT:#關閉視窗
                                    terminate()

                                #鍵盤移動
                                if event.type == KEYDOWN:

                                    if event.key == K_w:#上
                                        moveUp = True

                                    if event.key == K_a:#左
                                        moveLeft = True

                                    if event.key == K_s:#下
                                        moveDown = True

                                    if event.key == K_d:#右
                                        moveRight = True

                                if event.type == KEYUP:
                                    
                                    if event.key == K_w:#上
                                        moveUp = False

                                    if event.key == K_a:#左
                                        moveLeft = False

                                    if event.key == K_s:#下
                                        moveDown = False

                                    if event.key == K_d:#右
                                        moveRight = False

                                    if event.key == K_ESCAPE:#ESC
                                        terminate()

                                #滑鼠
                                if event.type == MOUSEMOTION:
                                    mouseRect.centerx = event.pos[0]
                                    mouseRect.centery = event.pos[1]

                                if event.type == MOUSEBUTTONDOWN:
                                    attackdesx = event.pos[0]
                                    attackdesy = event.pos[1]

                                    if cooltime == addattackrate:

                                        newattack = {'rect' : pygame.Rect(playerRect.centerx, playerRect.centery, attacksize, attacksize),
                                                     'speed' : (vector(attackdesx, attackdesy, playerRect.centerx, playerRect.centery, attackspeed))}

                                        attack.append(newattack)

                                        cooltime = 0                        


                            #偵測結束，移動玩家，換圖片
                            if moveLeft and playerRect.left > 0:
                                playerRect.move_ip(-1*playerspeed, 0)

                                if playertime > 20:
                                    playerimage = pygame.image.load(playerleft1)
                                else:
                                    playerimage = pygame.image.load(playerleft2)

                            if moveRight and playerRect.right < WINDOWWIDTH:
                                playerRect.move_ip(playerspeed, 0)

                                if playertime > 20:
                                    playerimage = pygame.image.load(playerright1)
                                else:
                                    playerimage = pygame.image.load(playerright2)

                            if moveUp and playerRect.top > 60:
                                playerRect.move_ip(0, -1*playerspeed)

                                if playertime > 20:
                                    playerimage = pygame.image.load(playerback1)
                                else:
                                    playerimage = pygame.image.load(playerback2)

                            if moveDown and playerRect.bottom < WINDOWHEIGHT:
                                playerRect.move_ip(0, playerspeed)

                                if playertime > 20:
                                    playerimage = pygame.image.load(playerface1)
                                else:
                                    playerimage = pygame.image.load(playerface2)

                            #新增攻擊
                            for a in attack:
                                a['rect'].move_ip(a['speed'])

                            for a in attack:
                                if a['rect'].colliderect(monsterRect):
                                    monsterlife -= 1
                                    attack.remove(a)

                                if a['rect'].top > WINDOWHEIGHT or a['rect'].bottom < (60 + attacksize) or a['rect'].right < 0 or a['rect'].left > WINDOWWIDTH:
                                    attack.remove(a)

                            #怪物移動
                            monsterRect.move_ip(vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, m['speed']))

                            rx = vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, m['speed'])[0]
                            ry = vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, m['speed'])[1]
                            if rx > 0:
                                monsterimage = pygame.image.load(m['right'])
                            if rx < 0:
                                monsterimage = pygame.image.load(m['left'])
                            if ry > 0 and rx < m['speed']**(0.5) and rx > -1*m['speed']**(0.5):
                                monsterimage = pygame.image.load(m['face'])
                            if ry < 0 and rx < m['speed']**(0.5) and rx > -1*m['speed']**(0.5):
                                monsterimage = pygame.image.load(m['back'])

                            #怪物攻擊
                            attack2counter += 1
                            if attack2counter == m['rate']:
                                attack2counter = 0
                                newattack2 = {'rect' : pygame.Rect(monsterRect.centerx, monsterRect.centery, attacksize, attacksize),
                                                'speed' : (vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, m['attackspeed']))}

                                attack2.append(newattack2)

                            for a2 in attack2:
                                a2['rect'].move_ip(a2['speed'])
                                      
                            for a2 in attack2:
                                if a2['rect'].colliderect(playerRect):
                                    playerlife -= 1
                                    attack2.remove(a2)

                                if a2['rect'].top > WINDOWHEIGHT or a2['rect'].bottom < (60 + attack2size) or a2['rect'].right < 0 or a2['rect'].left > WINDOWWIDTH:
                                    attack2.remove(a2)

                            #怪物撞擊
                            if monsterRect.colliderect(playerRect):
                                playerlife -= 1
                                monsterRect.move_ip(-25*vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, m['speed'])[0],
                                                    -25*vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, m['speed'])[1])

                                    
                            
                            #繪製物件
                            windowSurface.blit(m['bg'],(0,0))

                            for a in attack:
                                windowSurface.blit(attackimage, a['rect'])

                            for a2 in attack2:
                                windowSurface.blit(m['attackimage'], a2['rect'])

                            for h1 in range(0, playerlife):

                                if h1 % 2 == 0:
                                    heartleftRect = (10 + (60*(h1//2)), 10, 44, 40)
                                    windowSurface.blit(heartleft, heartleftRect)

                                if h1 % 2 == 1:
                                    heartrightRect = (10 + (60*(h1//2)), 10, 44, 40)
                                    windowSurface.blit(heartright, heartrightRect)

                            for h2 in range(0, monsterlife):
                                
                                if h2 % 2 == 0:
                                    heartrightRect = (746 - (60*(h2//2)), 10, 44, 40)
                                    windowSurface.blit(heartright, heartrightRect)

                                if h2 % 2 == 1:
                                    heartleftRect = (746 - (60*(h2//2)), 10, 44, 40)
                                    windowSurface.blit(heartleft, heartleftRect)

                            
                            windowSurface.blit(playerimage, playerRect)
                            windowSurface.blit(monsterimage, monsterRect)
                            pygame.display.update()
                            mainClock.tick(FPS)

                        if playerlife > 0:
                            fightflag = False
                            
                        elif playerlife == 0:
                            windowSurface.blit(bggameover, (0, 0))
                            pygame.display.update()
                            
                            home()
                            
                            fightflag = False
                                
                    playerRect.x = originplayerRectx
                    playerRect.y = originplayerRecty
                    moveUp = moveDown = moveLeft = moveRight = False
  
            
            #boss門
            if playerRect.colliderect(door['rect']):
                doorflag = True
                playerRect.topleft = (70, 270)

                while doorflag == True:

                    playertime += 1
                    if playertime > 40:
                        playertime = 0

                    lineup = pygame.Rect(0, 210, 800, 30)
                    lineunder = pygame.Rect(0, 360, 800, 30)

                    #偵測事件
                    for event in pygame.event.get():
                        if event.type == QUIT:#關閉視窗
                            terminate()

                        #鍵盤移動
                        if event.type == KEYDOWN:

                            if event.key == K_w:#上
                                moveUp = True
                                if playerRect.colliderect(lineup):
                                    moveUp = False

                            if event.key == K_a:#左
                                moveLeft = True

                            if event.key == K_s:#下
                                moveDown = True
                                if playerRect.colliderect(lineunder):
                                    moveDown = False

                            if event.key == K_d:#右
                                moveRight = True

                        if event.type == KEYUP:
                            
                            if event.key == K_w:#上
                                moveUp = False

                            if event.key == K_a:#左
                                moveLeft = False

                            if event.key == K_s:#下
                                moveDown = False

                            if event.key == K_d:#右
                                moveRight = False

                            if event.key == K_ESCAPE:#ESC
                                terminate()

                        #滑鼠
                        if event.type == MOUSEMOTION:
                            mouseRect.centerx = event.pos[0]
                            mouseRect.centery = event.pos[1]

                        if event.type == MOUSEBUTTONDOWN:
                            if mouseRect.colliderect(homesmallRect):#home鍵
                                modetype = 0
                                
                    if playerRect.colliderect(lineup):
                        moveUp = False

                    if playerRect.colliderect(lineunder):
                        moveDown = False

                    #偵測結束，移動玩家，換圖片
                    if moveLeft and playerRect.left > 0:
                        playerRect.move_ip(-1*playerspeed, 0)

                        if playertime > 20:
                            playerimage = pygame.image.load(playerleft1)
                        else:
                            playerimage = pygame.image.load(playerleft2)

                    if moveRight and playerRect.right < WINDOWWIDTH:
                        playerRect.move_ip(playerspeed, 0)

                        if playertime > 20:
                            playerimage = pygame.image.load(playerright1)
                        else:
                            playerimage = pygame.image.load(playerright2)

                    if moveUp and playerRect.top > 60:
                        playerRect.move_ip(0, -1*playerspeed)

                        if playertime > 20:
                            playerimage = pygame.image.load(playerback1)
                        else:
                            playerimage = pygame.image.load(playerback2)

                    if moveDown and playerRect.bottom < WINDOWHEIGHT:
                        playerRect.move_ip(0, playerspeed)

                        if playertime > 20:
                            playerimage = pygame.image.load(playerface1)
                        else:
                            playerimage = pygame.image.load(playerface2)

                    #回迷宮
                    if playerRect.colliderect(door['rect2']):
                        doorflag = False
                        playerRect.x = originplayerRectx - 20
                        playerRect.y = originplayerRecty

                    #進bossroom
                    elif playerRect.colliderect(door2['rect1']):
                        fightflag = True

                    if modetype == 0:
                        break
                    
                    windowSurface.blit(bgbossroute, (0, 0))
                    windowSurface.blit(door['image'], door['rect2'])
                    windowSurface.blit(playerimage, playerRect)
                    for h in range(0, playerlife):
                        if h % 2 == 0:
                            heartleftRect = (10 + (60*(h//2)), 10, 44, 40)
                            windowSurface.blit(heartleft, heartleftRect)

                        if h % 2 == 1:
                            heartrightRect = (10 + (60*(h//2)), 10, 44, 40)
                            windowSurface.blit(heartright, heartrightRect)
                    windowSurface.blit(homesmall, homesmallRect)
                    pygame.display.update()
                    mainClock.tick(FPS)

                    #bossroom
                    while fightflag == True:

                        attack = []#攻擊物件串列
                        cooltime = addattackrate
                        attackflag = False

                        attack2 = []
                        attack2counter = 0

                        monsterimage = pygame.image.load(boss['face1'])
                        monsterRect = monsterimage.get_rect()

                        playerRect.topleft = (100, 270)#玩家起始位置
                        monsterRect.topleft = (620, 270)#怪物起始位置

                        boss['life'] = 20

                        line01 = pygame.Rect(10, 0, 5, 255)
                        line02 = pygame.Rect(10, 345, 5, 255)
                        line03 = pygame.Rect(0, 255, 10, 5)
                        line04 = pygame.Rect(0, 340, 10, 5)

                        while playerlife > 0 and boss['life'] > 0: #生命值大於0

                            playertime += 1
                            if playertime > 40:
                                playertime = 0

                            bosstime += 1
                            if bosstime > 40:
                                bosstime = 0

                            if cooltime < addattackrate:
                                cooltime += 1

                            #偵測事件
                            for event in pygame.event.get():
                                if event.type == QUIT:#關閉視窗
                                    terminate()

                                #鍵盤移動
                                if event.type == KEYDOWN:

                                    if event.key == K_w:#上
                                        moveUp = True
                                        if playerRect.colliderect(line03):
                                            moveUp = False

                                    if event.key == K_a:#左
                                        moveLeft = True
                                        if playerRect.colliderect(line01) or playerRect.colliderect(line02):
                                            moveLeft = False

                                    if event.key == K_s:#下
                                        moveDown = True
                                        if playerRect.colliderect(line04):
                                            moveDown = False

                                    if event.key == K_d:#右
                                        moveRight = True

                                if event.type == KEYUP:
                                    
                                    if event.key == K_w:#上
                                        moveUp = False

                                    if event.key == K_a:#左
                                        moveLeft = False

                                    if event.key == K_s:#下
                                        moveDown = False

                                    if event.key == K_d:#右
                                        moveRight = False

                                    if event.key == K_ESCAPE:#ESC
                                        terminate()

                                #滑鼠
                                if event.type == MOUSEMOTION:
                                    mouseRect.centerx = event.pos[0]
                                    mouseRect.centery = event.pos[1]

                                if event.type == MOUSEBUTTONDOWN:
                                    attackdesx = event.pos[0]
                                    attackdesy = event.pos[1]

                                    if cooltime == addattackrate:

                                        newattack = {'rect' : pygame.Rect(playerRect.centerx, playerRect.centery, attacksize, attacksize),
                                                     'speed' : (vector(attackdesx, attackdesy, playerRect.centerx, playerRect.centery, attackspeed))}

                                        attack.append(newattack)

                                        cooltime = 0
                                        
                            if playerRect.colliderect(line03):
                                moveUp = False
                            if playerRect.colliderect(line01) or playerRect.colliderect(line02):
                                moveLeft = False
                            if playerRect.colliderect(line04):
                                moveDown = False


                            #偵測結束，移動玩家，換圖片
                            if moveLeft and playerRect.left > 0:
                                playerRect.move_ip(-1*playerspeed, 0)

                                if playertime > 20:
                                    playerimage = pygame.image.load(playerleft1)
                                else:
                                    playerimage = pygame.image.load(playerleft2)

                            if moveRight and playerRect.right < WINDOWWIDTH:
                                playerRect.move_ip(playerspeed, 0)

                                if playertime > 20:
                                    playerimage = pygame.image.load(playerright1)
                                else:
                                    playerimage = pygame.image.load(playerright2)

                            if moveUp and playerRect.top > 60:
                                playerRect.move_ip(0, -1*playerspeed)

                                if playertime > 20:
                                    playerimage = pygame.image.load(playerback1)
                                else:
                                    playerimage = pygame.image.load(playerback2)

                            if moveDown and playerRect.bottom < WINDOWHEIGHT:
                                playerRect.move_ip(0, playerspeed)

                                if playertime > 20:
                                    playerimage = pygame.image.load(playerface1)
                                else:
                                    playerimage = pygame.image.load(playerface2)

                            #新增攻擊
                            for a in attack:
                                a['rect'].move_ip(a['speed'])

                            for a in attack:
                                if a['rect'].colliderect(monsterRect):
                                    boss['life'] -= 1
                                    attack.remove(a)

                                if a['rect'].top > WINDOWHEIGHT or a['rect'].bottom < (60 + attacksize) or a['rect'].right < 0 or a['rect'].left > WINDOWWIDTH:
                                    attack.remove(a)

                            #怪物移動
                            monsterRect.move_ip(vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, boss['speed']))

                            rx = vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, boss['speed'])[0]
                            ry = vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, boss['speed'])[1]
                            if rx > 0:
                                if bosstime > 20:
                                    monsterimage = pygame.image.load(boss['right1'])
                                else:
                                    monsterimage = pygame.image.load(boss['right2'])
                            if rx < 0:
                                if bosstime > 20:
                                    monsterimage = pygame.image.load(boss['left1'])
                                else:
                                    monsterimage = pygame.image.load(boss['left2'])
                            if ry > 0 and rx < boss['speed']**(0.5) and rx > -1*boss['speed']**(0.5):
                                if bosstime > 20:
                                    monsterimage = pygame.image.load(boss['face1'])
                                else:
                                    monsterimage = pygame.image.load(boss['face2'])
                            if ry < 0 and rx < boss['speed']**(0.5) and rx > -1*boss['speed']**(0.5):
                                if bosstime > 20:
                                    monsterimage = pygame.image.load(boss['back1'])
                                else:
                                    monsterimage = pygame.image.load(boss['back2'])

                            #怪物攻擊
                            attack2counter += 1
                            if attack2counter == boss['rate']:
                                attack2counter = 0
                                newattack2 = {'rect' : pygame.Rect(monsterRect.centerx, monsterRect.centery, attacksize, attacksize),
                                                'speed' : (vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, boss['attackspeed']))}

                                attack2.append(newattack2)

                            for a2 in attack2:
                                a2['rect'].move_ip(a2['speed'])
                                      
                            for a2 in attack2:
                                if a2['rect'].colliderect(playerRect):
                                    playerlife -= 1
                                    attack2.remove(a2)

                                if a2['rect'].top > WINDOWHEIGHT or a2['rect'].bottom < (60 + attack2size) or a2['rect'].right < 0 or a2['rect'].left > WINDOWWIDTH:
                                    attack2.remove(a2)

                            #怪物撞擊
                            if monsterRect.colliderect(playerRect):
                                playerlife -= 1
                                monsterRect.move_ip(-25*vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, boss['speed'])[0],
                                                    -25*vector(playerRect.centerx, playerRect.centery, monsterRect.centerx, monsterRect.centery, boss['speed'])[1])

                                    
                            #撞門退出
                            if playerRect.colliderect(door2['rect2']):
                                boss['life'] = 0
                                fightflag = False


                            #繪製物件
                            windowSurface.blit(boss['bg'],(0,0))

                            for a in attack:
                                windowSurface.blit(attackimage, a['rect'])

                            for a2 in attack2:
                                windowSurface.blit(boss['attackimage'], a2['rect'])

                            for h1 in range(0, playerlife):

                                if h1 % 2 == 0:
                                    heartleftRect = (10 + (60*(h1//2)), 10, 44, 40)
                                    windowSurface.blit(heartleft, heartleftRect)

                                if h1 % 2 == 1:
                                    heartrightRect = (10 + (60*(h1//2)), 10, 44, 40)
                                    windowSurface.blit(heartright, heartrightRect)

                            for h2 in range(0, boss['life']):
                                
                                if h2 % 4 == 0:
                                    bossheart4Rect = (746 - (60*(h2//4)), 10, 44, 40)
                                    windowSurface.blit(bossheart4, bossheart4Rect)

                                elif h2 % 4 == 1:
                                    bossheart3Rect = (746 - (60*(h2//4)), 10, 44, 40)
                                    windowSurface.blit(bossheart3, bossheart3Rect)

                                elif h2 % 4 == 2:
                                    bossheart2Rect = (746 - (60*(h2//4)), 10, 44, 40)
                                    windowSurface.blit(bossheart2, bossheart2Rect)

                                elif h2 % 4 == 3:
                                    bossheart1Rect = (746 - (60*(h2//4)), 10, 44, 40)
                                    windowSurface.blit(bossheart1, bossheart1Rect)

                            
                            windowSurface.blit(playerimage, playerRect)
                            windowSurface.blit(monsterimage, monsterRect)
                            pygame.display.update()
                            mainClock.tick(FPS)

                        if fightflag == False:
                            playerRect.topleft = (720, 270)
                            break

                        if playerlife > 0:
                            windowSurface.blit(bgmazewin, (0, 0))
                            pygame.display.update()

                            home()

                            fightflag = False
                            doorflag = False
                            

                        elif playerlife == 0:
                            windowSurface.blit(bggameover, (0, 0))
                            pygame.display.update()
                            
                            home()
                            
                            fightflag = False
                            doorflag = False
                        
            if modetype == 0:
                break
            
            windowSurface.blit(bgmap, mapRect)
            
            for m in monsters:
                if m['show'] == 1:
                    windowSurface.blit(m['image'], m['rect'])
            for i in items:
                if i['show'] == 1:
                    windowSurface.blit(i['image'], i['rect'])
                    
            windowSurface.blit(playerimage, playerRect)
            
            for h in range(0, playerlife):

                if h % 2 == 0:
                    heartleftRect = (10 + (60*(h//2)), 10, 44, 40)
                    windowSurface.blit(heartleft, heartleftRect)

                if h % 2 == 1:
                    heartrightRect = (10 + (60*(h//2)), 10, 44, 40)
                    windowSurface.blit(heartright, heartrightRect)

            for si in smallitems:
                if si['show'] == 1:
                    windowSurface.blit(si['image'], si['rect'])
                    
            windowSurface.blit(homesmall, homesmallRect)
            pygame.display.update()
            mainClock.tick(FPS)
