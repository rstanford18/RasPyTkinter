import random
import GlobalVariables as gv
from sys import platform
import base64
import socket
import pprint

def ppr(value):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(value)

def getBluePrintPathforImage():
    return gv.imgBluePrint

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

def getBluePrintImageForWidget():
    from tkinter import PhotoImage
    return PhotoImage(file=getBluePrintPathforImage())

###################################################

def getGeometryFromCoor(coords, var=None):
    x1, y1, x2, y2 = list(map(int, coords))

    w = x2 - x1
    h = y2 - y1

    coordDict = {
        'x1'        : x1,
        'y1'        : y1,
        'x2'        : x2,
        'y2'        : y2,
        'w'         : w,
        'h'         : h,
        'width'     : w,
        'height'    : h
    }
    
    return coordDict.get(var, coordDict)
   
###################################################

def decryptPassword(pWord):
    return base64.b64decode(pWord)

###################################################

def encodePassword(pWord):
    return base64.b64encode(pWord.encode('ascii'))

###################################################

def isPasswordValid(pWord):
    return bool(encodePassword(pWord) == gv.password)

##################################################

def randomColor(self):
    foo = ['blue', 'yellow', 'purple']
    return random.choice(foo)

def randomCoord(pRange):
    return random.randint(*pRange)

###################################################

def getAvailableGPIO():
    tags = [gv.tagElements[i].GPIO for i in gv.tagElements]
    activeTags = []
    for tag in gv.gpioStateDict:
        if tag not in tags:
            activeTags.append(tag)

    return activeTags

###################################################
# Not Currently Implemented
###################################################
# import tkinter as tk

# class GetWidgetAttributes:
#     @staticmethod
#     def get_attributes(widget):
#         widg = widget
#         keys = widg.keys()
#         for key in keys:
#             print("Attribute: {:<20}".format(key), end=' ')
#             value = widg[key]
#             vtype = type(value)
#             print('Type: {:<30} Value: {}'.format(str(vtype), value))

###################################################

def updateTextVar(parent, value=None):
    currentValues = parent.get()

    if value == None:
        pString = ''
    elif currentValues == "":
        pString = str(value)
    else:
        pString = currentValues + str(value)

    parent.set(pString)

###################################################

def undoTextVar(parent):
    currentValues = parent.get()

    if currentValues == "":
        pass
    else:
        pString = currentValues[:-1]
        parent.set(pString)


###################################################
# TO BE DELETED - 08/7/2017
###################################################
# def geometry(root):

#     windowWidth  = root.winfo_screenwidth()
#     windowHeight = root.winfo_screenheight()

#     sw = root.winfo_screenwidth()
#     sh = root.winfo_screenheight()

#     x = int((sw/2)-(windowWidth/2))
#     y = int((sh/2)-(windowHeight/2))

#     geometryString = "%sx%s+%s+%s" % (windowWidth-8,windowHeight,x,y)
#     return geometryString