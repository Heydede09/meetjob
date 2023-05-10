# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 22:34:11 2023

@author: User
"""
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.google.com.tw/")
driver.implicitly_wait(3)

driver.find_element("xpath",'//*[@id="gb"]/div/div[1]/div/div[2]/a').click()
inputE=driver.find_element("name","q")
inputE.send_keys("風景圖片")
inputE.submit()
driver.implicitly_wait(3) #等待時間