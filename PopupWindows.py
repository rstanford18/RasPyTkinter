from tkinter import BOTH, Frame, LabelFrame, Label, Text, Checkbutton, IntVar, StringVar, Button, NORMAL, DISABLED, Widget, Entry, ttk
import tkinter as tk
import GlobalVariables as gv
import GlobalFunctions as gf
import UIWidgets as ui


class SizePopupWindow(tk.Toplevel):
    
    def __init__(self, parent):

        tk.Toplevel.__init__(self)
        ##

        self.callPar   = parent.parent
        self.ux        = parent.parent.ux

        w = 200
        h = 180  
        geometry = self.ux.get_popup_location(w,h)

        self.geometry(geometry)
        self.pVar = StringVar()
        self.cbVar = IntVar()
        self.tagName = parent.tagName
        self.title("(%s) x,y & w,h " % self.tagName)
#         
        self.entrySettings   = gv.entrySettings
        self.frame = Frame(self, background=gv.bckGround) 
           
        #self.parent.iconbitmap(default="gear16.ico")
    
        self.frame.pack(fill=BOTH, expand=1)               
       
        self.popupWindowUI()

    def popupWindowUI(self):
        self.positionEntry()
        self.sizeEntry()
        self.buttonsUI()       
    
    def positionEntry(self):
        
        gp1y = 5
        self.group1 = LabelFrame(self ,text="Position",
                           width=170,
                           height=50,
                           font=gv.NORMAL_FONT,
                           bg=gv.bckGround,
                           fg=gv.forGround)
        self.group1.place(x=15, y=15)       
        #################################################################        
        self.label1 = ui.make_label(self.group1, 15, gp1y, 20, 20, text="X:", 
                                    background=gv.bckGround,foreground=gv.forGround,
                                    font=gv.NORMAL_FONT)

        self.text1 = ui.make_TextEntry(self.group1, 35, gp1y, 35, 20, font=gv.NORMAL_FONT)
        self.text1.insert('end', self.callPar.getObjectGeometry(self.tagName,'x1'))
        #################################################################
        self.label2 = ui.make_label(self.group1, 85, gp1y, 20, 20, text="Y:", 
                                    background=gv.bckGround,foreground=gv.forGround
                                    ,font=gv.NORMAL_FONT)
 
        self.text2 = ui.make_TextEntry(self.group1, 105, gp1y, 35, 20, font=gv.NORMAL_FONT)
        self.text2.insert('end', self.callPar.getObjectGeometry(self.tagName,'y1'))               
        #################################################################
   
    def sizeEntry(self):
        
        gp2y = 5
        self.group2 = LabelFrame(self, text="Size",
                           width=170,
                           height=50,
                           font=gv.NORMAL_FONT,
                           bg=gv.bckGround,
                           fg=gv.forGround)
        self.group2.place(x=15, y=70)
        ################################################################         
        self.label1 = ui.make_label(self.group2, 15, gp2y, 20, 20, text="W:", 
                                    background=gv.bckGround,foreground=gv.forGround,
                                    font=gv.NORMAL_FONT)

        self.text3 = ui.make_TextEntry(self.group2, 35, gp2y, 35, 20, font=gv.NORMAL_FONT)
        self.text3.insert('end', self.callPar.getObjectGeometry(self.tagName,'w'))
        #################################################################
        self.label2 = ui.make_label(self.group2, 85, gp2y, 20, 20, text="H:", 
                                    background=gv.bckGround,foreground=gv.forGround,
                                    font=gv.NORMAL_FONT)
        
        self.text4 = ui.make_TextEntry(self.group2, 105, gp2y, 35, 20, font=gv.NORMAL_FONT)
        self.text4.insert('end', self.callPar.getObjectGeometry(self.tagName,'h'))   
        ################################################################
        
    def buttonsUI(self):   
        self.B1 = ui.make_OpenCloseBtn(self, 15, 150, 75, 25, self.updateWidget, text='Apply', 
                      bg=gv.bckGround, fg='white', font=gv.LARGE_FONT)
        
        self.B2 = ui.make_OpenCloseBtn(self, 110, 150, 75, 25, self.closeWindow, text='Close', 
                      bg=gv.bckGround, fg='white', font=gv.LARGE_FONT)       

    def buttonClrEnter(self, event):
        event.widget.config(bg='white', fg='black')
    
    def buttonClrLeave(self, event):
        event.widget.config(bg=gv.bckGround, fg='white')
        
    def updateWidget(self, event):        
        x = self.text1.get().strip()
        y = self.text2.get().strip()
        w = self.text3.get().strip()
        h = self.text4.get().strip()
        sizeTuple = (int(x),int(y),int(w),int(h))
        self.callPar.setObjectGeometry(sizeTuple, self.tagName)
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

##############################################################################
class GPIOBind(tk.Toplevel):
    
    def __init__(self, parent):

        tk.Toplevel.__init__(self)
        

        self.callPar   = parent.parent
        self.ux        = parent.parent.ux
        
        w = 450
        h = 120 
        geometry = self.ux.get_popup_location(w,h)
        self.geometry(geometry)
        self.pVar = StringVar()
        self.cbVar = IntVar()
        self.tagName = parent.tagName
        self.title("GPIO Assignment")
#         
        self.entrySettings   = gv.entrySettings
        self.frame = Frame(self, background=gv.bckGround) 

        self.frame.pack(fill=BOTH, expand=1)               
       
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















     
        