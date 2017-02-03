import pygame
from pygame.locals import *
import pygame.mixer
import random
#-------------------write-----------------------------------
def write1(writing):
    color = 250,250,250
    pygame.font.init()
    font = pygame.font.Font(None,125)
    textsurface = font.render(str(score),True,color)
    screen.blit(textsurface,(545,255))
def write2(writing):
    color = 250,250,250
    pygame.font.init()
    font = pygame.font.Font(None,75)
    textsurface = font.render("Score:"+str(score),True,color)
    screen.blit(textsurface,(0,0))
def write3(writing):
    color = 209,27,27
    pygame.font.init()
    font = pygame.font.Font(None,75)
    textsurface=font.render("Anti G incoming",True,color)
    screen.blit(textsurface,(300,0))
def write4(writing):
    color = 250,250,250
    pygame.font.init()
    font = pygame.font.Font(None,75)
    textsurface=font.render("Ammo:"+str(bullet),True,color)
    screen.blit(textsurface,(0,550))
def highscore_write(writing):
    color = 250,250,250
    pygame.font.init()
    font  = pygame.font.Font(None,75)
    textsurface= font.render("Highscore:"+str(highscore),True,color)
    screen.blit(textsurface,(0,40))
highscore_text = open("highscore.txt","r")
s = highscore_text.readline().strip()
highscore = (int(s))
highscore_text.close()
#------------Setting-Screen-size----------------------------
screen_width = 1000                      
screen_height = 600
size = screen_width,screen_height
screen= pygame.display.set_mode(size)
#-------------Loading-Bird----------------------------------
bird = pygame.image.load("bird.png")     
bird = pygame.transform.scale(bird,(150,50))
bird_width, bird_height = bird.get_size()
slice_bird_width= bird_width/3
slice_bird_height = bird_height
#------------Appending Bird --------------------------------
bird_flap =[]                            #Appending Bird Flap
for pipe_h_value in range(3):
    bird_flap.append(bird.subsurface(pipe_h_value*slice_bird_width,0, slice_bird_width, bird_height))
#------------------Loading Fireball--------------------------
fireball = pygame.image.load("fireball.png")
fireball_width,fireball_height = fireball.get_size()
slice_fireball_width = fireball_width/8
#-------------------Fireball Appending-----------------------
fireball_move = []
for pipe_h_value in range(8):
    fireball_move.append(fireball.subsurface(pipe_h_value*slice_fireball_width,0,slice_fireball_width,fireball_height))
#---------------Loading Picture------------------------------    
background = pygame.image.load("background.png")
instruction_pic = pygame.image.load("instruction.png")
end_pic = pygame.image.load("End.png")
menu_pic = pygame.image.load("menu.png")     

pipe = pygame.image.load("Pipe2.png")
pipe_width, pipe_height = pipe.get_size()

space = pygame.image.load("space.png")

cat = pygame.image.load("cat.png")
cat = pygame.transform.scale(cat,(100,50))
cat_width, cat_heights = cat.get_size()

laser = pygame.image.load("laser.png")
laser_width, laser_height = laser.get_size()

coin = pygame.image.load("coin.png")
coin = pygame.transform.scale(coin,(50,50))
coin_width, coin_heights = coin.get_size()

catboss = pygame.image.load("catboss.png")
catboss = pygame.transform.scale(catboss,(100,100))
catboss_width, catboss_height = catboss.get_size()
#---------------Getting sound files--------------------------
pygame.mixer.init()
music = pygame.mixer.Sound("music.wav")
flap = pygame.mixer.Sound("flap.wav")
smack = pygame.mixer.Sound("smack.wav")
point = pygame.mixer.Sound("bading.wav")
#---------------Setting Values-------------------------------
flapNum=0
fly = 0
score = 0
menu = True
end = False
life = False
instruction = False
firenum = 0
boost = False
antiG = False
hit = False
laserz = False
blank=("")
clock = pygame.time.Clock()
#--------------Game Start-------------------------------------
gameOn = True
while gameOn == True:  
    for event in pygame.event.get():
        if event.type == QUIT: 
            gameOn = False            
        elif event.type == KEYDOWN:                 
#---------------------------Menu------------------------------------------            
            if menu == True:
                 
                if event.key == K_i:
                        instruction = True
                        menu = False                
                if event.key == K_RETURN:
                    life=True
                    birdX=450
                    birdY=300
                    pipeX = 1000
                    fly = 0  
                    score = 0
                    music.play()
                    menu = False
                    boost = False
                    gravity = 0.3
                    catX = 1000
                    coinX = 1500
                    antiG = False
                    bullet = 10
                    hard = False
                    hit = False
                    laserz = False
                    laserX = 450
                    catbossX = 1000
                    catboss_hit = False
                    
#-----------------Death-------------------------------------------------------
            if end == True:
                if event.key == K_r:
                    life=True
                    birdX=450
                    birdY=300
                    pipeX = 1000
                    fly = 0  
                    score = 0
                    music.play()
                    menu = False
                    boost = False
                    gravity = 0.3
                    catX = 1000
                    coinX = 1500
                    antiG = False
                    bullet = 10
                    hard = False
                    hit = False
                    laserz = False
                    laserX = 450
                    catbossX = 1000
                    catboss_hit = False
                    end = False
                if event.key == K_m:
                    end = False 
                    menu = True
#--------------------------------------Life---------------------------------                  
            if life == True:
                if event.key == K_SPACE: 
                    if antiG == True:
                        fly = 6
                        flap.play()
                        flapNum = flapNum+1   #Animation Counter For Bird
                        if flapNum == 3:
                            flapNum = 0                          
                    if antiG == False:
                        fly = -6
                        flap.play()
                        flapNum = flapNum+1   #Animation Counter For Bird
                        if flapNum == 3:
                            flapNum = 0                          
                if event.key == K_x:
                    boost = True
#-----------------------------------------------------------------------------               
                if event.key == K_z and bullet >0 and laserz == False:
                    laserz = True
                    laserY = birdY-20                    
                    if bullet >= 0:
                        bullet = bullet - 1
                    if bullet <=0 :
                        bullet = 0
                    laserY = birdY
#--------------------------Key Up----------------------------------------
        elif event.type == KEYUP:
            if instruction == True:
                if event.key == K_i:
                    menu = True
                    instruction = False
            if life == True  :
                if event.key == K_x:
                    boost = False
                
    if instruction == True:
        screen.blit(instruction_pic,(0,0))
        pygame.display.flip()
    if menu == True:
        screen.blit(menu_pic,(0,0))
        pygame.display.flip()           
#-----------------------Fire Counter--------------------------------------------
    firenum = firenum+1
    if firenum == 8:
        firenum = 0
#------------------------Blitting------------------------------------
    pipe_height=[-25,-35,-50,-65,-75,-85,-100,-115,-125,-135,-150,-175,-200,-225,-250,-275,-300,-325,-350,-375,-400]
    cat_height=[25,35,45,50,65,75,85,100,115,125,135,150,165,175,200,225,250,275,300,325,375,400,425,450,475,500,525]
    coin_height=[25,35,45,50,65,75,85,100,115,125,135,150,165,175,200,225,250,275,300,325,375,400,425,450,475,500,525]
    catboss_heights=[25,50,100,175,225,300,500]
    if life == True:                #pipes 404
        pipe_h_value = random.randint(0,20)
        cat_h_value = random.randint(0,26)
        coin_h_value = random.randint(0,26)
#----------------------------Score if statements--------------------------------
        if score >= 1000:
            hard = True
            screen.blit(space,(0,0))
        if score <= 300:
            screen.blit(background,(0,0))
        if 300>= score >= 250:
            write3(blank)
        if 1000>= score >= 300:
            antiG = True
            gravity = -0.3
            screen.blit(space,(0,0))            
#-------------------------height choice--------------------------------------------------     
        if catX == 1000:
            catY =  cat_height[cat_h_value]
            hit = False
        if pipeX == 1000:
                pipeY = pipe_height[pipe_h_value]
        if coinX == 1500:
            coinY = coin_height[coin_h_value]
            eat = False
#---------------------------movement------------------------------------------        
        if boost == False:
            pipeX = pipeX-5
            catX = catX-10
            coinX = coinX-13
        if boost == True:
            pipeX = pipeX-13
            catX = catX-23
            coinX = coinX-33
            screen.blit(fireball_move[firenum],(birdX-50,birdY))
        if laserz == True:
            laserX = laserX+15
            screen.blit(laser,(laserX,laserY))
            if laserX >= 1000:
                laserz = False
                laserX = 450
        screen.blit(pipe,(pipeX,pipeY))
        if hit == False:
            screen.blit(cat,(catX,catY))
        if eat == False:
            screen.blit(coin,(coinX,coinY))
        write4(bullet)
        write2(score)
        if hard == True:
            if catbossX == 1000:
                catbossH = random.randint(0,6)
            catbossY = catboss_heights[catbossH]
            if boost == False:
                catbossX = catbossX-15
            if boost == True:
                catbossX = catbossX-15
            if catboss_hit == False:
                screen.blit(catboss,(catbossX,catbossY))
            if catbossX <=-300:
                catbossX = 1000
                catboss_hit = False
            
#----------------RESET---------------------------------------------------------
        if pipeX <= -200:
            pipeX = 1000
        if catX <= -300:
            catX = 1000
        if coinX <= -500:
            coinX = 1500
#----------------------Flight---------------------------------------------------
        fly = fly + gravity          
        
        birdY = birdY + fly                 #bird movement
        if birdY <=0 :                      #Ceilling
            birdY = 0
            if antiG == True:
                life = False
                end = True
                smack.play()
        
        if birdY >= 550:
            birdY = 550
            end = True
            life = False
            smack.play()
#------------------hit detection-----------------------        
        if pipeX <= birdX <= pipeX+pipe_width :
            if birdY <= pipeY + 404:
                end = True
                life = False
                smack.play()
                lasers = False
            if birdY+bird_height >= pipeY + 603:
                end = True
                life = False
                smack.play()
                lasers = False
        
        if birdX+slice_bird_width == pipeX:
            if birdY == pipeY + 404:
                end = True
                life = False
                smack.play()
                lasers = False
        
        if hit == False:
            if catX<=birdX<=catX+cat_width:
                if catY <= birdY <=catY + cat_heights:
                    life = False
                    end = True
                    smack.play()
                if catY <birdY+bird_height-10 <= catY + cat_heights:
                    life = False
                    end = True
                    smack.play()
        
        if catboss_hit == False:
            if catbossX<=birdX<=catbossX+catboss_width:
                if catbossY <= birdY <= catbossY + catboss_height:
                    life = False
                    end = True
                    smack.play()
                if catbossY <birdY+bird_height-10 <= catbossY + catboss_height-50:
                    life = False
                    end = True
                    smack.play()            
        if laserz == True and hard == True:
            if catbossX<=laserX+laser_width<=catbossX+catboss_width:
                if catbossY-10 <= laserY <= catbossY +catboss_height-50:
                    catboss_hit = True
                    score = score + 5
                    
        if laserz == True:            
            if catX<=laserX+laser_width<=catX+cat_width:
                if catY-10 <= laserY <= catY +cat_heights:
                    hit = True
                    score = score + 5           
                                     
#-----------------------score detection--------------------------------------   
        if  pipeX <= birdX <= pipeX+pipe_width:
            if life == True:
                score = score+1
                point.play()
        screen.blit(bird_flap[flapNum],(birdX,birdY))
        
        if coinX<=birdX<=coinX+coin_width:
            if coinY <= birdY <=coinY + coin_heights:
                if life == True:
                    score = score+25
                    point.play()
                    eat = True
            if coinY <birdY+bird_height-10 <= coinY + coin_heights:
                if life == True:
                    score = score+25
                    eat = True
                    point.play()               
#-----------------------End Screen-------------------------------------------    
        if end == True:
            screen.blit(end_pic,(0,0))
            music.stop()
            write1(score)            
            if score > highscore:
                highscore = score
                highscore_write(highscore)
            else:
                highscore_write(highscore)
        clock.tick(180)    
        pygame.display.flip()       
highscoretext = open("highscore.txt","w")
highscore = str(highscore)
highscoretext.write(highscore)
highscoretext.close()
pygame.quit()
