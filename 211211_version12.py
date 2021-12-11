#-*- coding: utf-8 -*-

################################################
#           author : Yong Ju Park              #
#           welcome to tomatoWorld!            #
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
global quiz_status
quiz_status = "none" #"game" "done" "tryagain"
global ans_status
ans_status = 0 #2 3 
global moksum
moksum = 5
global location
location = 0
global clickstream_blue, clickstream_explain
clickstream_blue = 0
clickstream_explain = 0
global index
index = 5

################################################

# import fonts
pygame.font.init()
font = pygame.font.SysFont('휴먼둥근헤드라인', 20)

# import images - characters

#############################
# 채린 / 세빈 : (맵이름) 설명
# import background
# import answers
quiz_start = pygame.image.load('./image_files/quiz_start.png')
quiz_start = pygame.transform.scale(quiz_start, (103,45)) #618 266 309 133 103 45

# import button names
game_start = pygame.image.load('./image_files/버튼_게임 시작.jpg')
game_start = pygame.transform.scale(game_start, (113,29))
game_explain = pygame.image.load('./image_files/버튼_게임 설명.png')
game_explain = pygame.transform.scale(game_explain, (110,30))
game_quit = pygame.image.load('./image_files/버튼_게임 종료.jpg')
game_quit = pygame.transform.scale(game_quit, (110,30))

 
main_explain = pygame.image.load('./image_files/버튼_게임 설명.png')
main_explain = pygame.transform.scale(main_explain, (60,17))

main_quit = pygame.image.load('./image_files/버튼_게임 종료.jpg')
main_quit = pygame.transform.scale(main_quit, (70,17))
 
main_home = pygame.image.load('./image_files/버튼_홈화면.png')
main_home = pygame.transform.scale(main_home, (53,17))


# import quiz
tomato_img = pygame.image.load('./image_files/nobackground_tomato.png')
tomato_img = pygame.transform.scale(tomato_img, (80, 80))

modebackground = pygame.image.load('./image_files/mode_buffer.png')
modebackground = pygame.transform.scale(modebackground, (800, 500))

mainbackground = pygame.image.load('./image_files/main.png')
mainbackground = pygame.transform.scale(mainbackground, (800, 500))
bluebackground = pygame.image.load('./image_files/blue.jpg')
bluebackground = pygame.transform.scale(bluebackground, (800, 500))
explainbackground = pygame.image.load('./image_files/explain.png')
explainbackground = pygame.transform.scale(explainbackground, (800, 500))
quizbackground = pygame.image.load('./image_files/example_quiz.png')
quizbackground = pygame.transform.scale(quizbackground, (800, 500))

tomato_img = pygame.image.load('./image_files/nobackground_tomato.png')
tomato_img = pygame.transform.scale(tomato_img, (80, 80))

blueintro_1 = pygame.image.load('./image_files/배경/슬라이드1.png')
blueintro_1 = pygame.transform.scale(blueintro_1, (800, 500))
blueintro_2 = pygame.image.load('./image_files/배경/슬라이드2.png')
blueintro_2 = pygame.transform.scale(blueintro_2, (800, 500))
blueintro_3 = pygame.image.load('./image_files/배경/슬라이드3.png')
blueintro_3 = pygame.transform.scale(blueintro_3, (800, 500))
blueintro_4 = pygame.image.load('./image_files/배경/슬라이드4.png')
blueintro_4 = pygame.transform.scale(blueintro_4, (800, 500))

explain_0 = pygame.image.load('./image_files/배경/배경.png')
explain_0 = pygame.transform.scale(explain_0, (800, 500))
explain_1 = pygame.image.load('./image_files/배경/슬라이드5.png')
explain_1 = pygame.transform.scale(explain_1, (800, 500))
explain_2 = pygame.image.load('./image_files/배경/슬라이드6.png')
explain_2 = pygame.transform.scale(explain_2, (800, 500))
explain_3 = pygame.image.load('./image_files/배경/슬라이드7.png')
explain_3 = pygame.transform.scale(explain_3, (800, 500))
explain_4 = pygame.image.load('./image_files/배경/슬라이드8.png')
explain_4 = pygame.transform.scale(explain_4, (800, 500))
explain_4 = pygame.image.load('./image_files/배경/슬라이드8.png')
explain_4 = pygame.transform.scale(explain_4, (800, 500))
explain_5 = pygame.image.load('./image_files/배경/슬라이드9.png')
explain_5 = pygame.transform.scale(explain_5, (800, 500))
explain_6 = pygame.image.load('./image_files/배경/슬라이드10.png')
explain_6 = pygame.transform.scale(explain_6, (800, 500))
explain_7 = pygame.image.load('./image_files/배경/슬라이드11.png')
explain_7 = pygame.transform.scale(explain_7, (800, 500))
explain_8 = pygame.image.load('./image_files/배경/슬라이드12.png')
explain_8 = pygame.transform.scale(explain_8, (800, 500))

explain_intro_1 = pygame.image.load('./image_files/배경/배경_intro/슬라이드1.png')
explain_intro_1 = pygame.transform.scale(explain_intro_1, (800, 500))
explain_intro_2 = pygame.image.load('./image_files/배경/배경_intro/슬라이드2.png')
explain_intro_2 = pygame.transform.scale(explain_intro_2, (800, 500))
explain_intro_3 = pygame.image.load('./image_files/배경/배경_intro/슬라이드3.png')
explain_intro_3 = pygame.transform.scale(explain_intro_3, (800, 500))
explain_intro_4 = pygame.image.load('./image_files/배경/배경_intro/슬라이드4.png')
explain_intro_4 = pygame.transform.scale(explain_intro_4, (800, 500))
explain_intro_5 = pygame.image.load('./image_files/배경/배경_intro/슬라이드5.png')
explain_intro_5 = pygame.transform.scale(explain_intro_5, (800, 500))
explain_intro_6 = pygame.image.load('./image_files/배경/배경_intro/슬라이드6.png')
explain_intro_6 = pygame.transform.scale(explain_intro_6, (800, 500))
explain_intro_7 = pygame.image.load('./image_files/배경/배경_intro/슬라이드7.png')
explain_intro_7 = pygame.transform.scale(explain_intro_7, (800, 500))
explain_intro_8 = pygame.image.load('./image_files/배경/배경_intro/슬라이드8.png')
explain_intro_8 = pygame.transform.scale(explain_intro_8, (800, 500))
explain_intro_9 = pygame.image.load('./image_files/배경/배경_intro/슬라이드9.png')
explain_intro_9 = pygame.transform.scale(explain_intro_9, (800, 500))
explain_intro_10 = pygame.image.load('./image_files/배경/배경_intro/슬라이드10.png')
explain_intro_10 = pygame.transform.scale(explain_intro_10, (800, 500))
explain_intro_11 = pygame.image.load('./image_files/배경/배경_intro/슬라이드11.png')
explain_intro_11 = pygame.transform.scale(explain_intro_11, (800, 500))

# import answers
answer = pygame.image.load('./image_files/example_quiz.png')
answer = pygame.transform.scale(answer, (800,500))

# import quiz
tropicalbackground = pygame.image.load('./image_files/example_quiz.png')
tropicalbackground = pygame.transform.scale(tropicalbackground, (800,500))

#quiz_1 = pygame.image.load('./image_files/quiz_location1.png')
#quiz_1 = pygame.transform.scale(quiz_1, (800,500))

#############################
# 채린: 1 설명
# import background

background_1 = pygame.image.load('./image_files/배경1.jpg')
background_1 = pygame.transform.scale(background_1, (800, 500)) 

# import quiz
quiz_1 = pygame.image.load('./image_files/문제1.jpg')
quiz_1 = pygame.transform.scale(quiz_1, (600,400)) 

#import answer
answer_1 = pygame.image.load('./image_files/해설1.png')
answer_1 = pygame.transform.scale(answer_1, (600,400))
############################# 

#############################
# 채린: 2 설명
# import background
background_2 = pygame.image.load('./image_files/배경2.jpg')
background_2 = pygame.transform.scale(background_2, (800, 500)) 

# import quiz
quiz_2 = pygame.image.load('./image_files/문제2.jpg')
quiz_2 = pygame.transform.scale(quiz_2, (600,400)) 

#import answer
answer_2 = pygame.image.load('./image_files/해설2.jpg')
answer_2 = pygame.transform.scale(answer_2, (600,400))
############################# 

#############################
# 채린: 3 설명
# import background
background_3 = pygame.image.load('./image_files/배경3.jpg')
background_3 = pygame.transform.scale(background_3, (800, 500)) 

# import quiz
quiz_3 = pygame.image.load('./image_files/문제3.jpg')
quiz_3 = pygame.transform.scale(quiz_3, (600,400)) 

#import answer
answer_3 = pygame.image.load('./image_files/해설3.jpg')
answer_3 = pygame.transform.scale(answer_3, (600,400))
############################# 

#############################
# 채린: 4 설명
# import background
background_4  = pygame.image.load('./image_files/배경4.jpg')
background_4 = pygame.transform.scale(background_4, (800, 500)) 

# import quiz
quiz_4 = pygame.image.load('./image_files/문제4.jpg')
quiz_4 = pygame.transform.scale(quiz_4, (600,400)) 

#import answer
answer_4 = pygame.image.load('./image_files/해설4.jpg')
answer_4 = pygame.transform.scale(answer_4, (600,400))
############################# 

#############################
# 채린: 5 설명
# import background
background_5 = pygame.image.load('./image_files/배경5.jpg')
background_5 = pygame.transform.scale(background_5, (800, 500)) 

# import quiz
quiz_5 = pygame.image.load('./image_files/문제5.jpg')
quiz_5 = pygame.transform.scale(quiz_5, (600,400)) 

#import answer
answer_5 = pygame.image.load('./image_files/해설5.jpg')
answer_5 = pygame.transform.scale(answer_5, (600,400))
############################# 
#############################
# 채린: 6 설명
# import background
background_6 = pygame.image.load('./image_files/퀴즈배경1.jpg')
background_6 = pygame.transform.scale(background_6, (800, 500))

# import quiz
quiz_6 = pygame.image.load('./image_files/퀴즈1.jpg')
quiz_6 = pygame.transform.scale(quiz_6, (600,400))

#import answer
answer_6 = pygame.image.load('./image_files/퀴즈해설1.jpg')
answer_6 = pygame.transform.scale(answer_6, (600,400))


#############################
# 채린: 13 설명
# import background
background_13 = pygame.image.load('./image_files/배경6.jpg')
background_13 = pygame.transform.scale(background_13, (800, 500)) 

# import quiz
quiz_13 = pygame.image.load('./image_files/문제6.jpg')
quiz_13 = pygame.transform.scale(quiz_13, (600,400)) 

#import answer
answer_13 = pygame.image.load('./image_files/해설6.jpg')
answer_13 = pygame.transform.scale(answer_13, (600,400))
############################# 

#############################
# 채린: 14 설명
# import background
background_14 = pygame.image.load('./image_files/배경7.jpg')
background_14 = pygame.transform.scale(background_14, (800, 500)) 

# import quiz
quiz_14 = pygame.image.load('./image_files/문제7.jpg')
quiz_14 = pygame.transform.scale(  quiz_14, (600,400)) 

#import answer
answer_14 = pygame.image.load('./image_files/해설7.jpg')
answer_14 = pygame.transform.scale(  answer_14, (600,400))
############################# 

#############################
# 채린: 16 설명
# import background
background_16 = pygame.image.load('./image_files/배경8.jpg')
background_16 = pygame.transform.scale(background_16, (800, 500)) 

# import quiz
quiz_16 = pygame.image.load('./image_files/문제8.jpg')
quiz_16 = pygame.transform.scale( quiz_16, (600,400)) 

#import answer
answer_16 = pygame.image.load('./image_files/해설8.jpg')
answer_16 = pygame.transform.scale( answer_16, (600,400))
############################# 

#############################
# 채린: 17 설명
# import background
background_17 = pygame.image.load('./image_files/배경9.jpg')
background_17 = pygame.transform.scale( background_17, (800, 500)) 

# import quiz
quiz_17 = pygame.image.load('./image_files/문제9.jpg')
quiz_17 = pygame.transform.scale( quiz_17, (600,400)) 

#import answer
answer_17 = pygame.image.load('./image_files/해설9.jpg')
answer_17 = pygame.transform.scale( answer_17, (600,400))
#############################
#############################
# 채린: 18 설명
# import background
background_18 = pygame.image.load('./image_files/퀴즈배경2.jpg')
background_18 = pygame.transform.scale(background_18, (800, 500))

# import quiz
quiz_18 = pygame.image.load('./image_files/퀴즈2.jpg')
quiz_18 = pygame.transform.scale(quiz_18, (600,400))

#import answer
answer_18 = pygame.image.load('./image_files/퀴즈해설2.jpg')
answer_18 = pygame.transform.scale(answer_18, (600,400))
#############################


# 세빈: 7 설명
# import background
background_7 = pygame.image.load('./image_files/건조지형 배경_최종.png')
background_7 = pygame.transform.scale(background_7, (800, 500))

# import quiz
quiz_7 = pygame.image.load('./image_files/건조지형 문제_최종.png')
quiz_7 = pygame.transform.scale( quiz_7, (600,400))

#import answer
answer_7 = pygame.image.load('./image_files/건조지형 해설_최종.png')
answer_7 = pygame.transform.scale( answer_7, (600,400))
#############################

#############################
# 세빈: 8 설명
# import background
background_8 = pygame.image.load('./image_files/빙하지형 배경 (1)_최종.png')
background_8 = pygame.transform.scale( background_8, (800, 500)) 

# import quiz
quiz_8 = pygame.image.load('./image_files/빙하지형 문제_최종.png')
quiz_8 = pygame.transform.scale( quiz_8, (600,400)) 

#import answer
answer_8 = pygame.image.load('./image_files/빙하지형 해설_최종.png')
answer_8 = pygame.transform.scale( answer_8, (600,400))
############################# 

#############################
# 세빈: 10 설명
# import background
background_10 = pygame.image.load('./image_files/해안지형 배경_최종.png')
background_10 = pygame.transform.scale(background_10, (800, 500)) 

# import quiz
quiz_10 = pygame.image.load('./image_files/해안지형 문제_최종.png')
quiz_10 = pygame.transform.scale( quiz_10, (600,400)) 

#import answer
answer_10 = pygame.image.load('./image_files/해안지형 해설_최종.png')
answer_10 = pygame.transform.scale( answer_10, (600,400))
############################# 

#############################
# 세빈: 11 설명
# import background
background_11 = pygame.image.load('./image_files/화산지형 배경_최종.png')
background_11 = pygame.transform.scale( background_11, (800, 500)) 

# import quiz
quiz_11 = pygame.image.load('./image_files/화산 지형 문제_최종.png')
quiz_11 = pygame.transform.scale( quiz_11, (600,400)) 

#import answer
answer_11 = pygame.image.load('./image_files/화산 지형 해설_최종.png')
answer_11 = pygame.transform.scale( answer_11, (600,400))
############################# 
#############################
# 세빈: 12 설명
# import background
background_12 = pygame.image.load('./image_files/나라퀴즈 배경_최종.png')
background_12 = pygame.transform.scale(background_12, (800, 500))

# import quiz
quiz_12 = pygame.image.load('./image_files/나라퀴즈 문제_최최종.png')
quiz_12 = pygame.transform.scale(quiz_12, (600,400))

#import answer
answer_12 = pygame.image.load('./image_files/나라퀴즈 해설_최종.png')
answer_12 = pygame.transform.scale(answer_12, (600,400))
#############################

#############################
# 세빈: 19 설명
# import background
background_19 = pygame.image.load('./image_files/음식1 배경_최종.png')
background_19 = pygame.transform.scale( background_19, (800, 500)) 

# import quiz
quiz_19 = pygame.image.load('./image_files/음식1 문제_최종.png')
quiz_19 = pygame.transform.scale( quiz_19, (600,400)) 

#import answer
answer_19 = pygame.image.load('./image_files/음식1 해설_최종.png')
answer_19 = pygame.transform.scale( answer_19, (600,400))
############################# 

#############################
# 세빈: 20 설명
# import background
background_20 = pygame.image.load('./image_files/음식2 배경_최종.png')
background_20 = pygame.transform.scale( background_20, (800, 500)) 

# import quiz
quiz_20 = pygame.image.load('./image_files/음식2 문제_최종.png')
quiz_20 = pygame.transform.scale( quiz_20, (600,400)) 

#import answer
answer_20 = pygame.image.load('./image_files/음식2 해설_최종.png')
answer_20 = pygame.transform.scale( answer_20, (600,400))
############################# 

#############################
# 세빈: 22 설명
# import background
background_22 = pygame.image.load('./image_files/축제 배경_최종.png')
background_22 = pygame.transform.scale( background_22, (800, 500)) 

# import quiz
quiz_22 = pygame.image.load('./image_files/축제 문제_최종.png')
quiz_22 = pygame.transform.scale( quiz_22, (600,400)) 

#import answer
answer_22 = pygame.image.load('./image_files/축제 해설_최종.png')
answer_22 = pygame.transform.scale( answer_22, (600,400))
############################# 

#############################
# 세빈: 23 설명
# import background
background_23 = pygame.image.load('./image_files/주거 배경_최종.png')
background_23 = pygame.transform.scale( background_23, (800, 500)) 

# import quiz
quiz_23 = pygame.image.load('./image_files/주거 문제_최종.png')
quiz_23 = pygame.transform.scale( quiz_23, (600,400)) 

#import answer
answer_23 = pygame.image.load('./image_files/주거 해설_최종.png')
answer_23 = pygame.transform.scale( answer_23, (600,400))
############################# 
#import effects
add1 = pygame.image.load('./image_files/add1.jpg')
add1 = pygame.transform.scale( add1, (800,500))

add2 = pygame.image.load('./image_files/add2.jpg')
add2 = pygame.transform.scale( add2, (800,500))

subtract1 = pygame.image.load('./image_files/subtract1.jpg')
subtract1 = pygame.transform.scale( subtract1, (800,500))

move2 = pygame.image.load('./image_files/앞으로 두 칸.jpg')
move2 = pygame.transform.scale( move2, (800,500))

move1 = pygame.image.load('./image_files/한 칸 이동.jpg')
move1 = pygame.transform.scale( move1, (800,500))

win = pygame.image.load('./image_files/win.png')
win = pygame.transform.scale( win, (800,500))

fail = pygame.image.load('./image_files/fail.png')
fail = pygame.transform.scale( fail, (800,500))

rule = pygame.image.load('./image_files/rule.png')
rule = pygame.transform.scale( rule, (800,500))

tryagain_1 = pygame.image.load('./image_files/재도전.jpg')
tryagain_1 = pygame.transform.scale( tryagain_1, (800,500))

############################# 

################################################
# tomato class
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

def diceFeedback():
    global diceNumber
    diceNumber = 1
    # 임시로 바꿔둠 random.randrange(1,4)
    feedback = f"{diceNumber}"
    return feedback

################################################
# Button class
                  
class Button:
    def __init__(self, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.status = game_status
        self.quiz = quiz_status
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
                    
    def done(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    pass
                
    def quizStatus(self, event, status):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    global quiz_status
                    quiz_status = status
                    
    def ansStatus(self, event, status):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    global ans_status
                    ans_status = status
                                                            
################################################                    
# game piece
class piece:
    def __init__(self):
        self.x = 730
        self.y = 20
        self.done = "yet"
        self.path = [[740, 430], [600,430], [460, 430],[350,430], [230,430], [130, 430], [20, 430], [20, 370], [20, 300], [20, 230], [20, 170], [20, 100], [20, 20], [120, 20], [230, 20], [370, 20], [490, 20], [620, 20], [730, 20], [730, 100], [730, 170], [730, 250], [730, 320], [730, 375], [730, 440]]
        self.location = 0
        self.destination = 0
        
    def move(self): #여기다가 dice 결과 변수 추가하기
        self.destination = self.location + diceNumber  
              
    def show(self):
        if self.location >= len(self.path) - 1:
            self.location = 0
        
        for i in range(self.location, self.destination+1):
            SCREEN.blit(tomato_img, (self.path[i][0], self.path[i][1]))           
            if i == self.destination:
                self.location = i
    
    def showQuiz(self):
        if self.done == "yet" and self.location != 0:
            global game_status
            global location
            game_status = "quiz"    
            location = self.location          
################################################                    
# game life

class life:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.check = 5
        self.do_update = True
        
    def show(self):
        score = font.render(f"물병 : {self.check}", True, (121,182,83))
        SCREEN.blit(score, (530, 190)) 
        
    def update(self, up):
        if self.do_update == True:
            self.check += up
            self.do_update = False
    
    def gameover(self):
        if self.check == 0:
            score = font.render("GAMEOVER", True, (0,0,0))
            SCREEN.blit(score, (500, 140))        
            
        game_status = "main"    
            
    def win(self, loca):
        if loca > 20:
            score = font.render("게임 승리!", True, (255,0,0))
            SCREEN.blit(score, (300, 140)) 
                        
################################################
# story class
class story:
    def __init__(self) -> None:
        global button1, button2, button3
        button1 = Button(
            "게임 시작", (475,160), font=20, bg=(121,182,83), feedback="게임 시작"
        )
        button2 = Button(
            "게임 설명", (475,200), font=20, bg=(121,182,83), feedback="게임 설명"
        )
        button3 = Button(
            "게임 종료", (475,240), font=20, bg=(121,182,83), feedback="게임 종료"
        )   
        
        global home, explain, quit    
        home = Button(
            "홈 화면", (23,10), font=15, bg=(121,182,83), feedback="홈 화면"
        )
        explain = Button(
            "게임 설명", (80,10), font=15, bg=(121,182,83), feedback="게임 설명"
        )
        quit = Button(
            "게임 종료", (150,10), font=15, bg=(121,182,83), feedback="게임 종료"
        )        
        
        global intro, main
        
        intro = Button(
            "처음이에요 : 게임 설명", (480,240), font=20, bg=(135,153,121), feedback="처음이에요 : 게임 설명"
        )
    
        main = Button(
            "할 줄 알아요 : 게임 시작", (474,320), font=20, bg=(135,153,121), feedback="할 줄 알아요 : 게임 시작"
        )        
        
        global bottle
        bottle = life()
        bottle.__init__()   
        
        global quiz, ans1, ans2, ans3, dice, ans4, ans5
        quiz = Button(
            "퀴즈 시작", (320,250), font=40, bg=(121,182,83), feedback="퀴즈 시작"
        )     
        
        ans1 = Button(
            "①", (150,400), font=30, bg=(121,182,83), feedback="①"
        )
        ans2 = Button(
            "②", (210,400), font=30, bg=(121,182,83), feedback="②"
        )
        ans3 = Button(
            "③", (270,400), font=30, bg=(121,182,83), feedback="③"
        )  
        ans4 = Button(
            "④", (330,400), font=30, bg=(121,182,83), feedback="④"
        )
        ans5 = Button(
            "⑤", (390,400), font=30, bg=(121,182,83), feedback="⑤"
        )              
        
        dice = Button(
            "던지기", (365,350), font=30, bg=(121,182,83), feedback=diceFeedback()
        )     

        global retry
        retry = Button(
            "다시 도전하시겠습니까?", (250,180), font=30, bg=(0,0,0), feedback="다시 도전하시겠습니까?"
        ) 
        global yes
        yes = Button(
            "좋아요", (230,380), font=30, bg=(211,238,247), feedback="좋아요"
        )         
        
        global no
        no = Button(
            "싫어요", (530,380), font=30, bg=(211,238,247), feedback="싫어요"
        ) 
        
        global backtoblue
        backtoblue = Button(
            "다음 문제 풀러가기", (475,160), font=30, bg=(121,182,83), feedback="다음 문제 풀러가기"
        )
                        
        global horse
        horse = piece()
        horse.__init__()      
        
        
    def background(self):
        global game_status, clickstream_explain
        if game_status == "main":
            SCREEN.blit(mainbackground, (0,0))
            
            button1.show()
            SCREEN.blit(game_start, (475,160))
            button2.show()
            SCREEN.blit(game_explain, (475,200))
            button3.show()
            SCREEN.blit(game_quit, (475,240))
            
        elif game_status == "buffer":
            SCREEN.blit(modebackground, (0,0))
            
            explain.show()
            
            quit.show()
            home.show()
            intro.show()
            
            #SCREEN.blit(main_home, (23,10)) 
            #SCREEN.blit(main_explain, (80,10))
            #SCREEN.blit(main_quit, (150,10))
            
            main.show()              
            
        elif game_status == "blue":
            if clickstream_blue == 0:
                SCREEN.blit(blueintro_1, (0,0))
            elif clickstream_blue == 1:
                SCREEN.blit(blueintro_2, (0,0))
            elif clickstream_blue == 2:
                SCREEN.blit(blueintro_3, (0,0))
            elif clickstream_blue == 3:
                SCREEN.blit(blueintro_4, (0,0))
            else:    
                SCREEN.blit(bluebackground, (0,0)) 
                dice.show()
            
                bottle.show()
                bottle.win(location)
                bottle.gameover()
                
                #horse.move()
                horse.show()
                horse.showQuiz()            
            
            home.show()
            explain.show()
            quit.show()
            
        elif game_status == "explain":
            if clickstream_explain == 0:
                SCREEN.blit(explain_0, (0,0))
            elif clickstream_explain == 1:
                SCREEN.blit(explain_intro_1, (0,0))
                #SCREEN.blit(explain_1, (0,0))
            elif clickstream_explain == 2:
                SCREEN.blit(explain_intro_2, (0,0))
                #SCREEN.blit(explain_2, (0,0))                
            elif clickstream_explain == 3:
                SCREEN.blit(explain_intro_3, (0,0))
                #SCREEN.blit(explain_3, (0,0))
            elif clickstream_explain == 4:
                SCREEN.blit(explain_intro_4, (0,0))
                #SCREEN.blit(explain_4, (0,0))
            elif clickstream_explain == 5:
                SCREEN.blit(explain_intro_5, (0,0))
                #SCREEN.blit(explain_5, (0,0))
            elif clickstream_explain == 6:
                SCREEN.blit(explain_intro_6, (0,0))
                #SCREEN.blit(explain_6, (0,0))
            elif clickstream_explain == 7:
                SCREEN.blit(explain_intro_7, (0,0))
            elif clickstream_explain == 8:
                SCREEN.blit(explain_intro_8, (0,0))                
            elif clickstream_explain == 9:
                SCREEN.blit(explain_intro_9, (0,0))                
            elif clickstream_explain == 10:
                SCREEN.blit(explain_intro_10, (0,0))                
            elif clickstream_explain == 11:
                SCREEN.blit(explain_intro_11, (0,0))
            elif clickstream_explain >= 12:
                game_status = "blue"
                init_click = 0
                
                                                                                                
            explain.show()
            quit.show()
            home.show()
            
            
            
            
                    
        elif game_status == "quiz":
            SCREEN.blit(quizbackground, (0,0))
            
            explain.show()
            quit.show()
            home.show()  

            button1.show()  
            bottle.show()
            
            quiz.show()
            SCREEN.blit(quiz_start, (100,100))
                            
################################################################################################
#                                  1번 문제 관련 루프                                           #
################################################################################################

            
            if location == 1:
                
                SCREEN.blit(background_1, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                quiz.show()  
                SCREEN.blit(quiz_start, (100,100))         

                global quiz_status
                
                if quiz_status == "game":
                    SCREEN.blit(quiz_1, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()                    
                    
                    # 정답
                    if ans_status == 5:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif 1 <= ans_status < 5:
                        
                        bottle.update(-1)
                        
                        SCREEN.blit(tryagain_1, (0,0)) 
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(background_1, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_1, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                                  
                    # 대도전해서 정답      
                    if ans_status == 5:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                    elif 1 <= ans_status < 5:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_1, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()   
                       
                else:
                    pass  
################################################################################################
#                                  2번 문제 관련 루프                                           #
################################################################################################
            if location == 2:
                
                SCREEN.blit(background_2, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           

                if quiz_status == "game":
                    SCREEN.blit(quiz_2, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 2:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 1 or 3 <= ans_status <= 5:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(quiz_2, (100,70))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 2:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                    elif ans_status == 1 or 3 <= ans_status <= 5:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_2, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()         
                        

################################################################################################
#                                  3번 문제 관련 루프                                           #
################################################################################################
            if location == 3:
                
                SCREEN.blit(background_3, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_3, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 2:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 1 or 3 <= ans_status <= 5:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(quiz_3, (100,70))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 2:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                    elif ans_status == 1 or 3<= ans_status <= 5:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_3, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()        
                        
################################################################################################
#                                  4번 문제 관련 루프                                           #
################################################################################################
            if location == 4:
                
                SCREEN.blit(background_4, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_4, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 3:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif 1<= ans_status <= 2 or  4<= ans_status <= 5:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                
                if quiz_status == "tryagain":
                    SCREEN.blit(background_4, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_4, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 3:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                    elif  1<= ans_status <= 2 or  4<= ans_status <= 5:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_4, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()            
                    
################################################################################################
#                                  5번 문제 관련 루프                                           #
################################################################################################
            if location == 5:
                
                SCREEN.blit(background_5, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_5, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit( background_5, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_5, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_5, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()          
################################################################################################
#                                  6번 문제 관련 루프                                          #
################################################################################################
            if location == 6:
                
                SCREEN.blit(background_6, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_6, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(background_6, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_6, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)      
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_6, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()         
                    
################################################################################################
#                                  7번 문제 관련 루프                                           #
################################################################################################
            if location == 7:
                
                SCREEN.blit( background_7, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_7, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit( background_7, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_7, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_7, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()    
                    
                                                
################################################################################################
#                                  8번 문제 관련 루프                                           #
################################################################################################
            if location == 8:
                
                SCREEN.blit( background_8, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    

                
                quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_8, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit( background_8, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_8, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_8, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show() 
                      
################################################################################################
#                                  9번 문제 관련 루프                                        #
################################################################################################
            if location == 9:
                #global index
                ranm = [add1, add2, subtract1, move2] 
                SCREEN.blit(ranm[index], (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                #quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_1, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(tropicalbackground, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_1, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show() 
                       
################################################################################################
#                                  10번 문제 관련 루프                                           #
################################################################################################
            if location == 10:
                
                SCREEN.blit(background_10, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_10, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 3:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif 1<= ans_status <= 2 or 4<=ans_status<=5:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit( background_10, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_10, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 3:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif 1<= ans_status <= 2 or 4<=ans_status<=5:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_10, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show() 
                    
                    
################################################################################################
#                                  11번 문제 관련 루프                                           #
################################################################################################
            if location == 11:
                
                SCREEN.blit( background_11, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_11, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit( background_11, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_11, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_11, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show() 
                    
                                                           
################################################################################################
#                                  12번 문제 관련 루프  - 준비 중                                          #
################################################################################################
            if location == 12:
                
                SCREEN.blit( background_12, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_12, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit( background_2, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_12, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_2, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()  
                                                                                  
################################################################################################
#                                  13번 문제 관련 루프                                           #
################################################################################################
            if location == 13:
                
                SCREEN.blit( background_13, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           
 
                
                if quiz_status == "game":
                    SCREEN.blit(quiz_13, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif 2 <= ans_status:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(background_13, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_13, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status >= 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_13, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                                          
################################################################################################
#                                  14번 문제 관련 루프                                           #
################################################################################################
            if location == 14:
                
                SCREEN.blit( background_14, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           
 
                
                if quiz_status == "game":
                    SCREEN.blit(quiz_14, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status >= 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit( background_14, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_14, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                    elif ans_status >= 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_14, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show() 
                                        
################################################################################################
#                                  15번 문제 관련 루프    - 준비 중                                        #
################################################################################################
            if location == 15:
                #global index
                ranm = [add1, add2, subtract1, move2] 
                SCREEN.blit(ranm[index], (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                #quiz.show()           
 
                
                if quiz_status == "game":
                    SCREEN.blit(quiz_1, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(tropicalbackground, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_1, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show() 
                     
################################################################################################
#                                  16번 문제 관련 루프                                           #
################################################################################################
            if location == 16:
                
                SCREEN.blit( background_16, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           
 
                
                if quiz_status == "game":
                    SCREEN.blit(quiz_16, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(background_16, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_16, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_16, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show() 
                    
                                        
################################################################################################
#                                  17번 문제 관련 루프                                           #
################################################################################################
            if location == 17:
                
                SCREEN.blit(background_17, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           
 
                
                if quiz_status == "game":
                    SCREEN.blit(quiz_17, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(background_17, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_17, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_17,(100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()   
                                                                              
################################################################################################
#                                  18번 문제 관련 루프                                           #
################################################################################################
            if location == 18:
                
                SCREEN.blit(background_18, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_18, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()     
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(background_18, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_18, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_18, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show() 
                                          
################################################################################################
#                                  19번 문제 관련 루프                                           #
################################################################################################
            if location == 19:
                SCREEN.blit(background_19, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_19, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(background_19, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_19, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_19, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show() 
                    
                      
################################################################################################
#                                  20번 문제 관련 루프                                           #
################################################################################################
            if location == 20:
                
                SCREEN.blit(background_20, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_20, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 4:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif 1<= ans_status <= 3 or ans_status == 5:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(background_20, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_20, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 4:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                    elif 1<= ans_status <= 3 or ans_status == 5:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                        
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_20, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show() 
                    
                     
################################################################################################
#                                  21번 문제 관련 루프                                      #
################################################################################################
            if location == 21:
                #global index
                ranm = [add1, add2, subtract1, move2] 
                SCREEN.blit(ranm[index], (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                #quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_1, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(tropicalbackground, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_1, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()     
                    
                                                       
################################################################################################
#                                  22번 문제 관련 루프                                           #
################################################################################################
            if location == 22:
                
                SCREEN.blit(background_22, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_22, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(background_22, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_22, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_22, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show() 
                    
                      
################################################################################################
#                                  23번 문제 관련 루프                                           #
################################################################################################
            if location == 23:
                
                SCREEN.blit(background_23, (0,0))
                
                explain.show()
                quit.show()
                home.show()     
                  
                button1.show()  
                bottle.show()    
                
                
                #score = font.render("요기가 어디징~", True, (255,0,0))
                #SCREEN.blit(score, (200,200))  
                
                quiz.show()           

                
                if quiz_status == "game":
                    SCREEN.blit(quiz_23,(100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                        
                        bottle.update(1)
                        
                        
                    elif ans_status == 2:
                        
                        bottle.update(-1)
                        
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))

                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                        
                    elif ans_status == 3:
                        
                        bottle.update(-1)
                            
                        #SCREEN.fill((255,0,0))
                        SCREEN.blit(tryagain_1, (0,0))
                        # 다시 도전하시겠습니까? 버튼 만들기
                        #retry.show()
                        yes.show()
                        no.show()
                                                
                if quiz_status == "tryagain":
                    SCREEN.blit(background_23, (0,0))
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()
                    
                    SCREEN.blit(quiz_23, (100,70))
                    ans1.show()
                    ans2.show()
                    ans3.show()
                    ans4.show()
                    ans5.show()   
                    
                    if ans_status == 1:
                        
                        bottle.update(1)
                                                  
                        quiz_status = "done"
                        game_status = "blue"
                        horse.done = "done"
                    elif ans_status == 2:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                    elif ans_status == 3:
                        quiz_status = "answer"
                        game_status = "quiz"
                        horse.done = "done"
                
                if quiz_status == "answer":
                    SCREEN.blit(answer_23, (100,70))
                    # 해설 그림으로 바꾸기 :)
                    
                    explain.show()
                    quit.show()
                    home.show()
                    
                    button1.show()
                    bottle.show()    
                
            if location == 24:
                SCREEN.blit(win,(0,0)) 
                explain.show()
                quit.show()
                home.show()
                                
                button1.show()
                bottle.show()      
                                                                                      
    
                                                                                                                                                                                                      
    def conversation(self):
        pass
         
    def logic(self):
        pass

################################################
# main loop
def main():
    global SCREEN, WINDOW_WIDTH, WINDOW_HEIGHT, life, index

    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("happyTomatoLife")
    color = (255,255,255)
    SCREEN.fill(color)
    
    clock = pygame.time.Clock()

    player = tomato()
    player.__init__()
    player.shape()
    
    
    logic = story()
    logic.__init__()
    logic.background()
    logic.conversation()
    logic.logic()    
                        
    playing = True

    while playing:
       
        SCREEN.fill(color)
        
        logic.background()
        logic.conversation()
        logic.logic()          
        
        global ans_status

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
                    global clickstream_blue, clickstream_explain
                    if game_status == "blue":
                        clickstream_blue += 1
                    elif game_status == "explain":
                        clickstream_explain += 1
                    if button1.rect.collidepoint(x, y):
                        button1.change_text(button1.feedback, bg=(121,182,83))
                        #button1.changeStatus(event, "buffer")       
                        if game_status == "quiz":
                            button1.changeStatus(event, "blue")  
                            horse.done = "done"
                        elif game_status == "answer":
                            button1.changeStatus(event, "blue")
                            button1.quizStatus(event, "done")
                            horse.done = "done"
                        else:
                            button1.changeStatus(event, "buffer")
                            
                    if button2.rect.collidepoint(x, y):
                        button2.change_text(button2.feedback, bg=(121,182,83))
                        button2.changeStatus(event, "explain")        
                    if button3.rect.collidepoint(x, y):
                        button3.change_text(button3.feedback, bg=(121,182,83))
                        event.type = pygame.QUIT
                        
                    if intro.rect.collidepoint(x, y):
                        intro.change_text(intro.feedback, bg=(135,153,121))
                        intro.changeStatus(event, "explain")
                        
                    if quiz.rect.collidepoint(x, y):
                        quiz.change_text(quiz.feedback, bg=(121,182,83)) 
                        quiz.quizStatus(event, "game")               
                    if ans1.rect.collidepoint(x, y):
                        ans1.change_text(ans1.feedback, bg=(121,182,83)) 
                        ans1.ansStatus(event, 1)  
                    if ans2.rect.collidepoint(x, y):
                        ans2.change_text(ans2.feedback, bg=(121,182,83)) 
                        ans2.ansStatus(event, 2)  
                    if ans3.rect.collidepoint(x, y):
                        ans3.change_text(ans3.feedback, bg=(121,182,83)) 
                        ans3.ansStatus(event, 3)   
                    if ans4.rect.collidepoint(x, y):
                        ans4.change_text(ans4.feedback, bg=(121,182,83)) 
                        ans4.ansStatus(event, 4)      
                    if ans5.rect.collidepoint(x, y):
                        ans5.change_text(ans5.feedback, bg=(121,182,83)) 
                        ans5.ansStatus(event, 5)      
                                                                                                                                                                       
                    if main.rect.collidepoint(x, y):
                        main.change_text(main.feedback, bg=(135,153,121) )
                        main.changeStatus(event, "blue")   
                                    
                    if retry.rect.collidepoint(x, y):
                        retry.change_text(retry.feedback, bg=(0,0,0)) 
                        #retry.quizStatus(event, "tryagain")     
                    if yes.rect.collidepoint(x, y):
                        yes.change_text(yes.feedback, bg=(211,238,247)) 
                        yes.quizStatus(event, "tryagain")       
                        ans_status = 0
                    if no.rect.collidepoint(x, y):
                        no.change_text(no.feedback, bg=(211,238,247)) 
                        no.quizStatus(event, "answer")     
                          
                    if backtoblue.rect.collidepoint(x, y):
                        backtoblue.change_text(backtoblue.feedback, bg=(121,182,83))
                        backtoblue.changeStatus(event, "blue") 
                        backtoblue.quizStatus(event, "done") 
                                                                                                                                
                    if dice.rect.collidepoint(x, y):
                        dice.feedback = diceFeedback()
                        dice.change_text(dice.feedback, bg=(121,182,83))
                        horse.done = "yet"
                        ans_status = 0
                        horse.move()
                        pygame.display.update()  
                        
                        if horse.destination == 9 or horse.destination == 21 or horse.destination == 15:
                            index = random.randint(0,3)        
                                                                    
                    if home.rect.collidepoint(x, y):
                        home.change_text(home.feedback, bg=(121,182,83))
                        home.changeStatus(event, "main") 
                    if explain.rect.collidepoint(x, y):
                        explain.change_text(explain.feedback, bg=(121,182,83))
                        explain.changeStatus(event, "explain")
                    if quit.rect.collidepoint(x, y):
                        quit.change_text(quit.feedback, bg=(121,182,83))
                        event.type = pygame.QUIT

                                                                                        
        #player.shape()
        #player.move_x()
        
        #player.update()
        #player.check_screen()        
        
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()

################################################
if __name__ == '__main__':
    main()