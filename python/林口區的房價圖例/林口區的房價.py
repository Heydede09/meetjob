# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 23:52:47 2023

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import fontManager #中文
fontManager.addfont("TaipeiSansTCBeta-Light.ttf") #中文字型 
mpl.rc('font',family='Taipei Sans TC Beta Light Regular')
fd=pd.read_csv("house.csv.csv",encoding="utf-8")
print(fd)
fd1=fd[fd.district=="林口區"].iloc[:,2]
fd2=fd[fd.district=="林口區"].iloc[:,15]
plt.bar(fd1,fd2)
plt.title("林口區")
plt.xticks(rotation=45) # X座標標籤轉角度
plt.xlabel("房價",fontsize=17)
plt.ylabel("地址",fontsize=17)
plt.show()