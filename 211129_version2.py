#-*- coding: utf-8 -*-#

################################################
#           author : Yong Ju Park              #
#           welcome to tomatoWorld!            #
################################################

################################################
# import modules
import random
import sys
import math
import pygame
from pygame import mixer
import pygame.gfxdraw
import time
from time import sleep
from math import pi

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

global game_status
game_status = "main"

################################################

# import fonts
pygame.font.init()
font = pygame.font.SysFont('휴먼둥근헤드라인', 20)

# import images - characters
mainbackground = pygame.image.load('main.png')
mainbackground = pygame.transform.scale(mainbackground, (800, 500))
bluebackground = pygame.image.load('blue.png')
bluebackground = pygame.transform.scale(bluebackground, (800, 500))
explainbackground = pygame.image.load('explain.png')
explainbackground = pygame.transform.scale(explainbackground, (800, 500))
quizbackground = pygame.image.load('quiz.png')
quizbackground = pygame.transform.scale(quizbackground, (800, 500))

################################################
# tomato class
# decides movements, storyline
VELOCITY = 7
MASS = 2

class tomato:
    def __init__(self) -> None:
        self.dx = 0
        self.dy = 0
        self.x = 0 + self.dx
        self.y = 0 + self.dy        
        self.right_arm = 1
        self.left_arm = 1
        self.right_max = 90
        self.left_max = - 520
        self.isJump = 0
        self.v = VELOCITY 
        self.m = MASS          
        
    def shape(self):
        # 몸통
        pygame.draw.ellipse(SCREEN, (255,0,0), [577+self.x, 340+self.y, 104, 124])
        pygame.draw.ellipse(SCREEN, (0,0,0), [571+self.x,334+self.y, 110, 130], 6)
                #꽁지1
        pygame.draw.ellipse(SCREEN, (0,0,0), [609+self.x,309+self.y, 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [615+self.x, 315+self.y, 7, 15])
                #꽁지2
        pygame.draw.ellipse(SCREEN, (0,0,0), [623+self.x,309+self.y, 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [629+self.x, 315+self.y, 7, 15])
                #꽁지3
        pygame.draw.ellipse(SCREEN, (0,0,0), [636+self.x,309+self.y, 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [642+self.x, 315+self.y, 7, 15]) 

                # 눈
        pygame.draw.line(SCREEN, (0,0,0), [613+self.x,370+self.y], [613+self.x,399+self.y], 6)
        pygame.draw.line(SCREEN, (0,0,0), [632+self.x,370+self.y], [632+self.x,399+self.y], 6)

                # 입
        pygame.draw.line(SCREEN, (0,0,0), [600+self.x,409+self.y], [625+self.x,437+self.y], 6)
        pygame.draw.line(SCREEN, (0,0,0), [644+self.x,408+self.y], [625+self.x,437+self.y], 6)

                # 오른팔
        pygame.draw.line(SCREEN, (0,0,0), [697+self.x+25.6*math.cos(self.right_arm),386+self.y+25.6*math.sin(self.right_arm)], [681+self.x,406+self.y], 6)
        pygame.draw.ellipse(SCREEN, (0,0,0), [684+self.x+25.6*math.cos(self.right_arm),368+self.y+25.6*math.sin(self.right_arm), 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [690+self.x+25.6*math.cos(self.right_arm), 374+self.y+25.6*math.sin(self.right_arm), 7, 15])

                # 왼팔
        pygame.draw.line(SCREEN, (0,0,0), [574+self.x,417+self.y], [552+self.x-25.6*math.cos(self.left_arm),401+self.y+25.6*math.sin(self.left_arm)], 6)

        pygame.draw.ellipse(SCREEN, (0,0,0), [536+self.x-25.6*math.cos(self.left_arm), 386+self.y+25.6*math.sin(self.left_arm), 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [542+self.x-25.6*math.cos(self.left_arm), 392+self.y+25.6*math.sin(self.left_arm), 7, 15])

                # 오른다리
        pygame.draw.line(SCREEN, (0,0,0), [635+self.x,457+self.y], [635+self.x,478+self.y], 6) # r = 21

        pygame.draw.ellipse(SCREEN, (0,0,0), [631+self.x,477+self.y, 30, 16], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [637+self.x, 483+self.y, 20, 6])

                # 왼다리
        pygame.draw.line(SCREEN, (0,0,0), [614+self.x,457+self.y], [614+self.x,478+self.y], 6) 
        pygame.draw.ellipse(SCREEN, (0,0,0), [590+self.x,476+self.y, 30, 16], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [596+self.x,482+self.y, 20, 6]) 
        

    def move_x(self):
        self.x += self.dx
    def check_screen(self):
        if self.x >= self.right_max:
            self.x = self.right_max
        elif self.x <= self.left_max:
            self.x = self.left_max
    def jump(self, j):
        self.isJump = j
    def update(self):
        if self.isJump > 0:
            if self.isJump == 2:
                self.v = VELOCITY
            if self.v > 0:
                F = (0.5*self.m*(self.v*self.v))
            else:
                F = -(0.5*self.m*(self.v*self.v))
            self.y -= round(F)
            self.v -= 1
            
            if self.y > 0:
                self.y = 0
                self.isJump = 0
                self.v = VELOCITY
################################################
# dice function
# "1~6 사이 랜덤 정수 return"

def diceFeedback():
    global diceNumber1, diceNumber2
    diceNumber1 = random.randrange(1,7)
    diceNumber2 = random.randrange(1,7)
    feedback = f"{diceNumber1}, {diceNumber2}"
    return feedback

################################################
# Button class
# decides storyline

# 객체는 story class에 종속적인 것으로 만들기


################################################                    
class Button:
    def __init__(self, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.status = game_status
        self.font = pygame.font.SysFont("휴먼둥근헤드라인", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)
 
    def change_text(self, text, bg="black"):
        """Change the text when you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
    def show(self):
        SCREEN.blit(self.surface, (self.x, self.y))
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")
                    
    def changeStatus(self, event, status):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    global game_status
                    game_status = status

################################################                    
# game piece
class piece:
    def __init__(self):
        self.x = 730
        self.y = 20
        self.path = [[740, 430], [600,430], [460, 430],[350,430], [230,430], [130, 430], [20, 430], [20, 370], [20, 300], [20, 230], [20, 170], [20, 100], [20, 20], [120, 20], [230, 20], [370, 20], [490, 20], [620, 20], [730, 20], [730, 100], [730, 170], [730, 250], [730, 320], [730, 375], [730, 440]]
        self.location = 0
        
    def show(self):
        pygame.draw.rect(SCREEN, (53, 36, 115), [self.path[self.location][0], self.path[self.location][1],50,50])
               
    def move(self): #여기다가 dice 결과 변수 추가하기
        if self.location == len(self.path) -1:
            self.location = 0
        self.location += 1
    
    def showQuiz(self):
        ############################
        # 테스트용 함수             #
        if self.location == 15:
            global game_status
            game_status = "quiz"


################################################
# story class
# decides storyline

class story:
    def __init__(self) -> None:
        pass
    def background(self):
        global game_status
        if game_status == "main":
            SCREEN.blit(mainbackground, (0,0))
            
        elif game_status == "blue":
            SCREEN.blit(bluebackground, (0,0))
        
        elif game_status == "explain":
            SCREEN.blit(explainbackground, (0,0))
        
        elif game_status == "quiz":
            SCREEN.blit(quizbackground, (0,0))
            
    def conversation(self):
        global game_status
        if game_status == "main":
            pass
        elif game_status == "blue":
            pass
        
        # 여기서 해야하는 것=
        # 필요한 함수 
        # : 주사위 굴리기 - 던지기 버튼 만들기 done
        # : 말을 옮기기 - 말 위치 리스트 만들기 
        # : 장소 바꾸기 - game_status 추가하기
         
    def logic(self):
        pass

################################################
# main loop
def main():
    global SCREEN, WINDOW_WIDTH, WINDOW_HEIGHT, base, map_num, tkey

    map_num = 0
    tkey = 0
    trial = 0
    move = 0.2
    
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("happytomato")
    color = (255,255,255)
    SCREEN.fill(color)
    
    clock = pygame.time.Clock()

    player = tomato()
    player.__init__()
    player.shape()
    
    horse = piece()
    horse.__init__()
    
    
    
    logic = story()
    logic.__init__()


    button1 = Button(
        "게임 시작", (475,160), font=20, bg=(53, 36, 115), feedback="게임 시작"
    )
    button2 = Button(
        "게임 설명", (475,200), font=20, bg=(53, 36, 115), feedback="게임 설명"
    )
    button3 = Button(
        "게임 종료", (475,240), font=20, bg=(53, 36, 115), feedback="게임 종료"
    )
        # 필요한 오브젝트 : 주사위 dice, 말 객체, 던지기 버튼, 이전 단계 버튼(home, explain, quit)
                
    dice = Button(
        "던지기", (365,240), font=30, bg=(97,78,217), feedback=diceFeedback()
    ) 
    home = Button(
        "홈 화면", (23,10), font=15, bg=(53, 36, 115), feedback="홈 화면"
    )
    explain = Button(
        "게임 설명", (80,10), font=15, bg=(53, 36, 115), feedback="게임 설명"
    )
    quit = Button(
        "게임 종료", (150,10), font=15, bg=(53, 36, 115), feedback="게임 종료"
    )     

                    
    playing = True

    while playing:
       

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.dx = 5
                elif event.key == pygame.K_LEFT:
                    player.dx = -5
                elif event.key == pygame.K_UP:
                    player.dy = -5
                elif event.key == pygame.K_DOWN:
                    player.dy = 5
                if event.key == pygame.K_SPACE:
                    if player.isJump == 0:
                        player.jump(1)
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.dx = 0
                elif event.key == pygame.K_LEFT:
                    player.dx = 0
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0]:
                    if button1.rect.collidepoint(x, y):
                        button1.change_text(button1.feedback, bg=(53, 36, 115))
                        button1.changeStatus(event, "blue")
                    if button2.rect.collidepoint(x, y):
                        button2.change_text(button2.feedback, bg=(53, 36, 115))
                        button2.changeStatus(event, "explain")
                        #button2.changeStatus(event)   -> 설명 창으로 넘어가도록 하기            
                    if button3.rect.collidepoint(x, y):
                        button3.change_text(button3.feedback, bg=(53, 36, 115))
                        event.type = pygame.QUIT

                    if dice.rect.collidepoint(x, y):
                        dice.change_text(dice.feedback, bg=(53,36,115))
                        #button3.changeStatus(event)    
                        horse.move()                                             
                    if home.rect.collidepoint(x, y):
                        home.change_text(home.feedback, bg=(53, 36, 115))
                        home.changeStatus(event, "main") 
                    if explain.rect.collidepoint(x, y):
                        explain.change_text(explain.feedback, bg=(53, 36, 115))
                        explain.changeStatus(event, "explain")
                        #button3.changeStatus(event)  
                    if quit.rect.collidepoint(x, y):
                        quit.change_text(quit.feedback, bg=(53, 36, 115))
                        event.type = pygame.QUIT

                                                                                             
        SCREEN.fill(color)
        
        logic.background()
        logic.conversation()
        logic.logic()

        
        
        if game_status == "main":
            button1.show()
            button2.show()
            button3.show()
            
        elif game_status == "blue":
            dice.show()
            home.show()
            explain.show()
            quit.show()
            horse.show()
            horse.showQuiz()
            
        elif game_status == "explain":
            explain.show()
            quit.show()
            home.show()
            
        elif game_status == "quiz":
            explain.show()
            quit.show()
            home.show()            
            
        # 필요한 오브젝트 : 주사위, 말 객체, 던지기 버튼, 이전 단계 버튼
        
        player.shape()
        player.move_x()
        
        player.update()
        player.check_screen()        
        
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()

################################################
if __name__ == '__main__':
    main()

