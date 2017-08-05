from tkinter import BOTH, Frame, LabelFrame, Label, Text, Checkbutton, IntVar, StringVar, Button, NORMAL, DISABLED, Widget, Entry, ttk
import tkinter as tk
import GlobalVariables as gv
import GlobalFunctions as gf
import UIWidgets as ui




class AdminCameraCfg(tk.Frame):
    
    def __init__(self, parent, nav):

        tk.Frame.__init__(self, parent, bg=gv.bckGround)
        self.nav         = nav
        self.ux          = self.nav.ux
        self.ux.han_change_title('Admin - Camera Config')
        self.menu        = nav.parent.config(menu=self.mb.getMenu()) 
        self.pVar        = StringVar()
        self.cbVar       = IntVar()        
        self.entrySettings   = gv.entrySettings


        self.w  = w
        self.ux = parent.ux
        self.canvas = parent.canvas
        self.frame = tk.Frame(self.parent, height=h, width=w, 
                              highlightbackground='white', highlightcolor='white', highlightthickness=1,)
        self.frame.pack_propagate(0) # don't shrink
        self.frame.place(x=x, y=y)
        self.initTreeView()
        self.prevSelection = None
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', background='black', 
                fieldbackground='black', foreground='white')
    
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
       
        self.popupWindowUI()

    def popupWindowUI(self):
        self.positionEntry()
        self.buttonsUI()       
    
    def positionEntry(self):
        
        gp1y = 5
        self.group1 = LabelFrame(self.frame ,text="GPIO",
                           width=420,
                           height=50,
                           font=gv.NORMAL_FONT,
                           bg=gv.bckGround,
                           fg=gv.forGround)
        self.group1.place(x=15, y=15)       
        #################################################################        
        self.label1 = ui.make_label(self.group1, 15, gp1y, 60, 20, text=self.tagName, 
                                    background=gv.bckGround,foreground=gv.forGround,
                                    font=gv.NORMAL_FONT)

        self.tkvar = StringVar()
        choices = gf.getAvailableGPIO()
        try:
            choices = sorted(choices+[gv.tagElements[self.tagName].GPIO])
            idx = choices.index(gv.tagElements[self.tagName].GPIO)
            #idx = 0
            print(type(gv.tagElements[self.tagName].GPIO))
        except:
            idx = None
        idx = idx if idx != None else 0
        self.tkvar.set(choices[idx]) 
        #self.parent.iconbitmap(default="gear16.ico")
        
        f1 = Frame(self.group1, height=20, width=60, background=gv.bckGround)
        f1.pack_propagate(0)
        f1.place(x=330, y=gp1y)
        self.dropDown1 = tk.OptionMenu(f1, self.tkvar, *choices, command=self.selValue1)
        self.dropDown1.configure(highlightthickness=0,highlightbackground="Black" ,highlightcolor="Black")
        self.dropDown1.pack(fill=BOTH, expand=1)       
    
        self.tkvar1 = StringVar()
        piChoices = gf.getAvailablePiNameList()
        try:
            idx = piChoices.index(gv.tagElements[self.tagName].GPIOParent)
        except:
            idx = None
        idx = idx if idx != None else 0
        self.tkvar1.set(piChoices[idx]) 
        
        f2 = Frame(self.group1, height=20, width=110, background=gv.bckGround)
        f2.pack_propagate(0)
        f2.place(x=125, y=gp1y)
        self.dropDown2 = tk.OptionMenu(f2, self.tkvar1, *piChoices, command=self.selValue2)
        self.dropDown2.configure(highlightthickness=0,highlightbackground="Black" ,highlightcolor="Black")
        self.dropDown2.pack(fill=BOTH, expand=1)    
    
    
    def selValue1(self, value):
        self.value1 = value

    def selValue2(self, value):
        self.value2 = value

        
    def buttonsUI(self):   
        self.B1 = ui.make_OpenCloseBtn(self, 15, 85, 75, 25, self.han_tag_bind, text='Bind', 
                      bg=gv.bckGround, fg='white', font=gv.LARGE_FONT)
        
        self.B2 = ui.make_OpenCloseBtn(self, 115, 85, 75, 25, self.han_tag_unbind, text='UnBind', 
                      bg=gv.bckGround, fg='white', font=gv.LARGE_FONT)
        
        self.B3 = ui.make_OpenCloseBtn(self, 360, 85, 75, 25, self.closeWindow, text='Close', 
                      bg=gv.bckGround, fg='white', font=gv.LARGE_FONT)       

    def buttonClrEnter(self, event):
        event.widget.config(bg='white', fg='black')
    
    def buttonClrLeave(self, event):
        event.widget.config(bg=gv.bckGround, fg='white')
        
    def han_tag_bind(self, event):
        print(self.tkvar1.get())
        print(self.tkvar.get())
        self.callPar.parent.nav.launch.ObjDataMgr.han_item_GPIO_bind(self.tagName, self.tkvar1.get(), self.tkvar.get(), True)     
        self.closeWindow(event)
    
    def han_tag_unbind(self, event):
        self.callPar.parent.nav.launch.ObjDataMgr.han_item_GPIO_bind(self.tagName, '', 0, False)     
        self.closeWindow(event)
    
    def _focusNext(self, widget):
        '''Return the next widget in tab order'''
        widget = self.tk.call('tk_focusNext', widget._w)
        if not widget: 
            return None
        else:
            return self.nametowidget(widget.string)

    def OnTextTab(self, event):
        '''Move focus to next widget'''
        widget = event.widget
        lnext = self._focusNext(widget)
        lnext.focus()
        return "break" 
        
    def closeWindow(self, event):
        self.destroy()















     
        