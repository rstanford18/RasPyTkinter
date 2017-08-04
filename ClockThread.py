
from tkinter import Frame, Label, BOTH
import time
import GlobalVariables as gv
import SMS

class Clock():
    
    def __init__(self, parent):
        self.parent = parent
        self.ClockFg = "#6E6E6E"
        self.handleClock()
        self.updateClock()
        
    def handleClock(self):
            
        self.Clock = self.buildClockUI(1600, 50, 200, 75, font=('times', 30, 'bold'), 
                                                    bg=gv.bckGround, fg=self.ClockFg)
               
    def buildClockUI(self, x, y, w, h, *args, **kwargs):
        f = Frame(self.parent, height=h, width=w, highlightbackground=self.ClockFg, 
                                highlightcolor=self.ClockFg, highlightthickness=2,)
        f.pack_propagate(0) # don't shrink
        f.place(x=x, y=y)
        lbl = Label(f, *args, **kwargs)
        lbl.pack(fill=BOTH, expand=1)
        return lbl 

    def updateClock(self, previousTime=''):
        currentTime = time.strftime('%H:%M:%S')
        if previousTime != currentTime:
            previousTime = currentTime
            self.Clock.config(text=currentTime)
        
        self.Clock.after(200, self.updateClock, previousTime)
        
class CountDownClock():
    
    def __init__(self, parent, x, y):
        self.parent = parent
        self.start = gv.CountDownToAlarm + 1
        self.ClockFg = "#FF0000"
        self.x = x
        self.y = y      
        self.handleClock()
        self.updateClock()

            
    def handleClock(self):
    
        self.Clock = self.buildClockUI(235, 75, font=('times', 30, 'bold'), 
                                                    bg=gv.bckGround, fg=self.ClockFg)
               
    def buildClockUI(self, w, h, *args, **kwargs):
        f = Frame(self.parent, height=h, width=w, highlightbackground=self.ClockFg, 
                                highlightcolor=self.ClockFg, highlightthickness=2,)
        f.pack_propagate(0)
        f.place(x=self.x, y=self.y)
        lbl = Label(f, *args, **kwargs)
        lbl.pack(fill=BOTH, expand=1)
        return lbl 

    def updateClock(self):
        self.start = int(self.start) - 1
        self.start = '0'+str(self.start) if len(str(self.start)) < 2 else str(self.start)     
        self.Clock.config(text=self.start)
        gv.CountDownToAlarm = int(self.start)
        if gv.AlarmArmed == False:
            return
        if int(self.start) < 1:
            SMS.sendSMS()
        else:    
            self.Clock.after(1000, self.updateClock)
        
        
    def destroyClock(self):
        self.Clock.destroy()
        
        
        
        
        