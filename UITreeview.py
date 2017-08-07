import GlobalVariables as gv
import tkinter as tk
from tkinter import ttk
from PopupMenus import WidgetPopup as wp

class TagManagerView():
    
    def __init__(self, parent, sizeTuple):
        
        self.parent = parent
        x, y, w, h = sizeTuple
        self.w  = w
        self.ux = parent.ux
        self.canvas = parent.canvas
        self.frame = tk.Frame(self.parent, height=h, width=w, 
                              highlightbackground='white', highlightcolor='white', highlightthickness=1,)
        self.frame.pack_propagate(0) # don't shrink
        self.frame.place(x=x, y=y)
        self.initTreeView()
        self.prevSelection = None
#         style = ttk.Style()
#         style.theme_use('clam')
#         style.configure('Treeview', background=gv.bckGround, 
#                 fieldbackground=gv.bckGround, foreground='white')
    
    def initTreeView(self):
        self.tree = ttk.Treeview(self.frame, columns=('Tag Name'))
        self.tree.heading('#0', text='Tag Name')
        self.tree.column('#0', minwidth=80, width=self.w-5, stretch=False)
        self.tree.bind('<Any-Enter>', self.highLightSelection)
        self.tree.bind('<Button-1>', self.highLightSelection)
        self.tree.bind('<Button-2>', self.highLightSelection)
        self.tree.bind('<Button-3>', self.highLightSelection)

        self.tree.bind('<ButtonRelease-2>', self.popup)
        self.tree.bind('<ButtonRelease-3>', self.popup)
        self.tree.pack(fill=tk.BOTH, expand=1)
        self.treeview = self.tree
        self.treeViewObj = self.treeview
        
    def popup(self, event):
        try:
            tagName = self.getCurrentTagName(event)
            self.wp = wp(self.parent.TagCvs)              
            self.wp.popup(event, tagName)
        except:
            pass
    
    def highLightSelection(self, event=None, tagName=None):
        if event != None:
            selIdx  = self.tree.identify_row(event.y)
            self.tree.selection_set(selIdx)
            try:
                tagName = self.getCurrentTagName(event)
                self.parent.TagCvs.onRemoteSelect(tagName,'yellow')
            except:
                pass
        
        else:
            selIdx = self.selectItem(tagName)
        
        self.tree.selection_set(selIdx)     
             
        if self.prevSelection != None:
            self.parent.TagCvs.onRemoteSelect(self.prevSelection,'white') 
        
        self.prevSelection = tagName
        
    def getCurrentTagName(self, event):
        self.selection = self.tree.set(self.tree.identify_row(event.y))
        tagName = self.selection['Tag']
        return tagName
                
    def selectItem(self, tagName):
         
        for child in self.treeview.get_children():
            tagNameValue = self.treeview.item(child)['values'][0]
            if tagNameValue == tagName:
                return child
