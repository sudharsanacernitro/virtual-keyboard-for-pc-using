import subprocess
import sys
import os
import pymysql
import pyautogui
import time
shift=0
cap=0
#argv=sys.argv[1:]
#print(argv[0])
#os.system(argv)
def write(p):
    
    if(p=="shift"):
        shift=1
        return
    if(len(p)<=2):
        p=p[0]
        pyautogui.typewrite(p)
    elif(p=="delete"):
        pyautogui.press('backspace')
    elif(p=="enter"):
        pyautogui.press('enter')
    elif(p=="space"):
        pyautogui.press('space')
    elif(p=="caplock"):
        if(cap==0):
            cap=1
            pyautogui.press('capslock')
        else:
            cap=0
            pyautogui.press('capslock')
    
    
connection = pymysql.connect(host="localhost",user="root", passwd="", database="wifi")
cursor = connection.cursor()
cursor.execute("TRUNCATE TABLE wifi")
num=1
while True:
 
    retrive = "Select cmd from wifi"

#executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    for i in rows:
        write(i[0])
        cursor.execute("TRUNCATE TABLE wifi")
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if rows :
        pass
    else:  
        cursor.execute("TRUNCATE TABLE wifi")
    
       
connection.close()

