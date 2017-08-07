import tkinter as tk
from tkinter import Label, StringVar, ttk
import GlobalVariables as gv
import GlobalFunctions as gf
import UIWidgets as ui
from MenuBar import MainMenuBar as mb
from ClockThread import Clock as ck

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import time
import datetime

from threading import Thread
# Figure.rcParams['axes.facecolor']='red'
# Figure.rcParams['savefig.facecolor']='red'



class ClimateMain(ttk.Frame):
    
    def __init__(self, parent, nav):
        tk.Frame.__init__(self, parent, bg=gv.bckGround)
        gv.topLevel      = id(self)
        self.parentID    = id(self)
        self.nav = nav
        self.parent = parent
        self.ux = self.nav.ux
        self.ux.han_change_title('Climate')
        self.mb     = mb(self)
        self.menu   = nav.parent.config(menu=self.mb.getMenu()) 
        self.Clock = ck(self)
        
        self.k = Thread(target=self.generateTestData)
        self.k.start()

        self.han_init_chart_ux()

        
    def han_init_chart_ux(self):
        ctr = self.ux.get_horizontal_center(1500)
        self.plotFrame = tk.Frame(self, height=500, width=1500, highlightbackground="white", highlightcolor='white', highlightthickness=1)
        self.plotFrame.pack_propagate(0) # don't shrink
        self.plotFrame.place(x=ctr, y=150)

        self.f = Figure(figsize=(3,3), dpi=100)
        self.f.set_facecolor('#333333')
        self.a = self.f.add_subplot(111)
        self.a.title.set_text('Climate')
        
        canvas = FigureCanvasTkAgg(self.f, self.plotFrame)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self.plotFrame)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.ani = animation.FuncAnimation(self.f, self.animate, interval=1000)
     
    
    def constructLaunchPad(self):
        
        
        w = 240
        ctr = self.ux.get_horizontal_center(w)
        l,m,r = (ctr-(w), ctr, ctr+(w))
        
        self.sh = 300
        sh = self.sh
        h1,h2 = (sh,sh+(w))
              
        self.B1 = ui.LaunchPadBtn(self,'Security',1,l,h1)
        self.B2 = ui.LaunchPadBtn(self,'Climate',2,m,h1)
        self.B3 = ui.LaunchPadBtn(self,'Cameras',3,r,h1)
        
        self.B4 = ui.LaunchPadBtn(self,'Lighting',4,l,h2)
        self.B5 = ui.LaunchPadBtn(self,'Listen',5,m,h2)
        self.B6 = ui.LaunchPadBtn(self,'Admin',6,r,h2)


    def generateTestData(self):
        pRange = (75,95)
        while True:
    
            st = datetime.datetime.now()
            YranINt = gf.randomCoord(pRange)     
            gv.testData += [[st,YranINt]]
            time.sleep(3)
    
    def animate(self, i):

        pullData = gv.testData
        
        dataList = pullData
        xList = []
        yList = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y = eachLine
                xList.append(x)
                yList.append(int(y))
                
        self.a.clear()
        self.a.plot(xList, yList)    
        self.a.set_yticks(ticks=[i for i in range(0,125) if i % 5 == 0])
        #
        self.a.set_xlabel('Date', color='white')
        self.a.set_ylabel('Temperature',color='white')
        self.a.patch.set_facecolor('#333333')
        self.a.tick_params(axis='x', colors='white')
        self.a.tick_params(axis='y', colors='white')
        self.a.grid(color='grey', linestyle='dotted', linewidth=1)

        for spine in self.a.spines.values():
            spine.set_edgecolor('white')



    