# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 21:35:23 2023

@author: User
"""

# HTML解說
# <a> 為超連結
# class="gb_d" 樣式
# target="_top" 開啟的網頁在哪個視窗
# 物件(按鈕、超連結...)
#copy Xpath 抓到位置

from selenium import webdriver


driver=webdriver.Chrome()
driver.get("https://www.google.com.tw/")
driver.implicitly_wait(3) #等待時間

driver.find_element("xpath",'//*[@id="gb"]/div/div[1]/div/div[1]/a').click()
