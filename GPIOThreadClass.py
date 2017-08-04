import time
from threading import Thread
import GlobalVariables as gv
import random
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import LED, Button, OutputDevice


class GPIOSimulator():
    
    def __init__(self, parent):
        self.factory = None
        self.parent  = parent
        self.initAlarmHorn()
        self.activeGPIO = self.getActiveGPIO()   
        #t = Thread(target=self.ChangeGPIOStates)
        #t.start() 
        self.start = True
        self.pauseAck = False
        self.initAlarmThread()
        self.TagCanvasLoaded = False
        
    def getActiveGPIO(self):
        tagDict = gv.tagElements
        
        activeGpioDict = {}
        for i in gv.tagElements:
            tagName = i
            gpioEnable = tagDict[tagName].isGPIOBound
            if gpioEnable:
                channelNum = tagDict[tagName].GPIO
                activeGpioDict[channelNum] = tagName
        
        return activeGpioDict
     
    def ChangeGPIOStates(self):
        while True:
            ranList  = range(0,25)
            ranState = [0,1]
            ranGPIO  = random.choice(ranList)
            ranState = random.choice(ranState)
            gv.gpioStateDict[ranGPIO] = ranState
            time.sleep(1)
    
    def destroyButtons(self):
        try:
            for i in self.buttonList:
                i[1].close()
            self.buttonList = []
        except:
            pass
        
    def initAlarmHorn(self):
        self.horn = OutputDevice(2, pin_factory=self.factory)
        
    def GPIOChannelConstructor(self):
     
        self.buttonList = []
        tagDict = gv.tagElements

        for i in self.getActiveGPIO():
            tagName = self.activeGPIO[i]
            self.factory = tagDict[tagName].GPIOParent
            factoryIP = gv.piFactoryXConnect[self.factory]
            button = Button(i, factoryIP)           
            
            self.buttonList.append([tagName, button])
            
    def han_start_tag_scan(self):
        self.start = True 
    
    
    def han_stop_tag_scan(self):
        self.start = False
 
    def han_load_GPIO_btn(self):
             
        try:
            self.destroyButtons()
        except:
            pass
        self.activeGPIO = self.getActiveGPIO()      
        self.GPIOChannelConstructor()
              
    def tagCanvasStart(self, tagCanvas):
        self.TagCanvas = tagCanvas
        self.TagCanvasLoaded = True
        
    def startUXIndicatorStatus(self):
        #self.start = False
        self.destroyButtons()       
        self.k = Thread(target=self.ScanActiveGPIOState)
        #self.start = True
        self.k.start()
    
    def getButtonlist(self):
        return self.buttonList
    
    def get_start_value(self):
        return self.start
    
    def ScanActiveGPIOState(self):
        self.GPIOChannelConstructor()
        self.activeSensors = []
        
        while True:
            if self.get_start_value():
                for i in self.getButtonlist(): 
                    try:
                        if self.get_start_value() == False:
                            self.pauseAck = True

                        tagName = i[0]
                        button  = i[1]
                    
                        if button.is_active:
                            state = 1
                            if button.pin not in self.activeSensors:
                                self.activeSensors.append(button.pin)
                            
                        if not button.is_active:
                            state = 0
                            if len(self.activeSensors) > 0:
                                if button.pin in self.activeSensors:
                                    if not self.getAlarmState():
                                        print(tagName,button)
                                        idx = self.activeSensors.index(button.pin)
                                        self.activeSensors.pop(idx)
                    except:
                        print('Reset Event in Scan Loop')    
                                         
                    if self.TagCanvasLoaded:
                        color = 'green' if state == 0 else 'red'
                        self.TagCanvas.onRemoteSelect(tagName, color)
                        
                time.sleep(.005)
            else:
                print('Scan Loop Buffer')
                time.sleep(1)
            
    
    def initAlarmThread(self):
        self.AlarmThread = Thread(target=self.AlarmState)
        self.AlarmThread.start()
      
    def getAlarmState(self):
        return gv.AlarmArmed
    
    def AlarmState(self):
       
        self.isCDCActive = False
        while True: 
            # print('Alarm State Loop', self.getAlarmState())
            if self.getAlarmState():
                if len(self.activeSensors) > 0:
                    self.horn.on()
                    if not self.isCDCActive:
                        self.ActivateCDC()
                        self.isCDCActive = True
                time.sleep(.25)      
            else:
                if self.horn.is_active:             
                    self.horn.off()
                    # print('Alarm Horn Off')
                    self.isCDCActive = False
                    try:
                        self.DeActivateCDC()
                    except:
                        pass
                time.sleep(.25)    
                
        
    def ActivateCDC(self):
        self.parent.nvm.currentFrame.callCDC()
    
    def DeActivateCDCr(self):
        self.parent.nvm.currentFrame.destroyCDC()
        
        
        
        
        
        
          
        
        
        
        
        
        
        
        
        
        
        
                         
 ###############################################################################  
        

 