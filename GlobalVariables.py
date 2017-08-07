tagToGpioXConnect = {}


tagElements = {}
tagElementStructure = {
                       'x1':0,
                       'y1':0,
                       'x2':0,
                       'y2':0,
                        'w':0,
                        'h':0,
                     'GPIO':0,           
              'isGPIOBound':None,
               'GPIOParent':None,
              'Description':None
                        }

camElements = {}
camElementStructure = ['Camera Name','Url','Port','Path','User','Password','Enabled']




gpioIndex = [i for i in range(1-27)]

gpioStateDict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,
                 10:0,11:0,12:0,13:0,14:0,15:0,16:0,
                 17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0}


AlarmArmed = False

CountDownToAlarm = 30
CountDownState = None






piFactoryXConnect = {
                   'localhost':'localhost',
                  'SecurityPi':'10.0.0.21',
                'GarageDoorPi':'192.168.1.4',
                 'SprinklerPi':'192.168.6.2',
                   'ClimatePi':'192.168.6.4'
                }


piFactoryXConnectOld = {}


testData = []



################################################### 

mySqlIpAddress = ''
mySqlUserName = ''
mySqlPassword = ''
mySqlDatabaseConnection = ''
mySqlTableName = ''
Update_Interval = 0

###################################################

SUPER_FONT=("Verdana",36)
LARGE_FONT=("Verdana",12)
NORMAL_FONT=("Verdana",10)
SMALL_FONT=("Verdana",8)

###################################################
fullscreen = False
bckGround = "#333"
forGround = "#FFF"
forGrdRed = "#F00"

bckGroundDisabled = "GREY"

###################################################

debugApp = False

###################################################

currentDt = ""
counter = 0

imgConnect = "images/connecting.jpg"
imgOffline = "images/offline.jpg"

password = 'MTIzNDU2'.encode('ascii')

imgBluePrint = "images/bluePrint.gif"

TagElementPath = 'bin/TagElement.omf'
CamElementPath = 'bin/CamElement.omf'

###################################################

labelSettings = {'width':15,
                      'background':bckGround,
                      'foreground':forGround,
                      'anchor':'e',
                      'font':SMALL_FONT}

textBoxSettings = {'height':1,
                        'width':20,
                        'font':SMALL_FONT}

entrySettings = {'width':20,
                        'font':SMALL_FONT}