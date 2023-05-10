# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
df=pd.read_csv('data5.csv.csv')
print(df)

sum = df.sum(axis=1)
avg = df.mean(axis=1)
print(sum,avg)
df2=pd.DataFrame(df,columns=["姓名",'班級',"國","英","數","總分","平均"]) # columns 增加欄位
igroup=['1','2','1','1'] #將班級做為群組
df2['班級']=igroup
df2["總分"]=sum
df2["平均"]=avg
print(df2)

df3=df2.groupby('班級').agg('mean').rank(ascending=False) 
print(df3) # groupby 群組 agg 依據 rank 排名 ascending 排序

df4=df2.sort_index(axis=0,ascending=False) #依據 index 排序
print(df4)

df5=df2.sort_values(by='英',ascending=False) #依據 英文分數 排序
print(df5)