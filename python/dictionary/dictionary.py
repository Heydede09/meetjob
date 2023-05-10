'''
廖美鳳的自製英文字典!!!
'''
def _hit32():
    if enteR31.get() in word:
        del word[enteR31.get()]
        lbL33["text"]="["+enteR31.get()+"]"+"已刪除!!"
        enteR31.delete(0,tk.END)
    else:
        lbL33["text"]="沒有這個字噢!!"
        enteR31.delete(0,tk.END)

def _hit31():
    if enteR31.get() in word:
        lbL33["text"]=word[enteR31.get()]
    else:
        lbL33["text"]="沒有這個字噢!!"
        enteR31.delete(0,tk.END)



def _hit11():
    word[enteR11.get()]=enteR12.get()
    enteR11.delete(0,tk.END)
    enteR12.delete(0,tk.END)
    enteR11.focus()
    
def _hit1(): #新增子視窗
    global enteR11,enteR12
    wiN1=tk.Toplevel(wiN)
    wiN1.title("新增/修改單字")
    wiN1.geometry("400x500+600+400")
    
    lbL11 = tk.Label(wiN1,text="請輸入英文: ",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
    lbL11.pack()
    enteR11=tk.Entry(wiN1,font=("Arial",16),bd=5)
    enteR11.pack()
    
    lbL12 = tk.Label(wiN1,text="請輸入中文: ",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
    lbL12.pack()
    enteR12=tk.Entry(wiN1,font=("Arial",16),bd=5)
    enteR12.pack()
    
    btN11 = tk.Button(wiN1, text="確定!", font=("Arial", 12),fg="white",bg='blue' ,width=10, height=3, command=_hit11)
    btN11.pack() 
    
    btN12 = tk.Button(wiN1, text="離開!", font=("Arial", 12),fg="white",bg='blue' ,width=10, height=3, command=wiN1.destroy)
    btN12.pack() 
    
def _hit2():
    wiN2=tk.Toplevel(wiN)
    wiN2.title("顯示所有單字")
    wiN2.geometry("250x500+400+100")
    
    btN2 = tk.Button(wiN2, text="結束!!",bg="red", font=("Arial", 12), width=10, height=2, command=wiN2.destroy)
    btN2.pack() 
    sBar=tk.Scrollbar(wiN2)
    sBar.pack(side=tk.RIGHT,fill=tk.Y)
    listBox=tk.Listbox(wiN2, font=("Arial", 20),yscrollcommand=sBar.set,bg="yellow",width=850)
    listBox.pack(side=tk.RIGHT, fill=tk.BOTH)
    sBar.config(command=listBox.yview)
    for iteM in word.items():
        listBox.insert(tk.END, iteM)
    
def _hit3():
    global lbL33,enteR31
    wiN3=tk.Toplevel(wiN)
    wiN3.title("查詢/刪除單字")
    wiN3.geometry("400x500+600+400")
    
    lbL31 = tk.Label(wiN3,text="請輸入英文",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
    lbL31.pack()
    enteR31=tk.Entry(wiN3,font=("Arial",16),bd=5)
    enteR31.pack()
    lbL32 = tk.Label(wiN3,text="中文是",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
    lbL32.pack()
    lbL33 = tk.Label(wiN3,text="",fg="white",bg="orange", font=("Arial", 16), width=25, height=2)
    lbL33.pack()
    btN31 = tk.Button(wiN3, text="查詢!!",bg="blue" ,fg="white",font=("Arial", 14), width=10, height=2, command=lambda:_hit31())
    btN31.pack() 
    btN32 = tk.Button(wiN3, text="刪除!!",bg="red", font=("Arial", 14), width=10, height=2, command=lambda:_hit32())
    btN32.pack() 
    btN33 = tk.Button(wiN3, text="結束!!",bg="black",fg="white", font=("Arial", 14), width=10, height=2, command=wiN3.destroy)
    btN33.pack() 
    
def _hit4():
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎???")
    if qQ:
        File=open("wordbook.json","w",encoding="utf-8")
        json.dump(word,File,ensure_ascii=False,indent=4) #ident 內縮
        File.close()
        wiN.destroy()  
        
        

import json,os

if os.path.isfile("wordbook.json"):
    file=open("wordbook.json","r",encoding="utf-8")
    word=json.load(file)
    file.close()
else:
    word={}
#1.載入tkinter
import tkinter as tk
import tkinter.messagebox

#2.使用tkinter建立一個叫做[wiN]的視窗
wiN = tk.Tk()

#3.設定視窗[標題]
wiN.title("廖美鳳的自製英文字典!!!")

#4.設定視窗[大小]
wiN.geometry("600x500+600+400")

#5.建立一個叫做[btN]的[button]物件,並做相關屬性設定
btN1= tk.Button(wiN, text="新增/修改單字",fg="white",bg="green", font=("Arial", 18), width=20, height=3, command=_hit1)
btN2= tk.Button(wiN, text="顯示所有單字",bg="green",fg="white", font=("Arial", 18), width=20, height=3, command=_hit2)
btN3= tk.Button(wiN, text="查詢/刪除單字", bg="green",fg="white",font=("Arial", 18), width=20, height=3, command=_hit3)
btN4= tk.Button(wiN, text="離開字典", bg="green",fg="white",font=("Arial", 18), width=20, height=3, command=_hit4)


#6.放置按鈕(設定顯示位置)
btN1.pack()
btN2.pack() 
btN3.pack()
btN4.pack() 
#7.顯示視窗
wiN.mainloop()

