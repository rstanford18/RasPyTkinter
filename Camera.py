from cv2 import opencv_ffmpeg320_64 as cv2
import urllib 
import numpy as np
import tkinter
from PIL import Image, ImageTk
import threading
import requests


root = tkinter.Tk()
image_label = tkinter.Label(root)  
image_label.pack()

def cvloop():    
    stream=open('output.mjpg','rb')
    bytes=''
    while True:
        bytes+=stream.read(1024)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')
        if a!=-1 and b!=-1:
            jpg = bytes[a:b+2]
            bytes= bytes[b+2:]
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)            
            tki = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(i, cv2.COLOR_BGR2RGB)))
            image_label.configure(image=tki)                
            image_label._backbuffer_ = tki  #avoid flicker caused by premature gc
            cv2.imshow('i',i)
        if cv2.waitKey(1) ==27:
            exit(0)  

thread = threading.Thread(target=cvloop)
thread.start()
root.mainloop()


# r = requests.get('http://192.168.1.xx/mjpeg.cgi', auth=('user', 'password'), stream=True)
# if(r.status_code == 200):
#     bytes = bytes()
#     for chunk in r.iter_navent(chunk_size=1024):
#         bytes += chunk
#         a = bytes.find(b'\xff\xd8')
#         b = bytes.find(b'\xff\xd9')
#         if a != -1 and b != -1:
#             jpg = bytes[a:b+2]
#             bytes = bytes[b+2:]
#             i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
#             cv2.imshow('i', i)
#             if cv2.waitKey(1) == 27:
#                 exit(0)
# else:
#     print("Received unexpected status code {}".format(r.status_code))