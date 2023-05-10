# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 08:26:51 2022

@author: User
"""
# 開啟Anaconda Prompt
# 輸入 cd\
#     cd meetjob 
#     cd flask
#     python travel.py
import requests
from bs4 import BeautifulSoup

import db

from pymysql.converters import escape_string

from datetime import datetime as dt #抓日期函式庫

today = dt.today() #抓今天的日期格式

todays = today.strftime('%Y-%m-%d') #將設定好的日期格式轉換為字串使用
myHead={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

url = "https://feebee.com.tw/all/"

payload = {'q':'大阪旅遊'}

data = requests.get(url,params=payload,headers=myHead).text

soup = BeautifulSoup(data,'html.parser')

soupS=soup.find("ol")

cursor = db.conn.cursor()

for mySoup in soupS.find_all("li"):
    try:
        link=mySoup.find("a")["href"]
        print(link)
        title=mySoup.find("h3").text   
        print(title)
        price=mySoup.find("span","price ellipsis xlarge").text
        price=price.replace(',','')
        print(price)
        p=mySoup.find_all("img")[0]
        photo=p.get("data-src")
        print(photo)
        print("-"*30) 
    except:
        continue
    # 開啟命令提示字元
    # mysql -u root -p   輸入密碼 123456789
    # use meetjob
    # create table ttproduct(
    # ->id int primary key auto_increment,
    # ->itemtype int,
    # ->name varchar(100),
    # ->price int,
    # ->link varchar(150),
    # ->photo_url varchar(200),
    # ->information text);

    # create table ttproducttype(
    # ->id int primary key auto_increment,
    # ->itemname varchar(30));

    # create table message(
    # ->id int primary key auto_increment,
    # ->title varchar(100)),
    # ->username varchar(30),
    # ->email varchar(100),
    # ->content tex);

    # create table work(     # 放作品用
    # ->id int primary key auto_increment,
    # ->workname varchar(50)),
    # ->information text,
    # ->create_date date,
    # ->photo_file varchar(100));

    # insert into ttproducttype(itemname) values('旅遊書籍 '),('旅遊衣服'),('旅遊鞋子'),('旅遊帽子'),('旅遊背包');


    #      書籍的 類別是1
    #      要新增時，請先確認 itemtype=1 的類別，values('1')才開始建立資料
    title = escape_string(title)
    
    sql = "select * from travel where name='{}' and itemtype=3 ".format(title)
    
    cursor.execute(sql)
    db.conn.commit()
    
    if cursor.rowcount ==0 : #表示沒有該產品
        sql = "insert into travel(itemtype,name,price,link,photo_url) values('3','{}','{}','{}','{}')".format(title,price,link,photo)
        cursor.execute(sql)
        db.conn.commit()
        
        
db.conn.close()



    
        
