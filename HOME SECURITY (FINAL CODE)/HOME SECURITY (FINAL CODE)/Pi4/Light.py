import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# port 7 for relay module
#port 22 for red LED 
#port 24 for green LED
GPIO.setup(7, GPIO.out)
GPIO.setup(22,GPIO.out)
GPIO.setup(24,GPIO.out)

#if person detected
def detect() :
    GPIO.output(7, False)
    GPIO.output(22,False)
    GPIO.output(24,False)
    GPIO.output(24,True)
    GPIO.output(7,True)

    time.sleep(7)

    GPIO.output(7, False)
    GPIO.output(22,False)
    GPIO.output(24,False)


def unknown(): 
    GPIO.output(7, False)
    GPIO.output(22,False)
    GPIO.output(24,False)
    GPIO.output(22,True)
    time.sleep(3)
    GPIO.output(22,False)
    GPIO.output(7,False)


def hold () : 
    GPIO.output(7, False)
    GPIO.output(22,False)
    GPIO.output(24,False)
    GPIO.output(24,True)
    GPIO.output(22,True)
    GPIO.output(7,False)

def endTime() : 
    GPIO.output(7,False)
    GPIO.output(22,False)
    GPIO.output(24,False)
    
    GPIO.output(24, True)
    time.sleep(1)
    GPIO.output(24,False)
    time.sleep(1)
    GPIO.output(24, True)
    time.sleep(1)
    GPIO.output(24,False)

