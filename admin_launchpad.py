import tkinter as tk
from tkinter import Label, StringVar, ttk
import GlobalVariables as gv
import UIWidgets as ui
from MenuBar import MainMenuBar as mb
from ClockThread import Clock as ck


class AdminLaunchPad(ttk.Frame):
    
    def __init__(self, parent, nav):
        tk.Frame.__init__(self, parent, bg=gv.bckGround)
        gv.topLevel      = id(self)
        self.parentID    = id(self) 
        self.nav   = nav
        self.parent = parent  
        self.ux     = self.nav.ux
        self.ux.han_change_title('Admin LaunchPad')
        self.mb     = mb(self)
        self.menu   = nav.parent.config(menu=self.mb.getMenu()) 
        self.constructLaunchPad()
        self.Clock  = ck(self)

        
    def constructLaunchPad(self):
        
        w = 240
        ctr = self.ux.get_horizontal_center(w)
        l,m,r = (ctr-(w), ctr, ctr+(w))
        
        self.sh = 300
        sh = self.sh
        h1,h2 = (sh,sh+(w))
              
        self.B1 = ui.AdminLaunchPadBtn(self,'Cameras',1,l,h1)
        self.B2 = ui.AdminLaunchPadBtn(self,'GPIO',2,m,h1)
        self.B3 = ui.AdminLaunchPadBtn(self,'Twilio',3,r,h1)
        
        self.B4 = ui.AdminLaunchPadBtn(self,'Theme',4,l,h2)
        self.B5 = ui.AdminLaunchPadBtn(self,'Rules',5,m,h2)
        self.B6 = ui.AdminLaunchPadBtn(self,'Users',6,r,h2)