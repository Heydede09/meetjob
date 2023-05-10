# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymysql

dbsetting ={
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "password":"123456789",
    "db":"meetjob",
    "charset":"utf8"
    }

conn = pymysql.connect(**dbsetting)
