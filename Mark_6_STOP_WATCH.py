#  Importing Required Packages
import time
import tkinter as tk
from tkinter import*
import winsound
import math
import datetime

#  countdown function 
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
        # taking entries 
        minute=set_minute.get()
        second=set_second.get()
        #Calling countdown function
        if(minute.isdigit and second.isdigit):
            time=int(minute)*60+int(second)
            countdown(time)

#  Reset function
def Reset():
    set_minute.delete('0',END)
    set_second.delete('0',END)
root=Tk()
root.geometry("400x400+50+50")
root.title("STOP_WATCH")
#creating entries
set_minute=Entry(root)
set_minute.pack()
set_second=Entry(root)
set_second.pack()
#submit Button
start=Button(root,text="Start",command=updateButton)
start.pack()
Reset_button=Button(root,text="Reset",command=Reset)
Reset_button.pack()



root.mainloop()