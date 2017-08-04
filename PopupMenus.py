import tkinter as tk
from tkinter import Menu
import PopupWindows as pw

class WidgetPopup(Menu):
    def __init__(self, parent):
        Menu.__init__(self, None,  tearoff=0)        
        self.tagName = None
        self.parent  = parent

    def getTagName(self):
        return self.tagName
    
    def menu_one(self):
        pw.SizePopupWindow(self)

    def menu_two(self):
        print( "two...")

    def menu_three(self):
        pw.GPIOBind(self)
    
    def menu_four(self):
        print(self.parent.parent.nav.launch.ObjDataMgr.han_data_harmony('remove', self.tagName))
        
    def addMenuItems(self):
        self.add_command(label='Size', command=self.menu_one)
        self.add_command(label="Tag Name", command=self.menu_two)
        self.add_command(label="GPIO Binding", command=self.menu_three)
        self.add_command(label="Delete %s" % self.tagName, command=self.menu_four)

    def popup(self, event, tagName):
               
        self.tagName = tagName
        self.addMenuItems()
        self.event = event
        self.tk_popup(event.x_root, event.y_root)
