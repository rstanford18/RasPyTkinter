import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread
import cv2
import GlobalVariables as gv
import GlobalFunctions as gf
import UIWidgets as ui
import UITreeview as uitv
from ClockThread import Clock as ck
from MenuBar import MainMenuBar as mb
import numpy

##############################################################################  
class CameraPopUpView(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, bg=gv.bckGround)   
       
        self.protocol("WM_DELETE_WINDOW", self.han_destroy_call_back)
        self.parent      = parent
        self.parent.panel.unbind('<ButtonRelease-1>')      
        self.ux          = parent.ux
        self.ux.han_change_title('CameraView')
        self.gridSizeCfg = [1,4,8,16]
        self.gridDict    = {1:(0,0), 4:(2,2), 8:(4,2) ,16:(4,4)}
        
        self.w = self.ux.get_curr_coords('w')
    
        self.h = self.w 
        geometry = self.ux.get_popup_location(self.w,self.h)

        self.geometry(geometry)
        
        self.han_init_ooe()
    
    def han_destroy_call_back(self):
        self.parent.parent.parent.han_create_frames(self.parent.item)
        self.destroy()
    
        
    def han_init_ooe(self):
        self.han_init_cam_fac()
        self.get_grid_pattern()
        self.han_init_frame_grid()
    
    def han_init_cam_fac(self):

        self.camList    = [self.parent]
        self.camListLen = len(self.camList)
        
    def get_grid_pattern(self):
        for i in self.gridSizeCfg:
            if self.camListLen <= i:
                self.gridSize = i
                break
    
    def han_init_frame_grid(self):
        for i in range(0, self.camListLen):
            cGeo = self.ux.get_curr_coords('all')
            geoDict = self.han_grid_spacing(self.gridSize,i, cGeo[2], cGeo[3])
            h = geoDict['h']
            w = geoDict['w']
#             x = geoDict['x']
#             y = geoDict['y']
#             f = tk.Frame(self, height=self.h, width=self.w, highlightbackground="#00FF00", 
#                             highlightcolor="#00FF00", highlightthickness=1,)
#             f.pack_propagate(0) # don't shrink
#             f.place(x=0, y=0)
            self.camList[i].han_start_stream(self, w, h)
                  
    def han_grid_spacing(self, size, itemCount, w, h):
        spacingDict = {}
        oriH = h
        if size == 1:
            spacingDict = {}
            spacingDict[0] = {'x':(w/2)/2,'y':0,'w':h,'h':h}                              
            return spacingDict[0]
        
        c, r = self.gridDict[size]
        xPadStart = 200
        pw = w-(xPadStart*2)
        
        #Lets figure out the area we are working with.
        colSquare = int(pw/c)
        rowSquare = int(h/r)
        
        w = min(colSquare,rowSquare)
        h = w
        yOffset = (oriH - (h*r))/2
        xPadStart = xPadStart+((pw-(c*w))/2)

        item = 0
        prevX = 0
        for k in range(0,r):
            y = (k*h)+yOffset
            for i in range(0,c):
                if i == 0:
                    x = xPadStart
                    prevX = x
                else:
                    x = prevX+w
                    prevX = x
                spacingDict[item] = {'x':x, 'y':y, 'w':w, 'h':h}
                item += 1

        return spacingDict[itemCount]



