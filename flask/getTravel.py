# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 01:10:18 2022

@author: User
"""
# 開啟Anaconda Prompt
# 輸入 cd\
#     cd meetjob 
#     cd flaskdemo
#     python getTravel.py
import requests # 上傳用

from bs4 import BeautifulSoup # 爬蟲專用

import db

from pymysql.converters import escape_string
# escape_string 特殊字符進行轉義

url="https://www.chinatimes.com/search/%E5%9C%8B%E9%9A%9B%E8%A7%80%E5%85%89?chdtv"


data = requests.get(url)  # 抓取URL的資料下來至電腦中，它的型態為：串流  stream byte

data.encoding = "utf-8" # 將資料編碼設定為： utf-8

data = data.text
# 抓取網路上的資料後轉換為文字

soup = BeautifulSoup(data,"html.parser")
#BeautifulSoup解析HTML 語法的

Travelnews = soup.find("ul","vertical-list list-style-none")



cursor = db.conn.cursor()

for row in Travelnews.find_all("div",'articlebox-compact'):
    try:
        title = row.find('h3','title').text.strip()
        print(title)
        link =row.a['href'].strip()
        print(link)
        photo = row.img['src'].strip()
        print(photo)
        postdate = row.find('span','date').text.strip()
        print(postdate)
        print('-'*30)
    except:
        continue


#開啟命令提示字元
#mysql -u root -p   輸入密碼 123456789
#use meetjob
#create table tnews(
# ->id int primary key auto_increment,
# ->title varchar(100),
# ->link varchar(255),
# ->photo varchar(255),
# ->modate datetime);
    
    title = escape_string(title) # 特殊字符進行轉義

      #先查詢標題是否有重覆的
    sql = "select * from tnews where title='{}'".format(title)
      
    cursor.execute(sql)
    db.conn.commit()

    if cursor.rowcount == 0 : #查詢的筆數為多少
        sql = "insert into tnews (title,link,photo,modate) values('{}','{}','{}','{}')".format(title,link,photo,postdate) 
      
        cursor.execute(sql)
        db.conn.commit()
      
db.conn.close()