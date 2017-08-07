import tkinter as tk
from tkinter import Label, StringVar, ttk
from ClockThread import Clock as ck, CountDownClock as cdc
import GlobalVariables as gv
import GlobalFunctions as gf
import UIWidgets as ui

class LoginPage(ttk.Frame):
    
    def __init__(self, parent, nav):
        tk.Frame.__init__(self, parent, bg=gv.bckGround)
        gv.topLevel      = id(self)
        self.parentID    = id(self)  
        self.nav = nav
        self.parent = parent  
        #strup.changeTitle('Main Panel')
#         titleLabel = Label(self,text="DisArm",font=gv.LARGE_FONT,
#                         bg=gv.bckGround,fg=gv.forGround)
#         titleLabel.place(x=350, y=10)
   
        self.constructNumberPad()
        self.constructKeyPadErrorField()
        self.Clock = ck(self)
        
    def constructNumberPad(self):
        
        self.ux = self.nav.launch.ux
        ctr = self.ux.get_horizontal_center(75)
        l,m,r = (ctr-80, ctr, ctr+80)
        
        self.sh = 350
        sh = self.sh
        h1,h2,h3,h4 = (sh,sh+90,sh+180,sh+270)
        
        self.keyPadtxt  = StringVar()
        self.keyPadHide = StringVar()
        
        self.keyEntry = ui.make_keyPadEntry(self, self.ux.get_horizontal_center(235), 
                                            self.sh-80, 235, 45, 
                                            textvariabl=self.keyPadHide, 
                                            font=gv.LARGE_FONT, bg='white',fg='black')

        
            
        self.B1 = ui.keyBtn(self,str(1),1,l,h1)
        self.B2 = ui.keyBtn(self,str(2),2,m,h1)
        self.B3 = ui.keyBtn(self,str(3),3,r,h1)
        
        self.B4 = ui.keyBtn(self,str(4),4,l,h2)
        self.B5 = ui.keyBtn(self,str(5),5,m,h2)
        self.B6 = ui.keyBtn(self,str(6),6,r,h2)
        
        self.B7 = ui.keyBtn(self,str(7),7,l,h3)
        self.B8 = ui.keyBtn(self,str(8),8,m,h3)
        self.B9 = ui.keyBtn(self,str(9),9,r,h3)
        
        self.BC = ui.keyBtn(self,u"\21","\21",l,h4)
        self.B0 = ui.keyBtn(self,str(0),0,m,h4)
        self.BE = ui.keyBtn(self,u"\u2386","\u2386",r,h4)
        
        self.createArmDIsArmBtn()
        
    def constructKeyPadErrorField(self):
        
        self.keyPadErrorField = StringVar()
        self.keyPadError = ui.make_keyPadEntry(self, self.ux.get_horizontal_center(235), 
                                               320, 235, 20, 
                                            textvariabl=self.keyPadErrorField, 
                                            font=gv.LARGE_FONT, bg=gv.bckGround,fg='red')
        
        
        
    def createArmDIsArmBtn(self):
        
        self.AlarmBtnLbl = StringVar()
        self.setAlarmVar()
        self.LoadBtn()
        
    def LoadBtn(self):
        
        self.B1       = self.make_ArmDisArm(self.ux.get_horizontal_center(235), 715, 235, 45, 
                                self.handleAlarmStateChange, text=self.AlarmBtnLbl.get(), 
                                fg=self.bg, bg=gv.bckGround, 
                                font=gv.LARGE_FONT)
    
    def createDestroyAlarmBtn(self):
        try:
            self.B1.destroy()
            self.LoadBtn()
        except:
            self.LoadBtn()
    
    def handleAlarmStateChange(self, event):
        
        isValid = gf.isPasswordValid(self.keyPadtxt.get())
         
        if isValid:
            if gv.AlarmArmed:
                gv.AlarmArmed = False
                self.nav.show_launch_pad()
            else:
                self.keyPadHide.set('')
                self.keyPadtxt.set('')
                gv.AlarmArmed = True
                self.setAlarmVar()
                self.createDestroyAlarmBtn()
        else:
            self.keyPadErrorField.set('Password is invalid.')
            self.keyPadtxt.set('')
                
    
    def setAlarmVar(self):
        value = self.getVarsForAlarmState()
        self.AlarmBtnLbl.set(value)
    
       
    def getVarsForAlarmState(self):
        
        if gv.AlarmArmed:
            value = 'Disarm'
            self.fg = 'Black'
            self.bg = '#FF0000'
        else:
            value = 'Arm'
            self.fg = 'Black'
            self.bg = '#00FF00'
        
        return value
        
        
        
    def make_ArmDisArm(self, x, y, w, h, action, *args, **kwargs):

        f = tk.Frame(self, height=h, width=w, highlightbackground=self.bg, highlightcolor=self.bg, highlightthickness=1,)
        f.pack_propagate(0) # don't shrink
        f.place(x=x, y=y)
        button = Label(f, *args, **kwargs)
        button.bind('<ButtonPress-1>', action)
        button.bind('<Any-Enter>', self.buttonClrEnter)
        button.bind('<Any-Leave>', self.buttonClrLeave)
        button.pack(fill=tk.BOTH, expand=1)
        return button   
    
    def buttonClrEnter(self, event):
        event.widget.config(bg=self.bg, fg='black')
    
    def buttonClrLeave(self, event):
        event.widget.config(bg=gv.bckGround, fg=self.bg)    
        
    def callCDC(self):
        self.cdc = cdc(self,self.ux.get_horizontal_center(235),780)
        
    def destroyCDC(self):
        self.cdc.destroyClock()
        
        
         
