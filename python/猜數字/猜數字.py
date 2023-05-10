# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 23:12:51 2023

@author: User
"""

#a=85
import  random #亂數
a=random.randint(1,100)
#for i in range(1,101,1):
i=0
while True:#無限迴圈
    i=i+1
    b=int(input("請輸入數字0-99:"))
    if b==a:
        print("你猜對了(第{}次)".format(i))
        break
    elif b<a:
        print("數字偏小(第{}次)".format(i))
    elif b>a:
        print("數字偏大(第{}次)".format(i))
        

        