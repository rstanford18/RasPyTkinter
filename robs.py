# from tkinter import *
# from tkinter import ttk
# import time
# # TOP RIGHT BOTTOM LEFT 
# # FILL DIRECTION - X Y BOTH NONE


# root = Tk()
# class Clock():
#     def __init__(self, parent):
#         self.parent = parent
#         self.ClockFg = "#6E6E6E"
#         self.handleClock()
#         self.updateClock()
        
#     def handleClock(self):
            
#         self.Clock = self.buildClockUI(1600, 50, 200, 75, font=('times', 30, 'bold'), 
#                                                     bg=gv.bckGround, fg=self.ClockFg)
               
#     def buildClockUI(self, x, y, w, h, *args, **kwargs):
#         f = Frame(self.parent, height=h, width=w, highlightbackground=self.ClockFg, 
#                                 highlightcolor=self.ClockFg, highlightthickness=2,)
#         f.pack_propagate(0) # don't shrink
#         f.place(x=x, y=y)
#         lbl = Label(f, *args, **kwargs)
#         lbl.pack(fill=BOTH, expand=1)
#         return lbl 

#     def updateClock(self, previousTime=''):
#         currentTime = time.strftime('%H:%M:%S')
#         if previousTime != currentTime:
#             previousTime = currentTime
#             self.Clock.config(text=currentTime)
        
#         self.Clock.after(200, self.updateClock, previousTime)
        
# clock = Clock(root)

# root.mainloop()
# ---------- TKINTER EVENTS  ----------
 
# def get_sum(event):
 
#     # Get the value stored in the entries
#     num1 = int(num1Entry.get())
#     num2 = int(num2Entry.get())
#     sum = num1 + num2
    
#     # Delete the value in the entry
#     sumEntry.delete(0, "end")
 
#     # Insert the sum into the entry
#     sumEntry.insert(0, sum)
 
# root = Tk()
 
# num1Entry = Entry(root)
# num1Entry.pack(side=LEFT)
 
# Label(root, text="+").pack(side=LEFT)
 
# num2Entry = Entry(root)
# num2Entry.pack(side=LEFT)
 
# equalButton = Button(root, text="=")
 
# # When the left mouse button is clicked call the
# # function get_sum
# equalButton.bind("<Button-1>", get_sum)
 
# equalButton.pack(side=LEFT)
 
# sumEntry = Entry(root)
# sumEntry.pack(side=LEFT)
 
# root.mainloop()



# root = Tk()


# Label(root, text="Description").grid(row=0, column=0, sticky=W)
# Entry(root, width=50).grid(row=0, column=1)
# Button(root, text="Submit").grid(row=0, column=8)

# Label(root, text="Quality").grid(row=1, column=0, sticky=W)
# Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
# Radiobutton(root, text="Good", value=2).grid(row=3, column=0, sticky=W)
# Radiobutton(root, text="Poor", value=3).grid(row=4, column=0, sticky=W)
# Radiobutton(root, text="Damaged", value=4).grid(row=5, column=0, sticky=W)

# Label(root, text="Benefits").grid(row=1, column=1, sticky=W)
# Checkbutton(root, text="Free Shipping").grid(row=2, column=1, sticky=W)
# Checkbutton(root, text="Bonus Gift").grid(row=3, column=1, sticky=W)


# Label(root, text="First Name").grid(row=0, sticky=W, padx=4)
# Entry(root).grid(row=0, column=1, sticky=E, pady=4)

# Label(root, text="Last Name").grid(row=1, sticky=W, padx=4)
# Entry(root).grid(row=1, column=1, sticky=E, pady=4)

# Button(root, text="Submit").grid(row=3)

# root.mainloop()

# from tkinter import Tk, BOTH
# from tkinter.ttk import Frame
# import asyncio
# import time

# class Example(Frame):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.master.title("Simple")
#         self.pack(fill=BOTH, expand=1)

# def main():
#     root = Tk()
#     root.geometry("250x150+300+300")
#     app = Example()
#     startAsync()
#     root.mainloop()

# def startAsync():
#     event_loop = asyncio.get_event_loop()
#     try:
#         print(event_loop.__dict__)
#         event_loop.run(slow_function())

#     finally:
#         event_loop.close()

# async def slow_function():
#     time.sleep(2)
#     print('slow_function_result')

# if __name__ == '__main__':
#         main()

