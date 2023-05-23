# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 06:34:03 2023

@author: User
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

usr=input("請輸入帳號(email或手機):") 
pwd=input("請輸入密碼：")
driver.get("https://www.facebook.com/")
print('opend facebook')
sleep(2)

username_box=driver.find_element('id','email')
username_box.send_keys(usr)
print("email id entered")
sleep(2)

password_box=driver.find_element('id','pass')
password_box.send_keys(pwd)
print("pass id entered")
sleep(2)

login_box=driver.find_element(By.CSS_SELECTOR,"button[name='login']")
login_box.click()
print("ok")
