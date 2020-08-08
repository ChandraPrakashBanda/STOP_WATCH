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
    hours=math.floor((count/3600))
    label=Label(root,text="Hours: "+str(hours)+"Minutes: "+str(minutes)+"Seconds: "+str(seconds))
    label.pack()

    if count>=0:
        root.after(1000,countdown,count-1)
    else:
        for x in range(3):
            winsound.Beep(1000,1000)
        label1=Label(root,text="Time is up")
        label1.pack()
def updateButton():
        # taking entries 
        hour=set_hour.get()
        minute=set_minute.get()
        second=set_second.get()
        #Calling countdown function
        if(hour.isdigit()and minute.isdigit and second.isdigit):
            time=int(hour)*3600+int(minute)*60+int(second)
            countdown(time)

root=Tk()
root.geometry("400x400+50+50")
root.title("STOP_WATCH")
#creating entries
set_hour=Entry(root)
set_hour.pack()
set_minute=Entry(root)
set_minute.pack()
set_second=Entry(root)
set_second.pack()
#submit Button
submit=Button(root,text="Update",command=updateButton)
submit.pack()
root.mainloop()