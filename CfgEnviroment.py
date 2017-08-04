import os


def defineEnviroment():
    
    os.environ['GPIOZERO_PIN_FACTORY'] = 'pigpio'
    
    os.environ['PIGPIO_ADDR'] = '10.0.0.21'