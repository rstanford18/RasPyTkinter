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
        print('camlen',self.camListLen)
        for i in range(0,self.gridSize):
            geoDict = self.han_grid_spacing(self.gridSize,i, self.ux.sw, self.ux.sh)
            h = geoDict['h']
            w = geoDict['w']
            x = geoDict['x']
            y = geoDict['y']
            
            f = tk.Frame(self, height=h, width=w, highlightbackground="#00FF00", 
                            highlightcolor="#00FF00", highlightthickness=1,)
            f.pack_propagate(0) # don't shrink
            f.place(x=x, y=y)
            print('in loop',self.camList[i].camName)
            pnl.pack(side="bottom", fill="both", expand="yes")
        
    def han_grid_spacing(self, size, itemCount, w, h):
        spacingDict = {}
        
        if size == 1:
            spacingDict = {}
            spacingDict[0] = {'x':0,'y':0,'w':w,'h':h}
            return spacingDict[0]
        
        
        gridSizeCfg = [1,2,4,6,8,12,16]
        gridDict    = {1:(0,0), 4:(2,2), 8:(4,2), 12:(4,3), 16:(4,4)}
        
        
        
        c, r = gridDict[size]
        
        objW = int(w/c)
        objH = int(h/r)
        
        item = 0
        for k in range(0,r):
            y = k*objH
            for i in range(0,c):
                w = objW
                x = i*objW
                spacingDict[item] = {'x':x,'y':y,'w':w,'h':objH}
                item += 1
        
        #print(spacingDict[item])   
        return spacingDict[itemCount]
        
        
class CameraFactory(tk.Frame):
    
    def __init__(self, parent):
        
        tk.Frame.__init__(self, parent)
        self.parent  = parent
        self.camList = []
        self.han_init_ooe()
        
    def han_init_ooe(self):
        self.han_create_camera()
       
    def get_active_cameras(self):
        return gv.ActiveCameras
    
    def han_create_camera(self):
        
        self.activeCams =  self.get_active_cameras()
        
        for i in self.activeCams:
             cam = CameraElementMeta(self, i, self.activeCams[i])
             self.camList.append(cam)
    
    
    
    
class CameraElementMeta(tk.Frame):
    
    def __init__(self, parent, camName, camDict):
        tk.Frame.__init__(self, parent) 
        self.parent = parent
        self.camName = camName
        self.camDict = camDict
        self.han_activate_stream()
        self.img = None
        self.parent.after(200, self.han_init_ooe)
    
    def han_init_ooe(self):
        self.get_init_img()
        self.han_init_cam_panel() 
        self.han_panel_stream()
       
    def han_activate_stream(self):
        self.camThread = CameraStream(self.camName, self.camDict)
    
    def get_active_frame(self):        
        return self.camThread.cImgFrame
    
    
    def get_init_img(self):
        try:
            img      = cv2.cvtColor(self.get_active_frame(), cv2.COLOR_BGR2RGB)
            img      = Image.fromarray(img)
            self.img = ImageTk.PhotoImage(img)
        except:
            print('failed')
    
    def han_init_cam_panel(self):
            
        self.panel = tk.Label(self.parent, image=self.img)
        self.panel.pack(side="bottom", fill="both", expand="yes")
    
     
    def han_panel_stream(self):
        self.get_init_img()
        self.panel.configure(image=self.img)
        self.panel.image = self.img
        self.panel._backbuffer_ = self.img
        print('hum repeater', self.camName)
        self.panel.after(100, self.han_panel_stream)
    
    def printTest(self):
        print('here is muh print testttttt')

class CameraStream():
      
    def __init__(self, cameraName, camDict):        
        self.cImgFrame = None
        self.camName = cameraName
        self.camDict = camDict
        self.han_init_ooe()
            
    def han_init_ooe(self):
        self.han_get_cam_params()
        self.han_construct_url()
        self.k = Thread(target=self.han_get_cam_feed)     
        self.k.start()
        
    def han_get_cam_params(self):
  
        for i in self.camDict:
            setattr(self, i, self.camDict[i])
    
    def han_construct_url(self):
        self.port = ':'+self.port if self.port != '' else ''
        
        if self.user == '': 
            self.url = '%s%s%s' % (self.url, self.port, self.path)
        
        if self.user != '':
            self.port = ':'+self.port if self.port != '' else ''
            self.url = self.url.split('//')
            self.url = self.url[0]+'//'+self.user+':'+self.passw+'@'+self.url[1]
            self.url = '%s%s%s' % (self.url, self.port, self.path)
   
    def get_stream_data(self):
        return cv2.VideoCapture(self.url)
    
    def han_get_cam_feed(self):

        cap = self.get_stream_data()
        keepAlive = True
        while True:
            if keepAlive == False:
                cap = self.get_stream_data()
                keepAlive = True
            try:
                ret, frame = cap.read()
                keepAlive = ret
            except:
                pass
           # print(frame)
            self.cImgFrame = frame
            
            #cv2.imshow('Video', frame)
            if cv2.waitKey(1) == 27:
                exit(0)
        print('Camera:',self.camName,'Thread State:','Dead')



# root = tk.Tk() 
# cam = CameraView('SteritecSecurity', root)   
# #root.bind("<Return>", callback)
# root.mainloop()

