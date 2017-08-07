import tkinter as tk
from tkinter import Label, StringVar, ttk
import GlobalVariables as gv
import UIWidgets as ui
from MenuBar import MainMenuBar as mb
from ClockThread import Clock as ck


class LaunchMain(ttk.Frame):
    
    def __init__(self, parent, nav):
        tk.Frame.__init__(self, parent, bg=gv.bckGround)   
        self.nav   = nav
        self.parent = parent  
        self.ux     = self.nav.ux
        self.ux.han_change_title('Launch Pad')
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
              
        self.B1 = ui.LaunchPadBtn(self, 'Security', 1,  l,  h1)
        self.B2 = ui.LaunchPadBtn(self, 'Climate',  2,  m,  h1)
        self.B3 = ui.LaunchPadBtn(self, 'Cameras',  3,  r,  h1)
        
        self.B4 = ui.LaunchPadBtn(self, 'Lighting', 4,  l,  h2)
        self.B5 = ui.LaunchPadBtn(self, 'Listen',   5,  m,  h2)
        self.B6 = ui.LaunchPadBtn(self, 'Admin',    6,  r,  h2)