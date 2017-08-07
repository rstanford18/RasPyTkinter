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
from Camera_Popup import CameraPopUpView as cpv
from copy import deepcopy

##############################################################################  
class CameraView(tk.Frame):
    def __init__(self, parent, nav):
        tk.Frame.__init__(self, parent, bg=gv.bckGround)   
###
        self.parent      = parent       
        self.nav         = nav
        self.mb          = mb(self)
        self.menu        = nav.parent.config(menu=self.mb.getMenu()) 
        self.ux          = self.nav.ux
        self.ux.han_change_title('CameraView')
        self.objDataMgr  = self.nav.launch.ObjDataMgr 
        self.gridSizeCfg = [1,4,8,16]
        self.gridDict    = {1:(0,0), 4:(2,2), 8:(4,2) ,16:(4,4)}
        self.han_init_ooe()
        
    def han_init_ooe(self):
        self.han_init_cam_fac()
        self.get_grid_pattern()
        self.han_init_frame_grid()
    
    def han_init_cam_fac(self):
        self.camFac     = CameraFactory(self)
        self.camList    = self.camFac.camList
        self.camListLen = len(self.camFac.camList)
        
    def get_grid_pattern(self):
        for i in self.gridSizeCfg:
            if self.camListLen <= i:
                self.gridSize = i
                break
    
    def han_init_frame_grid(self):
        for i in range(0, self.camListLen):
            self.han_create_frames(i)
    
    def han_create_frames(self, item):
        cGeo = self.ux.get_curr_coords('all')
        geoDict = self.han_grid_spacing(self.gridSize, item, cGeo[2], cGeo[3])
        h = geoDict['h']
        w = geoDict['w']
        x = geoDict['x']
        y = geoDict['y']
        f = tk.Frame(self, height=h, width=w, highlightbackground="#686868", 
                        highlightcolor="#686868", highlightthickness=1,)
        f.pack_propagate(0) # don't shrink
        f.place(x=x, y=y)
        self.camList[item].han_set_item_value(item)
        self.camList[item].han_start_stream(f, w, h)
                      
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

##############################################################################         
class CameraFactory():
    
    def __init__(self, parent):
        
        self.parent  = parent
        self.ux      = parent.ux
        self.camList = []
        self.han_init_ooe()
        
    def han_init_ooe(self):
        self.han_create_camera()
       
    def get_active_cameras(self):
        return gv.camElements
    
    def han_create_camera(self):
        
        self.activeCams =  self.get_active_cameras()
        
        for i in self.activeCams:
           
            if self.activeCams[i].get('Enabled', False):
                
                cam = CameraElementMeta(self, i, self.activeCams[i])
                self.camList.append(cam)
      
##############################################################################      
class CameraElementMeta():
    
    def __init__(self, parent, camName, camDict):
        self.parent = parent
        self.camName = camName
        self.camDict = camDict
        self.ux      = parent.ux
        self.han_activate_stream()
        self.img     = None
        self.w       = None
        self.h       = None
        self.frame   = None
    
    def han_init_ooe(self):
        self.get_init_img()
          
    def han_start_stream(self, frame, w, h):
        self.frame = frame
        self.w     = w
        self.h     = h
        self.han_init_cam_panel() 
        self.han_panel_stream()      
           
    def han_activate_stream(self):
        self.camThread = CameraStream(self.camName, self.camDict)
    
    def get_active_frame(self):
        return self.camThread.displayImg
    
    def get_init_img(self):
        try:
            img      = self.get_active_frame()
            img      = Image.fromarray(img)
            if self.w != None:
                basewidth = self.w
                wpercent = (basewidth/float(img.size[0]))
                hsize = int((float(img.size[1])*float(wpercent)))
                img = img.resize((basewidth,hsize), Image.ANTIALIAS)
                self.img = ImageTk.PhotoImage(img)
            else:    
                self.img = ImageTk.PhotoImage(img)
        except cv2.error as e:
            pass
    
    def han_init_cam_panel(self):         
        self.panel = tk.Label(self.frame, image=self.img, bg=gv.bckGround)
        self.panel.pack(side="bottom", fill="both", expand="yes")
        self.panel.bind('<ButtonPress-1>', self.on_mouse_enter)
    
    def on_mouse_enter(self, event):
        
        cpv(self)
    def han_set_item_value(self, item):
        self.item = item
    
    def han_panel_stream(self):
        self.get_init_img()
        #print(self.camName, 'Panel Stream Alive')
        self.panel.configure(image=self.img)
        self.panel.image = self.img
        self.panel._backbuffer_ = self.img
        self.panel.after(100, self.han_panel_stream)

##############################################################################  
class CameraStream():
      
    def __init__(self, cameraName, camDict):              
        self.get_connecting_img()
        self.displayImg    = self.connectingImg
        self.camName       = cameraName
        self.camDict       = camDict
        self.han_init_ooe()
            
    def han_init_ooe(self):
        self.han_get_cam_params()
        self.han_construct_url()
        self.get_failed_img()
        self.k = Thread(target=self.han_get_cam_feed)     
        self.k.start()
    
    def get_connecting_img(self):
        img = Image.open(gv.imgConnect).convert("L")
        arr = numpy.array(img)
        self.connectingImg = arr
      
    def get_failed_img(self):
        img = Image.open(gv.imgOffline).convert("L")
        arr = numpy.array(img)
        self.failedImg = arr
           
    def han_get_cam_params(self):
  
        for i in self.camDict:
            setattr(self, str(i).lower(), self.camDict[i])
    
    def han_construct_url(self):
        self.port = ':'+self.port if self.port != '' else ''
        
        if self.user == '': 
            self.url = '%s%s%s' % (self.url, self.port, self.path)
        
        if self.user != '':
            self.port = ':'+self.port if self.port != '' else ''
            self.url = self.url.split('//')
            self.url = self.url[0]+'//'+self.user+':'+self.password+'@'+self.url[1]
            self.url = '%s%s%s' % (self.url, self.port, self.path)
   
    def get_stream_data(self):
        return cv2.VideoCapture(self.url)
    
    def han_get_cam_feed(self):
        cap = self.get_stream_data()
        keepAlive = True
        failCount = 0
        while True:
            if keepAlive == False:
                cap = self.get_stream_data()
                keepAlive = True
            try:
                ret, frame = cap.read()        
                keepAlive = ret        
            except cv2.error as e:
                pass
            try:
                '''test the frame element if it has no shape property
                its invalid and the exception handles the dislplay.'''
                shp = frame.shape 
                self.displayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                failedCount = 0
            except:
                self.displayImg = self.failedImg      
                failCount += 1
#             if self.camName == 'BankOfAmerica':
#                 print('Camera:',self.camName,'Thread State:','Alive', id(self.parent))
            if failCount > 1000:
                    break   
                
            if cv2.waitKey(1) == 27:
                exit(0)
        print('Camera:',self.camName,'Thread State:','Dead')
