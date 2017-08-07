from tkinter import BOTH, Frame, LabelFrame, Label, Text, Checkbutton, IntVar, StringVar, Button, NORMAL, DISABLED, Widget, Entry, ttk
import tkinter as tk
import GlobalVariables as gv
import GlobalFunctions as gf
import UIWidgets as ui
import Config as cf
from ClockThread import Clock as ck
from MenuBar import MainMenuBar as mb
from PopupMenus import AdminCameraCfgPopup as accp

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
        self.optionVar   = StringVar()        
        self.entrySettings   = gv.entrySettings

        
        self.han_init_ooe()

#         style = ttk.Style()
#         style.theme_use('clam')
#         style.configure('Treeview', background='black', 
#                 fieldbackground='black', foreground='white')
    def han_init_ooe(self):
        self.han_init_main_frame()
        self.han_init_object_geometry()
        
        self.han_init_treeview_widget()
        self.han_bind_tree()
        self.han_load_active_camera_db()
        self.han_init_label_frame_widget()
        self.han_init_label_widgets()
        self.han_init_btn_widgets()
        self.han_init_text_entry_widgets()
        self.han_init_option_menu_widgets()
       
    def han_init_main_frame(self):
        self.mainWidgetSize = 1100
        self.centerX     = self.ux.getHorizontalCenter(self.mainWidgetSize)
        self.frame = tk.Frame(self, height=350, width=self.mainWidgetSize, 
                              highlightbackground='white',
                               highlightcolor='white', highlightthickness=1,)
        self.frame.pack_propagate(0) # don't shrink
        self.frame.place(x=self.centerX , y=400)

    def han_init_object_geometry(self):
        startx = 15
        spacer = 15
        self.sizeList = [150,240,50,325,50,80,80]
        self.itemOrder = gv.camElementStructure
        
        l = []
        
        for i in range(len(self.sizeList)):
            if i == 0:
                l.append(startx)
            else:
                l.append(spacer+self.sizeList[i-1]+l[i-1])
                
        self.objXlist = l
           
    def han_init_treeview_widget(self):
        self.tree = ttk.Treeview(self.frame, columns=tuple(self.itemOrder))

        self.tree.heading('#0', text='idx')
        self.tree.column('#0', minwidth=0, width=0, stretch=False)        
        
        for i in range(len(self.itemOrder)):
            
            self.tree.heading('#'+str(i+1), text=self.itemOrder[i])
            self.tree.column('#'+str(i+1), minwidth=50, width=self.sizeList[i], stretch=True)
     

        self.tree.pack(fill=tk.BOTH, expand=1)
        self.treeview = self.tree

    def han_init_label_frame_widget(self):
    
        self.group0 = LabelFrame(self ,text="Add/Edit Cameras",
                           width=self.mainWidgetSize,
                           height=120,
                           font=gv.NORMAL_FONT,
                           bg=gv.bckGround,
                           fg=gv.forGround)
        self.group0.place(x=self.centerX, y=250) 
       
    def han_init_label_widgets(self):
        
        self.labelY = 20
        self.labelList = []
        for i in range(len(self.itemOrder)):
        
            self.lbl = ui.make_label(self.group0, self.objXlist[i], self.labelY, 
                                     self.sizeList[i], 20, text=self.itemOrder[i], 
                                    background=gv.bckGround,foreground=gv.forGround,
                                    font=gv.NORMAL_FONT, anchor="w")
            
            self.labelList.append(self.lbl)
  
    def han_init_text_entry_widgets(self):
        
        self.textEntryY = 50
        self.textEntryX = 150
        self.txtList = []
        for i in range(len(self.itemOrder)-1):
            self.txt = ui.make_TextEntry(self.group0, self.objXlist[i], 
                                         self.textEntryY , self.sizeList[i], 20, 
                                         font=gv.NORMAL_FONT)
        
            self.txtList.append(self.txt)
             
    def han_init_option_menu_widgets(self):
        
        choices = [['True'],['False']]
        self.optionVar.set(choices[0][0])
        
        f1 = Frame(self.group0, height=20, width=self.sizeList[6], background=gv.bckGround)
        f1.pack_propagate(0)
        f1.place(x=self.objXlist[6], y=self.textEntryY)
        self.dropDown0 = tk.OptionMenu(f1, self.optionVar, *choices, command=self.selValue1)
        self.dropDown0.configure(highlightthickness=0,highlightbackground="Black" ,highlightcolor="Black")
        self.dropDown0.pack(fill=BOTH, expand=1)       

    def han_init_btn_widgets(self):   
        self.B1 = ui.make_OpenCloseBtn(self, 1525, 260, 75, 25, self.han_add_update_route, text='Add', 
                      bg=gv.bckGround, fg='white', font=gv.LARGE_FONT)
        
        self.B2 = ui.make_OpenCloseBtn(self, 1525, 300, 75, 25, 
                                       self.han_clear_entry_widgets, text='Clear', 
                      bg=gv.bckGround, fg='white', font=gv.LARGE_FONT)
              
        self.B3 = ui.make_OpenCloseBtn(self, 1525, 400, 75, 25, 
                                       self.han_load_edit_values, text='Edit', 
                      bg=gv.bckGround, fg='white', font=gv.LARGE_FONT)        
        
        self.B4 = ui.make_OpenCloseBtn(self, 1525, 440, 75, 25, 
                                       self.han_delete_camera_in_db, text='Delete', 
                      bg=gv.bckGround, fg='white', font=gv.LARGE_FONT)       
        
        self.B5 = ui.make_OpenCloseBtn(self, 1525, 750, 75, 25, 
                                       self.han_save_changes_to_db, text='Save', 
                      bg=gv.bckGround, fg='white', font=gv.LARGE_FONT)
        
        
    def han_init_popup(self, event):
        try:
            self.accp = accp(self)              
            self.accp.popup(event)
        except:
            pass        

    def han_bind_tree(self):
        self.tree.bind('<Button-2>', self.highLightSelection)
        self.tree.bind('<Button-3>', self.highLightSelection)
        self.tree.bind('<ButtonRelease-2>', self.han_init_popup)
        self.tree.bind('<ButtonRelease-3>', self.han_init_popup)
                    
    def han_load_active_camera_db(self):
        
        self.activeCameras = gv.camElements
        
        for i in self.activeCameras:
            camName = i
            camDict = self.activeCameras[i]
            
            self.treeview.insert('', 'end', text='', 
                 value=tuple([camDict[i] for i in self.itemOrder]))
  
    def han_load_text_entry_widgets(self):
        for i in range(len(self.txtList)):
            self.txtList[i].delete(0,'end')
            self.txtList[i].insert('end',self.selRow[i])
    
    def han_load_edit_values(self, event=None):
        self.selIdx  = self.tree.focus()
        self.selRow  = self.get_selected_item()
        self.camName = self.selRow[0]
        self.han_load_text_entry_widgets()
        self.han_load_option_widget()
        self.B1.config(text='Update')
        
    def han_load_option_widget(self):
        self.optionVar.set(str(self.selRow[-1]))
       
    def han_popup_action_route(self, action):
        if action == 'edit':
            self.han_load_edit_values()
        if action == 'delete':
            self.han_delete_camera_in_db()
            
    def han_clear_entry_widgets(self, event=None):       
        for i in range(len(self.txtList)):
            self.txtList[i].delete(0,'end')
        
        self.B1.config(text='Add')
    
    def han_add_update_route(self, event=None):
        self.cName = self.B1.cget('text')
        if self.cName == 'Add':
            self.han_add_camera_to_db()
        if self.cName == 'Update':
            self.han_update_camera_in_db()
            
    def han_add_camera_to_db(self):
        self.get_entry_values()

        if self.newRow[0] not in list(gv.camElements.keys()):
            gv.camElements[self.newRow[0]] = {self.itemOrder[0]:self.newRow[0],
                                                self.itemOrder[1]:self.newRow[1],
                                                self.itemOrder[2]:self.newRow[2],
                                                self.itemOrder[3]:self.newRow[3],
                                                self.itemOrder[4]:self.newRow[4],
                                                self.itemOrder[5]:self.newRow[5],
                                                self.itemOrder[6]:self.newRow[6]}
            
            self.han_clear_entry_widgets()
            for item in self.treeview.get_children():
                self.treeview.delete(item)
            self.han_load_active_camera_db()   
        else:
            print('Duplicate Camera Exists') 
        
    
    def han_update_camera_in_db(self):
        gv.camElements.pop(self.camName)
        self.han_add_camera_to_db()
        
    def han_delete_camera_in_db(self, event=None):
        self.selIdx  = self.tree.focus()
        self.camName = self.treeview.item(self.selIdx)['values'][0]
        gv.camElements.pop(self.camName)
        
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        
        self.han_load_active_camera_db()
        self.han_clear_entry_widgets()
    
    def han_save_changes_to_db(self, event=None):
        cf.saveCamFile()
               
    def get_entry_values(self):
        l = []
        for i in range(len(self.txtList)):
            try:
                l.append(self.txtList[i].get().strip())
                
            except:
                l.append('')
        try:
            optVal = False if 'F' in self.optionVar.get() else True
            l.append(optVal)
        except:
            l.append(True)      
        self.newRow = l   

    def get_selected_item(self):
         
        for child in self.treeview.get_children():
            if child == self.selIdx:
                return self.treeview.item(child)['values']
         
    def highLightSelection(self, event=None):
        
        self.selIdx  = self.tree.identify_row(event.y)
        self.tree.selection_set(self.selIdx)
        self.han_init_popup(event)
                                         
    def selValue1(self, value):
        self.value1 = value
  
    def buttonClrEnter(self, event):
        event.widget.config(bg='white', fg='black')
    
    def buttonClrLeave(self, event):
        event.widget.config(bg=gv.bckGround, fg='white')
       
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
        


        