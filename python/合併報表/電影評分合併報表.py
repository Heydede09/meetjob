# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 00:37:17 2023

@author: User
"""

import  pandas  as  pd
pd.options.display.max_rows = 10 #秀出10筆資料
users_index = ['user_id', 'gender', 'age',  'occupation', 'zip']

users = pd.read_table('users.dat',sep='::', header=None,  names=users_index) # sep 分隔符號
print(users[:5])

ratings_index =['user_id',  'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat',  sep='::', header=None,  names=ratings_index)
print(ratings[:5])

movies_index =['movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat',  sep='::', header=None,  names=movies_index)
print(movies[:5])

data=pd.merge(pd.merge(ratings, users), movies) # 合併三個資料表
print(data[:5])
print(data.iloc[0]) #知道欄位名稱

#依據性別針對每部電影的平均得分
from pandas.core.reshape.pivot import pivot_table

mean_ratings  = data.pivot_table('rating',index='title',  columns='gender', aggfunc='mean') # aggfunc 依據
print(mean_ratings[:5])

#依據性別針對每部電影的總分
mean_ratings_sum = data.pivot_table('rating',index='title',  columns='gender', aggfunc='sum')
print(mean_ratings_sum[:5])

#電影評分數據200秀出資料
ratings_groupby=data.groupby('title').size()
print(ratings_groupby[:10])

title200=ratings_groupby.index[ratings_groupby >=200]
print(title200[:10])

abcmean_ratings= mean_ratings.loc[title200]
print(abcmean_ratings[:10])

#女性最喜歡的電影
top10 = mean_ratings.sort_values(by="F",ascending=False) #ascending=False 降冪排列
print(top10[:10])

#男性，女性差異最大的十部電影
mean_ratings['diff']=mean_ratings["M"]-mean_ratings['F']
difftop10=mean_ratings.sort_values(by='diff',ascending=False)
print(difftop10[:10])

