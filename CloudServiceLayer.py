import urllib.request

from tkinter import Tk, Label, Button

from tkinter import *
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.label = Label(master, fg="dark green")
    self.label.pack()

    def sendRequest():
        response = urllib.request.urlopen("http://192.168.6.58:3000").read()
        printResponse(response)

    self.slogan = Button(frame,
                         text="Send Request",
                         command=sendRequest)
    self.slogan.pack(side=LEFT)

    def printResponse(response):
        self.label.config(text=response)

root = Tk()
app = App(root)
root.mainloop()