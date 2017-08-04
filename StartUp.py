import tkinter as tk
from tkinter import BOTH, Frame
import GlobalVariables as gv
import CfgEnviroment as envir
envir.defineEnviroment()
 
isGPIOOn = True
if isGPIOOn:
    import GPIOThreadClass as tb
    
import Config as cf

from Overview  import OverviewPage     as op
from Login     import LoginPage        as lp
from LaunchPad import LaunchMain       as lm
from DataLayer import MainObjectDataHandler
from Climate   import ClimateMain       as cm

from Camera import CameraView as camv
################################################################################
class SystemInfo():
    
    def __init__(self, root, nav):
        root.update_idletasks()
        self.root = root
        self.nav = nav
        self.sw = root.winfo_screenwidth()
        self.sh = root.winfo_screenheight()
        self.g  = root.winfo_geometry()

    def han_change_title(self, title):
        self.nav.han_change_title(title)

    def getHorizontalCenter(self, px):
        return int((self.sw/2)-(px/2))
    
    def getVerticalCenter(self,px):   
        return int((self.sh/2)-(px/2))
   
    def getPopUpLocation(self, w, h):
        self.root.update_idletasks()
        popUpWidth  = w
        popUpHeight = h
        rootGeometry = self.root.geometry()
    
        xy = rootGeometry.split('+',1)[1].split('+')
        wh = rootGeometry.split('+',1)[0].split('x')
       
        pW = int(wh[0])
        pH = int(wh[1])
        pX = int(xy[0])
        pY = int(xy[1])
        
        x = int(pX+(pW/2)-(popUpWidth/2))
        y = int(pY+(pH/2)-(popUpHeight/2))
    
        popUpGeometry = "%sx%s+%s+%s" % (popUpWidth,popUpHeight,x,y)

        return popUpGeometry   
 
################################################################################ 
class NavigationManager(Frame):
    
    def __init__(self, parent, launch):
 
        Frame.__init__(self, parent, bg=gv.bckGround) 
        self.cFrame = None
        self.parent = parent  
        self.launch = launch
        self.ux     = self.launch.ux 
       
        self.showFrame(lp)

    def showFrame(self, nav):

        if self.cFrame != None:
            self.nav.pack_forget()
        
        self.nav = Frame(self.parent, bg=gv.bckGround)
        self.nav.pack(fill=BOTH, expand=1)           
        
        self.frame = nav(self.nav, self)
        self.cFrame = self.frame
        self.frame.pack(fill=BOTH, expand=1)
        self.frame.tkraise()
                   
    def showOverviewPage(self):
        self.showFrame(op)
    
    def showLoginPage(self):
        self.showFrame(lp)
              
    def showLaunchPad(self):
        self.showFrame(lm)
    
    def showClimatePage(self):
        self.showFrame(cm)
    
    def showCameraPage(self):
        self.showFrame(camv)     
################################################################################ 
class Launch():
    
    def __init__(self):
        
        root = tk.Tk()
        cf.loadConfigFile()
        self.titleVar = tk.StringVar()
        self.titleVar.set("SA Smart Home - Login")
        self.isGPIOOn = isGPIOOn
        
        if self.isGPIOOn:
            self.scan = tb.GPIOSimulator(self)
            self.scan.startUXIndicatorStatus()
        #root.attributes('-fullscreen', True)
        root.title(self.titleVar.get())

        root.geometry('%dx%d+%d+%d' % (1910, 1055, 1920, 0))
#         self.var.set(root.title())
        self.root = root
        self.ux      = SystemInfo(root, self)
        self.ObjDataMgr = MainObjectDataHandler(self)
            
        self.nvm = NavigationManager(root, self)    
        root.mainloop()
    
    def han_change_title(self,pTitle):
        self.titleVar.set(pTitle)
        self.root.title("SA Smart Home - %s" % self.titleVar.get())
        self.root.update_idletasks()
                
###################################################
if __name__ == '__main__':
    strup = Launch()