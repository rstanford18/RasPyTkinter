import CfgEnviroment as envir
envir.defineEnviroment()

import GlobalVariables as gv
 
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import LED, Button, InputDevice, OutputDevice, MCP3008
from time import sleep
import winsound
import random

def getRandomFreq():
     
    return random.choice(range(130,8000))

def getRandomTime():
     
    return float('.'+str(random.choice(range(1,100))))

while True:
    pot = MCP3008(0)
    print(pot.value)



# 
# factory3 = PiGPIOFactory(host='10.0.0.21')
# led_1 = OutputDevice(2, pin_factory=factory3)
# led_2 = LED(20, pin_factory=factory3)
# led_3 = LED(16, pin_factory=factory3)
# led_4 = LED(12, pin_factory=factory3)
#   
# btn1 = Button(26, factory3)
# btn1 = Button(19, factory3)
# btn1 = Button(13, factory3)
# btn1 = Button(6, factory3)
#   
#   
# while True:
#     led_1.on()
#     sleep(getRandomTime())
#     led_1.off()
#     winsound.Beep(getRandomFreq(),250)
#     
#     led_1.off()
#     led_2.on()
#     winsound.Beep(getRandomFreq(),250)
#     sleep(.005)
#     led_2.off()
#     led_3.on()
#     winsound.Beep(getRandomFreq(),250)
#     sleep(.005)
#     led_3.off()
#     led_4.on()
#     winsound.Beep(getRandomFreq(),250)
#     sleep(.005)
#     led_4.off()  