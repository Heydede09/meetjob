# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 22:56:40 2022

@author: User
"""
#將資料表 news的資料傳給網頁使用

from flask import Flask,render_template,request,url_for,redirect

#分頁時，要使用的
from flask_paginate import Pagination,get_page_parameter

import db

app= Flask(__name__)

@app.route("/news")
def news():
    sql="select * from tnews order by id desc"
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    allnews = cursor.fetchall()
    
    return render_template("news.html", **locals()) # **locals 將所有變數都丟進 news.html 

@app.route("/")
def index():

   
    return render_template("index.html",**locals())



@app.route("/product",methods=['GET'])
def product():
                            #網址的參數名稱
    items = request.args.get('item')
    keyword= request.args.get('p')
    page = request.args.get('page')
    
    sql = "select count(*) as allcount from travel" # 統計全部的筆數
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    res = cursor.fetchone() # 抓取一筆資料，一維串列
    count = int(res[0]) # 抓到全部的筆數
    
    
    if page == None:
        
        page=1
    
        #使用者都沒有依條件查詢，只單獨點選產品頁的連結
        if items == None and keyword == None:
            sql= "select * from travel order by id desc limit 10"
        elif len(items) > 0 and len(keyword) == 0:
            #使用者查類別但沒有查關鍵字
            sql = "select * from travel where itemtype='{}' limit 10" .format(items)
            
        elif items =="0" and len(keyword) > 0:
            #關鍵字查詢
            sql = " select * from travel where name like '%{}%' limit 10".format(keyword)
            
        else:
            #使用者查類別及關鍵字
            sql = "select *from travel where itemtype='{}' and name like '%{}%' limit 10".format(items,keyword)
            
        cursor = db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        res= cursor.fetchall() 
        # 抓取全部的資料，二維串列
        
        pagination = Pagination(page=page,total=count,per_page=10)
        
        return render_template("product.html",result=res,pagination=pagination)
    
    else:
        #表示使用者有按分頁(下一頁、上一頁)
        page = request.args.get(get_page_parameter(),type=int,default=int(page))
        startPage = page -1
        
        #使用者都沒有依條件查詢，只單獨點選產品頁的連結
        if items == None and keyword == None:
            sql= "select * from travel order by id desc limit {},{}".format(startPage*10,10)
        elif len(items) > 0 and len(keyword) == 0:
            #使用者查類別但沒有查關鍵字
            sql = "select * from travel where itemtype='{}' limit {},{}" .format(items,startPage*10,10)
            
        elif items =="0" and len(keyword,startPage*10,page*10) > 0:
            #關鍵字查詢
            sql = " select * from travel where name like '%{}%' limit {},{}".format(keyword,startPage*10,10)
            
        else:
            #使用者查類別及關鍵字
            sql = "select *from travel where itemtype='{}' and name like '%{}%' limit {},{}".format(items,keyword,startPage*10,10)
            
        cursor = db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        res= cursor.fetchall() 
        # 抓取全部的資料，二維串列
        
        pagination = Pagination(page=page,total=count,per_page=10)
        
        return render_template("product.html",result=res,pagination=pagination)
        


@app.route("/contact")
def message():
    return render_template("contact.html")

@app.route("/addMessage", methods=['POST'])
def addContact():
    if request.method == 'POST':
        username = request.form.get('username')
        title = request.form.get('title')
        email = request.form.get('email')
        content = request.form.get('content')
        
        sql= "insert into message(title,username,email,content) values('{}','{}','{}','{}')" .format(title,username,email,content)
        
        cursor= db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
    
    return redirect(url_for('message')) 
    # url_for 返回 message
    #return render_template('contact.html')
    
    
# @app.route('/hots/<page>')
# def hot(page):
#     if page == "MMA":
#         sql = "select * from ttproduct where itemtype='1'"
#     elif page == "JJU":    
#         sql = "select * from ttproduct where itemtype='2'"
#     else:
#         sql = "select * from ttproduct order by id desc"
#     cursor = db.conn.cursor()
#     cursor.execute(sql)
#     db.conn.commit()
#     res = cursor.fetchall()
#     return render_template("product.html",result=res)    



@app.route('/about')
def about():
    return render_template("about.html")








app.run(debug=True,host='0.0.0.0',port=5577)