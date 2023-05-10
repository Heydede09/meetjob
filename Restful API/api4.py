# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 00:04:55 2022

@author: User
"""

from flask import Flask,request
from flask_restful import Resource,Api,reqparse

app = Flask(__name__)

api = Api(app)

customer = [{
    'name':'Bill',
    'email':'bill@gmail.com'    
    }]


class Member(Resource):
    
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email',required=True,help='Email is required',location="form")
        self.parser.add_argument('password',required=True,help='Password is required',location="form")
    
    # 若只指定一個格式進來時==> location='json'  或  location='form'
    
    def get(self,name): # 用來抓取資料
        find = [item for item in customer if item['name'] == name]
        if len(find) == 0:
            return {'message':'username not exist'},403
        
        user = find[0]
        if not user:
            return {'message':'username not exist'},403
        
        return {'message':'success','user':user},200
    
    
    def post(self,name): # 用來新增資料
        arg = self.parser.parse_args()  # 解析帶入的參數
        user = {
            'name':name,
            'email':arg['email'],
            'password':arg['password']
            }
        
        global customer
        
        customer.append(user)
        return {'message':'Add User Success','user':user},200
    
    def put(self,name): # 資料修改
        arg = self.parser.parse_args()
        find = [item for item in customer if item['name'] == name]
        if len(find) == 0:
            return {'message':'username not exist'},403
    
        user = find[0]
        user['email'] = arg['email']
        user['password'] = arg['password']
        
        return {'message':'update user Success','user':user},200
    
    def delete(self,name): # 資料刪除
        global customer
        customer = [item for item in customer if item['name'] != name]
        return {'message':'Delete Success'},200


class MemberList(Resource):
    # 取得所有的客戶資料
    def get(self):
        return {'customer':customer},200


    
api.add_resource(Member,'/member/<string:name>')   
api.add_resource(MemberList , '/memberlist')

if __name__ == "__main__":
    app.run(port=5566,debug=True)