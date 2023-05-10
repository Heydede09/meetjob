# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 21:29:20 2022

@author: User
"""

import db

from flask import Flask,request
from flask_restful import Resource,Api,reqparse

app = Flask(__name__)

api= Api(app)

class Students(Resource):
    def get(self):
        
        sql= "select *from students"
        cursor = db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        result = cursor.fetchall()
        data = list()

        for item in result:
            json = {}
            json ['name']= item[0]
            json ["sex"] = item[1]
            json ["stuNo"]= item[2]
            
            data.append(json)

        return {"students":data},200
    
api.add_resource(Students,"/studentsList")

if __name__ == "__main__":
    app.run(debug=True)