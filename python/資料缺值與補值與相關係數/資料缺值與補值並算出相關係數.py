# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:51:19 2023

@author: User
"""

import numpy as np
import pandas as pd
df=pd.read_csv("AQIa.csv.csv")

df1=df.drop("Pollutant",axis=1) #針對專欄刪除
df2=df.dropna(axis=1,how="all")
#how="all" 該欄位全部缺值做刪除
df2.to_csv("aaAQIa.csv.csv")

from pandas.core import missing
from sklearn import impute
from sklearn.impute import SimpleImputer  

df3=df[['AQI','CO','CO_8hr']]
df3=df3.replace(['-'],np.nan)#將 - 轉換成空值
print(df3.head(10))

imputer = SimpleImputer(missing_values=np.nan, strategy="mean") #用平均值做補值
print(imputer)

imputer=imputer.fit(df3)
df3=imputer.transform(df3)

#df4=pd.DataFrame(df3)
df4=pd.DataFrame(np.around(df3,decimals=1)) #四捨五入，小數點1位
print(df4.head(10))
print(df4.corr()) #皮爾森相關係數
print(df4.corr('kendall'))# kendall相關係數

