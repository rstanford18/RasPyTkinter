from tkinter import Menu
import GlobalVariables as gv

class MainMenuBar(Menu):
    
    def __init__(self, parent):
        
        self.parent = parent
        self.nav   = self.parent.nav
        
        self.buildMenuUI()
         
              
    def buildMenuUI(self):
        
        self.menubar = Menu(self.parent)
        self.menubar.config(bg=gv.bckGround)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Launch Pad", command=self.nav.show_launch_pad)
        filemenu.add_separator()
        
        filemenu.add_command(label="Logout", command=self.callLoginPage)
        filemenu.add_command(label="Exit", command=self.parent.parent.master.destroy)
        self.menubar.add_cascade(label="File", menu=filemenu)
    
    def callLoginPage(self):
        self.menubar.delete(0,'end')
        self.nav.show_login_page()  
    
    def getMenu(self):
        return self.menubar   