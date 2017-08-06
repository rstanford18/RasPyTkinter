from tkinter import BOTH, Frame, LabelFrame, Label, Text, Checkbutton, IntVar, StringVar, Button, NORMAL, DISABLED, Widget, Entry, ttk
import tkinter as tk
import GlobalVariables as gv
import GlobalFunctions as gf
import UIWidgets as ui

from ClockThread import Clock as ck
from MenuBar import MainMenuBar as mb


class AdminCameraCfg(tk.Frame):
    
    def __init__(self, parent, nav):

        tk.Frame.__init__(self, parent, bg=gv.bckGround)
        self.parent      = parent
        self.nav         = nav
        self.ux          = self.nav.ux
        self.ux.han_change_title('Admin - Camera Config')
        self.mb          = mb(self)
        self.menu        = nav.parent.config(menu=self.mb.getMenu()) 
        self.pVar        = StringVar()
        self.cbVar       = IntVar()        
        self.entrySettings   = gv.entrySettings
        self.centerX     = self.ux.getHorizontalCenter(1100)
        self.frame = tk.Frame(self, height=350, width=1100, 
                              highlightbackground='white',
                               highlightcolor='white', highlightthickness=1,)
        self.frame.pack_propagate(0) # don't shrink
        self.frame.place(x=self.centerX , y=400)
        
        self.han_init_ooe()
        self.prevSelection = None
#         style = ttk.Style()
#         style.theme_use('clam')
#         style.configure('Treeview', background='black', 
#                 fieldbackground='black', foreground='white')
    def han_init_ooe(self):
        self.han_init_treeview()
        self.han_bind_tree()
        self.han_load_active_camera_db()
        self.han_init_entry_widgets()
        self.han_init_btn_widgets()
        
    def han_init_treeview(self):
        self.tree = ttk.Treeview(self.frame, columns=('Camera Name','URL','Port',
                                                      'Path','User',"Password",'Enabled'))
        print('init')
        self.tree.heading('#0', text='idx')
        self.tree.column('#0', minwidth=0, width=0, stretch=True)        
        
        self.tree.heading('#1', text='Camera Name')
        self.tree.column('#1', minwidth=80, width=150, stretch=True)
       
        self.tree.heading('#2', text='Url')
        self.tree.column('#2', minwidth=80, width=275, stretch=True)
        
        self.tree.heading('#3', text='Port')
        self.tree.column('#3', minwidth=30, width=50, stretch=True)
        
        self.tree.heading('#4', text='Path')
        self.tree.column('#4', minwidth=80, width=350, stretch=True)
        
        self.tree.heading('#5', text='User')
        self.tree.column('#5', minwidth=50, width=50, stretch=True)
        
        self.tree.heading('#6', text='Password')
        self.tree.column('#6', minwidth=50, width=80, stretch=True)
        
        self.tree.heading('#7', text='Enabled')
        self.tree.column('#7', minwidth=50, width=100, stretch=True)        
          

        self.tree.pack(fill=tk.BOTH, expand=1)
        self.treeview = self.tree

    def han_bind_tree(self):
        self.tree.bind('<Button-1>', self.highLightSelection)
#         self.tree.bind('<Button-2>', self.highLightSelection)
#         self.tree.bind('<Button-3>', self.highLightSelection)
# 
#         self.tree.bind('<ButtonRelease-2>', self.han_init_popup)
#         self.tree.bind('<ButtonRelease-3>', self.han_init_popup)
    
    def han_item_add(self):
        
        self.treeview.insert('', 'end', text='idx', 
                             value=('http://72.48.229.3','8887','/mjpg/video.mjpg','testuser','testpass','True'))
      
    def han_load_active_camera_db(self):
        
        self.activeCameras = gv.ActiveCameras
        
        for i in self.activeCameras:
            camName = i
            camDict = self.activeCameras[i]
            
            self.treeview.insert('', 'end', text='', 
                 value=(camName, camDict.get('url'),camDict.get('port',''),
                        camDict.get('path'),camDict.get('user', ''),
                        camDict.get('passsword', ''),str(camDict.get('enabled'))))
  
    def han_init_popup(self, event):
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
            selIdx = self.get_selected_item()
        
        self.tree.selection_set(selIdx)     
                  
    def getCurrentTagName(self, event):
        self.selection = self.tree.set(self.tree.identify_row(event.y))
        print('getCurrentTagName',self.selection)
        tagName = self.selection['Tag']
        return tagName
                
    def get_selected_item(self):
         
        for child in self.treeview.get_children():
            tagNameValue = self.treeview.item(child)['values'][0]
            print(self.treeview.item(child)['values'])
           
       
        self.popupWindowUI()

    def popupWindowUI(self):
        self.positionEntry()
        self.buttonsUI()       
    
    def han_init_entry_widgets(self):
        
        gp1y = 20
        self.group1 = LabelFrame(self ,text="Add/Edit Cameras",
                           width=1100,
                           height=120,
                           font=gv.NORMAL_FONT,
                           bg=gv.bckGround,
                           fg=gv.forGround)
        self.group1.place(x=self.centerX, y=250)       
        #################################################################
        m =150   
        self.label1 = ui.make_label(self.group1, 25, gp1y, 90, 20, text='Camera Name', 
                                    background=gv.bckGround,foreground=gv.forGround,
                                    font=gv.NORMAL_FONT)
        self.label2 = ui.make_label(self.group1, 25+(m*1), gp1y, 90, 20, text='Url', 
                                    background=gv.bckGround,foreground=gv.forGround,
                                    font=gv.NORMAL_FONT)
        self.label3 = ui.make_label(self.group1, 25+(m*2), gp1y, 90, 20, text='Port', 
                                    background=gv.bckGround,foreground=gv.forGround,
                                    font=gv.NORMAL_FONT)
        self.label4 = ui.make_label(self.group1, 25+(m*3), gp1y, 90, 20, text='Path', 
                                    background=gv.bckGround,foreground=gv.forGround,
                                    font=gv.NORMAL_FONT)
        self.label5 = ui.make_label(self.group1, 25+(m*4), gp1y, 90, 20, text='User', 
                                    background=gv.bckGround,foreground=gv.forGround,
                                    font=gv.NORMAL_FONT)
        
        self.label6 = ui.make_label(self.group1, 25+(m*5), gp1y, 90, 20, text='Password', 
                                    background=gv.bckGround,foreground=gv.forGround,
                                    font=gv.NORMAL_FONT)
        self.label7 = ui.make_label(self.group1, 25+(m*6), gp1y, 90, 20, text='Enabled', 
                                    background=gv.bckGround,foreground=gv.forGround,
                                    font=gv.NORMAL_FONT)

        self.tkvar = StringVar()
        choices = [1,2,3,]

        self.tkvar.set(1) 
        #self.parent.iconbitmap(default="gear16.ico")
        
        f1 = Frame(self.group1, height=20, width=60, background=gv.bckGround)
        f1.pack_propagate(0)
        f1.place(x=330, y=50)
        self.dropDown1 = tk.OptionMenu(f1, self.tkvar, *choices, command=self.selValue1)
        self.dropDown1.configure(highlightthickness=0,highlightbackground="Black" ,highlightcolor="Black")
        self.dropDown1.pack(fill=BOTH, expand=1)       
    
        self.tkvar1 = StringVar()
        piChoices = [1,2,3,4,5]

        self.tkvar1.set(piChoices) 
        
        f2 = Frame(self.group1, height=20, width=110, background=gv.bckGround)
        f2.pack_propagate(0)
        f2.place(x=125, y=50)
        self.dropDown2 = tk.OptionMenu(f2, self.tkvar1, *piChoices, command=self.selValue2)
        self.dropDown2.configure(highlightthickness=0,highlightbackground="Black" ,highlightcolor="Black")
        self.dropDown2.pack(fill=BOTH, expand=1)    
    def han_init_text_entry_widgets(self):
        
        self.text4 = ui.make_TextEntry(self.group2, 105, gp2y, 35, 20, font=gv.NORMAL_FONT)
        self.text4.insert('end', '') 
        
        
        
    
    def selValue1(self, value):
        self.value1 = value

    def selValue2(self, value):
        self.value2 = value

        
    def han_init_btn_widgets(self):   
        self.B1 = ui.make_OpenCloseBtn(self, 1525, 400, 75, 25, self.han_tag_bind, text='Add', 
                      bg=gv.bckGround, fg='white', font=gv.LARGE_FONT)
        
        self.B3 = ui.make_OpenCloseBtn(self, 1525, 445, 75, 25, self.han_tag_bind, text='Delete', 
                      bg=gv.bckGround, fg='white', font=gv.LARGE_FONT)       

    def buttonClrEnter(self, event):
        event.widget.config(bg='white', fg='black')
    
    def buttonClrLeave(self, event):
        event.widget.config(bg=gv.bckGround, fg='white')
        
    def han_tag_bind(self, event):
        print(self.tkvar1.get())
        print(self.tkvar.get())
        #self.callPar.parent.nav.launch.ObjDataMgr.han_item_GPIO_bind(self.tagName, self.tkvar1.get(), self.tkvar.get(), True)     
        self.closeWindow(event)
    
    def han_tag_unbind(self, event):
        #self.callPar.parent.nav.launch.ObjDataMgr.han_item_GPIO_bind(self.tagName, '', 0, False)     
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
        


        