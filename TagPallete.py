import GlobalFunctions as gf
import GlobalVariables as gv
from tkinter import *
import tkinter as tk
from PopupMenus import WidgetPopup as wp

################################################################################ 
class CreateTagElementMeta():
    
    def __init__(self, tagName):

        self.tagName     = tagName
        self.valueDict   = {}
        self.han_create_attr_from_structure()
        
    def han_create_attr_from_structure(self):
        for i in gv.tagElementStructure:
            setattr(self, i, None)
            self.valueDict[i] = None
                
    def get_value_dict(self):
        return self.valueDict 
    
    def han_update_meta(self, name, value):
        setattr(self, name, value)
        self.valueDict[name] = value

################################################################################ 
class TagElementFactory():
      
    def __init__(self, parent, tagName):
        
        self.parent    = parent
        self.canvas    = self.parent.canvas
        self.w         = self.parent.w
        self.h         = self.parent.h
        self.shapeType = 'Rectangle'
        self.tagName   = tagName
        self.shape     = self.canvas.create_rectangle

        self.createTagElement()
                    
    def createTagElement(self):
        elementMeta = CreateTagElementMeta(self.tagName)
        
        xRange = (0,int(self.w/2))
        randomX = gf.randomCoord(xRange)
        
        yRange = (0,int(self.h/2))
        randomY = gf.randomCoord(yRange)
        
        elementMeta.han_update_meta('x1', randomX)
        elementMeta.han_update_meta('y1', randomY)
        gv.tagElements[self.tagName] = elementMeta
        
        self.objectId = self.shape(
                                   randomX, randomY, 
                                   randomX+60, randomY+30,
                                   tags=(self.shapeType, self.tagName)
                                   )
        
################################################################################         
class TagElementConfig():

    def __init__(self, parent, tagName):
        self.parent    = parent
        self.canvas    = self.parent.canvas    
        
        self.handleObjectEventBindings(tagName)
        self.handleObjectInitFill(tagName)
        
    def handleObjectEventBindings(self, tagName):
        
        self.canvas.tag_bind(tagName, '<Any-Enter>', self.parent.onMouseEnter)
        self.canvas.tag_bind(tagName, '<Any-Leave>', self.parent.onMouseExit)            
        self.canvas.tag_bind(tagName, '<ButtonPress-2>',  self.parent.popup)
        self.canvas.tag_bind(tagName, '<ButtonPress-3>',  self.parent.popup)

    def handleObjectInitFill(self, tagName):
        self.canvas.itemconfig(tagName, fill='white')

################################################################################ 
class TagElementEdit():
    
    def __init__(self, parent, tagName):
        
        self.parent    = parent
        self.tagName   = tagName
        self.canvas    = self.parent.canvas
        x1, y1, x2, y2 = self.parent.getWidgetCoords(tagName)
        self.x1        = x1
        self.y1        = y1
        self.x2        = x2
        self.y2        = y2
                
    def onObjectGrow(self, event):        
        self.canvas.coords(self.tagName,
                       self.x1, 
                       self.y1, 
                       event.x, 
                       event.y,
                       ) 
    
    def onObjectMove(self, event):
        x, y = (event.x - self.x1), (event.y - self.y1)       
        self.canvas.move(self.tagName, x, y)

    def manualObjectGeometry(self, sizeTuple):
        x, y, w, h = sizeTuple
        x1 = w+x
        y1 = h+y 
        self.canvas.coords(self.tagName, x, y, x1, y1)
         
################################################################################
     
class LoadTagElement():
    
    def __init__(self, parent, tagName):
        
        self.parent      = parent
        self.canvas      = self.parent.canvas
        self.elmt        = gv.tagElements[tagName]
        self.tagName     = tagName
        self.shapeType   = 'Rectangle'
        self.shape       = self.canvas.create_rectangle
        
        self.han_load_tag_element()
  
    def han_load_tag_element(self):
        self.objectId = self.shape(
                                   self.elmt.x1, self.elmt.y1, 
                                   self.elmt.x2, self.elmt.y2,
                                   tags=(self.shapeType, self.elmt.tagName)
                                   )
                
################################################################################
class TagCanvas(tk.Frame): 
    
    def __init__(self, parent, w, h):
        self.parent = parent
        canvas      = Canvas(width=w, height=h)
        self.image  = gf.getBluePrintImageForWidget()     
        canvas.pack()
        canvas.create_image(0,0, image=self.image, anchor='nw')
        
        self.ux           = parent.ux
        self.w            = w
        self.h            = h            
        self.canvas       = canvas
        self.canvasObj    = self.canvas 
  
    def getWidgetCoords(self, tagName):
        return self.canvas.coords(tagName)
     
    def onRemoteSelect(self, tagName, color='pink'):
        self.canvas.itemconfig(tagName, fill=color)
      
    def onMouseEnter(self, event):       
        tagName =  self.getCurrentTagName()     
        self.parent.han_obj_hover_alert(tagName)
        self.canvas.itemconfig(tagName, fill='grey')
        
        mouseX, mouseY = (event.x,event.y)
        x1, y1, x2, y2 = self.getWidgetCoords(tagName)
        
        if mouseX > (x2-5) and mouseX <= x2 or mouseY <= y2 and mouseY > (y2-5):
            event.widget.configure(cursor='sizing')
            self.canvas.tag_bind(tagName, '<ButtonPress-1>',  self.onObjectResize)
            self.canvas.tag_bind(tagName, '<B1-Motion>',  self.onObjectResize)
        else:
            event.widget.configure(cursor='hand1')
            self.canvas.tag_bind(tagName, '<ButtonPress-1>',  self.onObjectMove)
            self.canvas.tag_bind(tagName, '<B1-Motion>',  self.onObjectMove)
    
    def onMouseExit(self, event):  
        tagName = self.getCurrentTagName()
        self.canvas.itemconfig(tagName, fill='white')
        event.widget.configure(cursor='arrow')
                
    def popup(self, event):
        self.wp = wp(self)
        tagName = self.getCurrentTagName()
        self.wp.popup(event, tagName)
        
    def getCurrentTagName(self):
        objectId = self.canvas.find_withtag("current")[0]
        tagName  =  self.canvas.gettags(objectId)[1]
        return tagName
        
    def onObjectResize(self, event):
        tagName  = self.getCurrentTagName()
        TagElementEdit(self, tagName).onObjectGrow(event)
    
    def onObjectMove(self, event):
        tagName  = self.getCurrentTagName()
        TagElementEdit(self, tagName).onObjectMove(event)
        
    def setObjectGeometry(self, sizeTuple, tagName):
        TagElementEdit(self, tagName).manualObjectGeometry(sizeTuple)

    def getObjectGeometry(self, tagName, var=None):
        coords = self.getWidgetCoords(tagName)
        return gf.getGeometryFromCoor(coords,var)
    
    