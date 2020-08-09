# Importing Required Packages
import time
import tkinter as tk
from tkinter import*
import winsound
import math
import datetime
#Countdown function 
def countdown(count):
    # counting time 
    seconds=math.floor(count%60)
    minutes=math.floor((count/60)%60)
    #Conditional statement for counting time in seconds
    if count>=0:
        root.after(1000,countdown,count-1)
    else:
        for x in range(3):
             winsound.Beep(1000,1000)
def updateButton():
        # Taking entries 
        minute=set_minute.get()
        second=set_second.get()
        #Calling countdown function
        if(minute.isdigit and second.isdigit):
            time=int(minute)*60+int(second)
            countdown(time)
#Reset Function
def Reset():
    set_minute.delete('0',END)
    set_second.delete('0',END)
root=Tk()
root.geometry("370x200+50+50")
root.title("STOP_WATCH")
#Creating Entries

Label1=Label(root, text='Minutes',font=('Algerian',16),foreground="black")
Label1.grid(row=0,column=0,sticky=W,padx=5,pady=5)

set_minute=Entry(root,font=('Algerian',16),foreground='black')
set_minute.grid(row=0,column=1,padx=5,pady=5)

Label2=Label(root, text='Seconds',font=('Algerian',16),foreground="black")
Label2.grid(row=1,column=0,sticky=W,padx=5,pady=5)

set_second=Entry(root,font=('Algerian',16),foreground='black')
set_second.grid(row=1,column=1,padx=5,pady=5)



#Submit Button

start=Button(root,text="Start",command=updateButton,font=('Algerian',16))
start.grid(row=2,columnspan=2,pady=10)

Reset_button=Button(root,text="Reset",command=Reset,font=('Algerian',16))
Reset_button.grid(row=4,columnspan=2,pady=10)

root.mainloop()
