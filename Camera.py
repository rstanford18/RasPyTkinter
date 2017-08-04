import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread
import cv2
import GlobalVariables as gv
import GlobalFunctions as gf
frame1 = None

class Camera(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent) 
        self.parent = parent
        self.img = gf.getImageForWidget()
        self.get_init_img()
        self.cam() 
        self.loader()
        
    
    def get_init_img(self):
        try:
            global frame1
            print(frame1)
            img = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            self.img = ImageTk.PhotoImage(img)
        except:
            pass
    
    def cam(self):
        
        
        self.panel = tk.Label(self.parent, image=self.img)
        self.panel.pack(side="bottom", fill="both", expand="yes")
    
     
    def loader(self):
        self.get_init_img()
        self.panel.configure(image=self.img)
        self.panel.image = self.img
        self.panel._backbuffer_ = self.img
        
        self.panel.after(100, self.loader)


###

class CameraStream():
    
    
    def __init__(self, parent=None, cameraName):
        
        self.frame = None
        self.camName = cameraName
        
    
    def han_get_cam_params(self):
        self.camPars = gv.ActiveCameras[self.camName]
        self.userName = self.camPars['user']
    
    def get_stream_data():
        return cv2.VideoCapture('http://72.48.229.3:8887/mjpg/video.mjpg')
    
    def han_get_cam_feed():
        global frame1
        cap = get_stream_data()
        keepAlive = True
        while True:
            if keepAlive == False:
                cap = get_stream_data()
                keepAlive = True
            try:
                ret, frame = cap.read()
                keepAlive = ret
                
                    
                print('ret',ret)
            except:
                print('ret',ret)
        
            frame1 = frame
            
            #cv2.imshow('Video', frame)
            #print(frame1)
            if cv2.waitKey(1) == 27:
                exit(0)
        print('deadThread')

k = Thread(target=han_get_cam_feed)
k.start()  

 
root = tk.Tk() 
pd = Cam(root)   
#root.bind("<Return>", callback)
root.mainloop()



# #             tki = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(i, cv2.COLOR_BGR2RGB)))
# #             image_label.configure(image=tki)
# #             image_label._backbuffer_ = tki



#cap = cv2.VideoCapture('rtsp://admin:steritec@192.168.6.103/Streaming/Channels/1')
