# # use Tkinter to show a digital clock
# # tested with Python24    vegaseat    10sep2006
# from tkinter import *
# import time
# root = Tk()
# time1 = ''
# clock = Label(root, font=('times', 20, 'bold'), bg='green')
# clock.pack(fill=BOTH, expand=1)
# def tick():
#     global time1
#     # get the current local time from the PC
#     time2 = time.strftime('%H:%M:%S')
#     # if time string has changed, update it
#     if time2 != time1:
#         time1 = time2
#         clock.config(text=time2)
#     # calls itself every 200 milliseconds
#     # to update the time display as needed
#     # could use >200 ms, but display gets jerky
#     clock.after(200, tick)
# tick()
# root.mainloop(  )







'''
import GlobalVariables as gv
 
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import LED, Button, InputDevice, OutputDevice
from time import sleep
import winsound
 
factory3 = PiGPIOFactory(host='10.0.0.21')
led_1 = OutputDevice(2, pin_factory=factory3)
led_2 = LED(20, pin_factory=factory3)
led_3 = LED(16, pin_factory=factory3)
led_4 = LED(12, pin_factory=factory3)
  
  btn1 = Button(26, factory3)
  btn1 = Button(19, factory3)
  btn1 = Button(13, factory3)
  btn1 = Button(6, factory3)
  
  sleepTime = .25
  
  def btn_release():
      global sleepTime
      sleepTime = .25 
  
import random
def getRandomFreq():
     
    return random.choice(range(130,8000))

def getRandomTime():
     
    return float('.'+str(random.choice(range(1,100))))
  
   
while True:
     led_1.on()
     sleep(getRandomTime())
    led_1.off()
    winsound.Beep(getRandomFreq(),250)
      
      led_1.off()
     led_2.on()
     winsound.Beep(getRandomFreq(),250)
     sleep(.005)
     led_2.off()
     led_3.on()
     winsound.Beep(getRandomFreq(),250)
     sleep(.005)
     led_3.off()
     led_4.on()
     winsound.Beep(getRandomFreq(),250)
     sleep(.005)
     led_4.off()
      
 
     sleep(1)
 
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
      
  def buttonPressed(value):
      print('Scored! %s'%value)
      
  GPIO.add_event_detect(17, GPIO.FALLING, callback=lambda x: buttonPressed(50), bouncetime=2000)
  GPIO.add_event_detect(27, GPIO.FALLING, callback=lambda x: buttonPressed(150), bouncetime=2000)
 
 def say_hello( *args, **kwargs):
     print("Hello!")
     print(args, kwargs)
     winsound.Beep(329,0)
   
 def say_goodbye():
     print("Goodbye!")
      winsound.Beep(261,250)
       
 button = Button(26, factory3)
 
 button.
 l = [button]
 button = Button(19, factory3)
 l.append(button)
 button = Button(13, factory3)
 l.append(button)
 button = Button(6, factory3)
 l.append(button)
 print(len(l))
 print(button26.__dict__)
 l = [button26,button19,button13,button6]
 
 
 while True:
     for i in l: 
         if i.is_active:
             print(i.pin, '**************************active************************')
         if not i.is_active:
             print(i.pin, 'inacitve')
     sleep(.3)
      
     
     
     
      button26.when_pressed = say_hello
      button26.when_released = say_goodbye
      
      button.when_pressed = say_hello
      button.when_released = say_goodbye    
      
      button.when_pressed = say_hello
      button.when_released = say_goodbye    
      
      button.when_pressed = say_hello
      button.when_released = say_goodbye
 
 import time
 
 time1 = time.localtime()
 print(type(time1))
'''


     
