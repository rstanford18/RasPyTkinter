from tkinter import Frame,Label,BOTH,Text
import GlobalVariables as gv
import GlobalFunctions as gf

class LaunchPadBtn():
    def __init__(self, parent, name, value, x, y):
        
        self.value    = value
        self.parent   = parent
        self.keyName  = name
        self.B1       = make_LaunchPadButtons(parent, self, x, y, 220,220, 
                                    self.handleBtnFuncRoute, text=name, 
                                    fg='#B1B8FF', bg=gv.bckGround, 
                                    font=gv.LARGE_FONT)
      
    def handleBtnFuncRoute(self, event):
               
        if self.value == 1:
            self.parent.nav.showOverviewPage()
        
        if self.value == 2:
            self.parent.nav.showClimatePage()
        
        if self.value == 3:
            self.parent.nav.showCameraPage()   
                  
    def buttonClrEnter(self, event):
        event.widget.config(bg='#B1B8FF', fg='black')
    
    def buttonClrLeave(self, event):
        event.widget.config(bg=gv.bckGround, fg='#B1B8FF')



class keyBtn():
    def __init__(self, parent, name, value, x, y):
        
        self.value    = value
        self.parent   = parent
        self.keyName  = name
        self.B1       = make_keyPad(parent, self, x, y, 75, 75, 
                                    self.handleBtnFuncRoute, text=name, 
                                    fg='orange', bg=gv.bckGround, 
                                    font=gv.LARGE_FONT)

        self.cle      = "\21"
        self.enterKey = "\u2386"

        
    def handleBtnFuncRoute(self, event):
        
        inst = self.parent.keyPadtxt
        
        if self.value == self.cle:
            gf.undoTextVar(inst)
            gf.undoTextVar(self.parent.keyPadHide)
            self.parent.keyPadErrorField.set('')
        
        elif self.value == self.enterKey:
            isValid = gf.isPasswordValid(inst.get())
            if not isValid:
                self.parent.keyPadErrorField.set('Password is invalid.')
                inst.set('')
            else:
                self.parent.nav.showLaunchPad()
        else:    
            gf.updateTextVar(inst, str(self.value))
            gf.updateTextVar(self.parent.keyPadHide, '*')
            
    def buttonClrEnter(self, event):
        event.widget.config(bg='orange', fg='black')
    
    def buttonClrLeave(self, event):
        event.widget.config(bg=gv.bckGround, fg='orange')
        
               
def make_label(master, x, y, w, h, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)
    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)
    return label

def make_button(master, x, y, w, h, action, *args, **kwargs):
    f = Frame(master, height=h, width=w, highlightbackground="#00FF00", highlightcolor="#00FF00", highlightthickness=1,)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)
    button = Label(f, *args, **kwargs)
    button.bind('<ButtonPress-1>', action)
    button.bind('<Any-Enter>', master.buttonClrEnter)
    button.bind('<Any-Leave>', master.buttonClrLeave)
    button.pack(fill=BOTH, expand=1)
    return button

def make_LaunchPadButtons(master, parent, x, y, w, h, action, *args, **kwargs):

    f = Frame(master, height=h, width=w, highlightbackground='#B1B8FF', highlightcolor='#B1B8FF', highlightthickness=1,)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)
    button = Label(f, *args, **kwargs)
    button.bind('<ButtonPress-1>', action)
    button.bind('<Any-Enter>', parent.buttonClrEnter)
    button.bind('<Any-Leave>', parent.buttonClrLeave)
    button.pack(fill=BOTH, expand=1)
    return button

def make_keyPad(master, parent, x, y, w, h, action, *args, **kwargs):

    f = Frame(master, height=h, width=w, highlightbackground="orange", highlightcolor="orange", highlightthickness=1,)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)
    button = Label(f, *args, **kwargs)
    button.bind('<ButtonPress-1>', action)
    button.bind('<Any-Enter>', parent.buttonClrEnter)
    button.bind('<Any-Leave>', parent.buttonClrLeave)
    button.pack(fill=BOTH, expand=1)
    return button

def make_keyPadEntry(master, x, y, w, h, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)
    button = Label(f, *args, **kwargs)
    button.pack(fill=BOTH, expand=1)
    return button

def make_OpenCloseBtn(master, x, y, w, h, action, *args, **kwargs):
    f = Frame(master, height=h, width=w, highlightbackground="white", highlightcolor="white", highlightthickness=1,)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)
    button = Label(f, *args, **kwargs)
    button.bind('<ButtonPress-1>', action)
    button.bind('<Any-Enter>', master.buttonClrEnter)
    button.bind('<Any-Leave>', master.buttonClrLeave)
    button.pack(fill=BOTH, expand=1)
    return button

def make_TextEntry(master, x, y, w, h, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)
    tb = Text(f, *args, **kwargs)
    tb.bind('<Tab>',master.master.master.OnTextTab)
    tb.pack(fill=BOTH, expand=1)
    return tb


        