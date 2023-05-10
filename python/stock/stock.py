# -*- coding: utf-8 -*-
"""
可以繪出台灣所有股票的某年某月的股價圖
"""
import twstock
import csv
import pandas 
import pandas_bokeh 
import os

def _hit():
    
    nO=enteR.get()
    stocK=twstock.Stock(nO)
    yeaR=enteR2.get()
    montH=enteR3.get()
    datA=stocK.fetch(int(yeaR),int(montH))
    fileName=nO+"="+yeaR+"-"+montH+".csv"
    csvFile=open(fileName,"w",newline="",encoding="utf-8-sig")
    writeR=csv.writer(csvFile)
    colName = ["日期","開盤價","最高價","最低價","收盤價"]
    writeR.writerow(colName)

    for vI in range(len(datA)):
        datE=str(datA[vI][0])
        datE=datE.split(" ")[0]
        opeN=str(datA[vI][3])
        higH=str(datA[vI][4])
        loW=str(datA[vI][5])
        closE=str(datA[vI][6])        
        writeR.writerow([datE,opeN,higH,loW,closE])

    csvFile.close()
    pandas_bokeh.output_file("stockprice.html")

    dF=pandas.read_csv(fileName)
    titlE=nO+"--"+yeaR+"年"+montH+"月"+"的股價圖"
    
    if var.get()=="1":
        pp="line"
    elif var.get()=="2":
        pp="point"
    elif var.get()=="3":
        pp="step"
    
    
    dF.plot_bokeh(kind=pp,x="日期",y=["開盤價", "最高價","最低價",'收盤價'],line_width=5,title=titlE,line_alpha=0.3,figsize=(1500,400),ylabel="價格") 
    enteR.delete(0,tk.END)
    enteR2.delete(0,tk.END)
    enteR3.delete(0,tk.END)
    

   
import tkinter as tk

wiN = tk.Tk()

wiN.title("Welcome 股價圖!!!")

wiN.geometry("500x450+500+200")
wiN.configure(bg="red")

lbL = tk.Label(wiN,text="股票代號: ",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
lbL.pack()

enteR=tk.Entry(wiN,font=("Arial",16),bd=5)
enteR.pack()

lbL2 = tk.Label(wiN,text="哪一年: ",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
lbL2.pack()

enteR2=tk.Entry(wiN,font=("Arial",16),bd=5)
enteR2.pack()

lbL3 = tk.Label(wiN,text="哪一月: ",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
lbL3.pack()

enteR3=tk.Entry(wiN,font=("Arial",16),bd=5)
enteR3.pack()

var = tk.StringVar()
myradiobutton1 = tk.Radiobutton(wiN, text='Line', font=("Arial", 16),variable=var, value=1,bg="yellow")
myradiobutton1.pack()

myradiobutton2 = tk.Radiobutton(wiN, text='Point', font=("Arial", 16),variable=var, value=2,bg="lime")
myradiobutton2.pack()

myradiobutton3 = tk.Radiobutton(wiN, text='Step', font=("Arial", 16),variable=var, value=3,bg="orange")
myradiobutton3.pack()
myradiobutton1.select()

btN = tk.Button(wiN, text="送出!!", font=("Arial", 16), width=10, height=2,fg="white",bg="blue", command=_hit)
btN.pack(side=tk.BOTTOM) 

wiN.mainloop()