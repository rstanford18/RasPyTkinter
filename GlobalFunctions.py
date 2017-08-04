import random
import GlobalVariables as gv
from sys import platform
import base64
import socket

def getPathforImage():
    
    if socket.gethostname() == 'DESKTOP-AB68VHC':
        return gv.personalPCPhoto
 
    if platform == 'darwin':
        return gv.macPhotoPath
    else:
        return gv.winPhotoPath
###################################################
def getPathForIni():
    
    if socket.gethostname() == 'DESKTOP-AB68VHC':
        return gv.personalPCIni

    if platform == 'darwin':
        return gv.macConfigPath
    else:
        return gv.winConfigPath
    
###################################################
def getAvailablePiNameList():

    return [i for i in gv.piFactoryXConnect]

###################################################
def getAvailablePiIPList():
  
    return list(gv.piFactoryXConnect.values())
  
###################################################
def handleGetAvailableTagName(CanvasTags):
    
    masterList  =  set(CanvasTags+[i for i in gv.tagElements])
    l = []
    for i in masterList:
        l.append((int(i.split('-')[1].strip())))
    
    l = sorted(l)
    if len(l) < 1:
        lenL = 24
    else:
        lenL = max(l)*4
        
    for i in range(1,lenL):
        if i not in l:
            return i

###################################################
def getImageForWidget():
    from tkinter import PhotoImage
    photo  = PhotoImage(file=getPathforImage())
    return photo

###################################################
def getGeometryFromCoor(coords, var=None):
    x1, y1, x2, y2 = coords
    w = int(x2-x1)
    h = int(y2-y1)
    
    if var == 'x1':
        return int(x1)
    
    if var == 'y1':
        return int(y1)
    
    if var == 'x2':
        return int(x2)
    
    if var == 'y2':
        return int(y2)
    
    if var == 'w':
        return int(w)
    
    if var == 'h':
        return int(h) 
    else:
        return {'width':w,'height':h,'x1':int(x1),
                'y1':int(y1),'x2':int(x2),'y2':int(y2)}
###################################################

def decryptPassword(pWord):
    passWord = base64.b64decode(pWord)
    return passWord

###################################################

def encodePassword(pWord):

    passWord = base64.b64encode(pWord)
    return passWord 


###################################################
def isPasswordValid(pWord):
    
    encodedPass = encodePassword(pWord.encode('ascii'))
    print(encodedPass)
    storedPass = gv.password
    print(storedPass)
    if encodedPass == storedPass:
        return True
    else:
        return False

##################################################

def randomColor(self):

    foo = ['blue', 'yellow', 'purple']
    return random.choice(foo)

def randomCoord(pRange):
    a, b = pRange
    
    return random.randint(a, b)

###################################################
def getAvailableGPIO():
    gv.gpioStateDict
    l = [gv.tagElements[i].GPIO for i in gv.tagElements]
    al = []
    for i in gv.gpioStateDict:
        if i not in l:
            al.append(i)
     
    return al             
      
###################################################
import tkinter as tk


class GetWidgetAttributes:
    @staticmethod
    def get_attributes(widget):
        widg = widget
        keys = widg.keys()
        for key in keys:
            print("Attribute: {:<20}".format(key), end=' ')
            value = widg[key]
            vtype = type(value)
            print('Type: {:<30} Value: {}'.format(str(vtype), value))


###################################################

def updateTextVar(inst,value=None):
    currentValues = inst.get()       

    if value == None:
        pString = '' 
    elif currentValues == "":
        pString = str(value)
    else:
        pString = currentValues + str(value)

    inst.set(pString)
        
###################################################

def undoTextVar(inst):
    currentValues = inst.get()       

    if currentValues == "":
        pass
    else:
        pString = currentValues[:-1]
        inst.set(pString)
    
        
###################################################        
def geometry(root):

    windowWidth  = root.winfo_screenwidth()
    windowHeight = root.winfo_screenheight()  

    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    x = int((sw/2)-(windowWidth/2))
    y = int((sh/2)-(windowHeight/2))

    geometryString = "%sx%s+%s+%s" % (windowWidth-8,windowHeight,x,y)
    return geometryString       