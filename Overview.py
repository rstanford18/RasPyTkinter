import tkinter as tk
import TagPallete as tp
import GlobalVariables as gv
import GlobalFunctions as gf
import UIWidgets as ui
import UITreeview as uitv
from ClockThread import Clock as ck
from MenuBar import MainMenuBar as mb

class OverviewPage(tk.Frame):
    
    def __init__(self, parent, nav):
        tk.Frame.__init__(self, parent, bg=gv.bckGround)   

        self.parent     = parent       
        self.nav       = nav
        self.mb         = mb(self)
        self.menu       = nav.parent.config(menu=self.mb.getMenu()) 
        self.ux         = self.nav.ux
        self.ux.han_change_title('Launch Pad')
        self.objDataMgr = self.nav.launch.ObjDataMgr       
      
        self.han_init_sequence()

    def han_init_sequence(self):
        self.han_init_banner()
        self.han_init_buttons()
        self.han_init_tagpallet()
        self.han_init_canvas()
        self.han_init_treeview()
        self.han_init_clock()
        self.han_init_data_mgr_link()
        self.han_init_thread_link()
        
    def han_init_clock(self):   
        self.Clock = ck(self)
     
    def han_init_banner(self):
        x = self.ux.getHorizontalCenter(500)
        
        ui.make_label(self, x, 50, 500, 60, text='Sensor Overview', 
                      bg=gv.bckGround, fg=gv.forGround, font=gv.SUPER_FONT)
             
    def han_init_buttons(self):
             
        self.B1 = ui.make_button(self, 15, 175, 120, 30, self.han_print_canvas_data, text='Edit Mode', 
                      bg=gv.bckGround, fg='#00FF00', font=gv.LARGE_FONT)
        
        self.B2 = ui.make_button(self, 15, 220, 120, 30, self.han_btn_add_cmd, text='Add Tag', 
                      bg=gv.bckGround, fg='#00FF00', font=gv.LARGE_FONT)
        
        self.B3 = ui.make_button(self, 15, 265, 120, 30, self.han_btn_save_cmd, text='Save', 
                      bg=gv.bckGround, fg='#00FF00', font=gv.LARGE_FONT)
        
    
    def han_btn_add_cmd(self, event):
        self.han_task_route('add')
    
    def han_btn_save_cmd(self, event):
        self.han_task_route('save')
    
    
    def han_init_data_mgr_link(self):
        self.objDataMgr.han_tagcanvas_data(self.TagCvs)
        self.objDataMgr.han_treeview_data(self.TreeView)
        self.objDataMgr.han_obj_data_init()
            
    def buttonClrEnter(self, event):
        event.widget.config(bg='#7DE87E', fg='black')
    
    def buttonClrLeave(self, event):
        event.widget.config(bg=gv.bckGround, fg='#00FF00')
   
    def han_print_canvas_data(self, event):
        for i in self.canvas.find_all():
            if len(self.canvas.gettags(i))==0:
                navinue         
            tagName =  self.canvas.gettags(i)[1]
            print(self.canvas.gettags(i))
            x1, y1, x2, y2 = self.canvas.coords(tagName)
            w = x2-x1
            h = y2-y1
            print(tagName,w,h,x1,y1,x2,y2)
                    
    def han_task_route(self, instruction):   

        self.objDataMgr.han_data_harmony(instruction)

        
    def han_obj_hover_alert(self, tagName): 
        self.TreeView.highLightSelection(None, tagName)
    
    def han_init_canvas(self):
        x = self.ux.getHorizontalCenter(self.w)
        y = self.ux.getVerticalCenter(self.h) 
        self.canvas = self.TagCvs.canvas
        self.canvas.place(x=x, y=y)
            
    def han_init_tagpallet(self):  
        
        self.photo = gf.getImageForWidget()
        self.w = self.photo.width()
        self.h = self.photo.height()     
        self.TagCvs = tp.TagCanvas(self, self.w, self.h)     

    def han_init_thread_link(self):      
        if self.nav.launch.isGPIOOn:
            self.nav.launch.scan.tagCanvasStart(self.TagCvs)
    
    
    def han_init_treeview(self):
        sizeTuple = (15, 300, 120, 400)
        self.TreeView = uitv.TagManagerView(self, sizeTuple)
    
    
    