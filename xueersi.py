# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:07:22 2019

@author: 沈筠昕
"""

from turtle import*
from random import*
from time import*

cards = [ [2, 4, 7, 8],
          [3, 5, 9, 9],
          [6, 7, 8, 9],
          [4, 7, 8, 9],
          [1, 2, 2, 6],
          [2, 3, 5, 6],
          [2, 4, 4, 6],
          [3, 3, 6, 7],
          [3, 4, 7, 7]]
          
def heart_arc():
    for i in range(20):
        right(10)
        forward(4)

def draw_heart(x, y):
    color('red', 'red')  
    penup()
    goto(x, y)
    down()
    speed(0)
    left(140)
    begin_fill()
    forward(50)
    heart_arc()
    left(130)
    heart_arc()
    forward(50)
    end_fill()
  
def spade_arc():
    for i in range(20):
        left(10)
        forward(4)
        
def draw_spade(x, y):
    color('black', 'black')  
    up()
    goto(x, y)
    down()
    speed(0)
    right(40)
    begin_fill()
    forward(48)
    heart_arc()
    left(125)
    heart_arc()
    forward(48)
    end_fill()
    up()
    goto(x, y-60)
    setheading(0)
    down()
    begin_fill()
    right(60)
    forward(30)
    right(120)
    forward(30)
    end_fill()

def draw_club(x, y):
    color('black', 'black')  
    up()
    goto(x, y)
    speed(0)
    down()
    begin_fill()
    circle(20)
    end_fill()
    up()
    goto(x-20, y-30)
    down()
    begin_fill()
    circle(20)
    end_fill()
    up()
    goto(x+20, y-30)
    down()
    begin_fill()
    circle(20)
    end_fill()
    up()
    goto(x, y-20)
    down()
    begin_fill()
    right(60)
    forward(30)
    right(120)
    forward(30)
    end_fill()
    
def draw_diamond(x,y):
    goto(x,y)
    color("red", "red")
    pendown()
    begin_fill()
    right(60)
    forward(50)
    right(60)
    forward(50)
    right(120)
    forward(50)
    end_fill()
    
def puke_single(x, y, number, type):
    speed(0)
    penup()
    goto(x,y)
    setheading(0)
    if(type==0 or type==2):
        color("black")
    else:
        color("red")
    pendown()
    forward(160)
    right(90)
    forward(240)
    right(90)
    forward(160)
    right(90)
    forward(240)
    right(90)
    penup()
    if(type == 0):
        draw_spade(x+80, y-80)
    elif(type == 1):
        draw_heart(x+80, y-160)
    elif(type == 2):
        draw_club(x+80, y-120)
    elif(type == 3):
        draw_diamond(x+80, y-80)
    penup()
    goto(x+10, y-50)
    write(number, font=('Arial',40))
    goto(x+120, y-230)
    write(number, font=('Arial',40))
    hideturtle()
         
def caculate_mul(exp):
    for i in range(len(exp)):
        if(exp[i] == '*'):
            sum = int(exp[i-1]) * int(exp[i+1])
            exp = exp[:i-1]+str(sum)+exp[i+2:]
            break
        elif(exp[i] == '/'):
            if(int(exp[i-1]) % int(exp[i+1]) == 0):
                sum = int(int(exp[i-1]) / int(exp[i+1]))
                exp = exp[:i-1]+str(sum)+exp[i+2:]
                break
    return exp

def caculate_add(exp):
    for i in range(len(exp)):
        if(exp[i] == '+'):
            a = int(exp[i-1]) 
            b = int(exp[i+1])
            ashift = 0
            bshift = 0
            if((exp[i-2])<'9' and (exp[i-2])>'0'):
                a = int(exp[i-2])*10+int(exp[i-1]) 
                ashift = 1
            if((exp[i+2])<'9' and (exp[i+2])>'0'):
                b = int(exp[i+1])*10+int(exp[i+2]) 
                bshift = 1
            sum = a + b
            exp = exp[:i-1-ashift]+str(sum)+exp[i+2+bshift:]
            break
        elif(exp[i] == '-'):
            a = int(exp[i-1]) 
            b = int(exp[i+1])
            ashift = 0
            bshift = 0
            if(i>=2 and (exp[i-2])<'9' and (exp[i-2])>'0'):
                a = int(exp[i-2])*10+int(exp[i-1]) 
                ashift = 1
            if((i+2)<len(exp) and (exp[i+2])<'9' and (exp[i+2])>'0'):
                b = int(exp[i+1])*10+int(exp[i+2]) 
                bshift = 1
            sum = a - b
            exp = exp[:i-1-ashift]+str(sum)+exp[i+2+bshift:]
            break
    return exp

def caculate_inbrackets(exp):
    exp = caculate_mul(exp)
    exp = caculate_mul(exp)
    exp = caculate_mul(exp)
    exp = caculate_add(exp)
    exp = caculate_add(exp)
    exp = caculate_add(exp)
    return str(exp) 
    
def caculate(exp):
    for i in range(len(exp)):
        if(exp[i] == ')'):
            for j in range(i):
                if(exp[i-j-1] == '('):
                   return caculate(exp[:i-j-1]+caculate_inbrackets(exp[i-j:i])+exp[i+1:])
    return caculate_inbrackets(exp)

def caculate24point(exp, index):
    if(len(exp)%2 == 0):
        return -1
    for i in range(len(exp)):
        if((exp[i]!='+')and(exp[i]!='-')and(exp[i]!='/')and(exp[i]!='*')
           and(exp[i]!='(')and(exp[i]!=')')and(exp[i]>'9')and(exp[i]<'0')):
            return -1
    scard = [-1,-1,-1,-1]
    for j in range(4):
        scard[j] = cards[index][j]
    for i in range(len(exp)):
        if((exp[i] <= '9') and (exp[i] >= '1')):
            for j in range(4):
               if(int(exp[i]) == scard[j]):
                   scard[j]=-1
    for j in range(4):
        if(scard[j] != -1):
            return -1
    ret = caculate(exp)
    for i in range(len(ret)):
        if((exp[i] > '9') and (exp[i] < '0')):
            return -1
    return int(ret)    

print("请和我一起来玩24点游戏!")
sleep(1)
print("*************************************")
sleep(1)
print("24点游戏的规则是：屏幕上随机出现4张扑克牌，")
sleep(1)
print("用四则运算 +,-,×,/ 计算出24,并且每个数字只能用一次!") 
sleep(1)
print("例如：屏幕上出现了1，3，2，4")
sleep(1)
for i in range(2):
    puke_single(-300+300*i, 300, str(2*i+1),2*i)
    puke_single(-300+300*i, 0, str(2*i+2),2*i+1)
   
print("例如输入：1*2*3*4")
sleep(1)
print("正确！")
sleep(1)
print("*************************************")
sleep(1)
print("游戏正式开始！Let's Go!")
print("请输入回车继续游戏")
input()
sleep(0.5)

reset()

for index in range(0, 9):
    reset()
    card = cards[index]
    for i in range(2):
        puke_single(-300+300*i, 300, str(card[i*2]),randint(0,3))
        puke_single(-300+300*i, 0, str(card[i*2+1]),randint(0,3))
    
    print("请输入你的计算过程：")
    express = input()

    if(caculate24point(express, index) != 24):
        j = 0
        for j in range(1,3):
            print("错误， 重新输入你的计算过程:")
            express = input()
            if(caculate24point(express, index) == 24):
                break
        if(j == 2):
            print("3次错误， 游戏结束")
            break
                
    print(express+"=24")
    print("正确， 按n再来一题, 其他键退出游戏")
    if(input() == 'n'):
        continue
    else:
        print("再见~游戏结束！")
        break