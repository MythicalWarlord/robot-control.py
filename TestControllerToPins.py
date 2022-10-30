#!/usr/bin/env python

import RPi.GPIO as GPIO

from pyPS4Controller.controller import Controller
GPIO.setwarnings(False)

#sets pins
xPressPin=17
analogPinr=12
analogPinl=13

#tells system what method to number pins 
GPIO.setmode(GPIO.BCM)

#sets pins as outputs
GPIO.setup(analogPinr, GPIO.OUT)

GPIO.setup(analogPinl, GPIO.OUT)

GPIO.setup(xPressPin, GPIO.OUT)

#setsup pin as a pwm and sets frequency 
my_pwmr=GPIO.PWM(analogPinr,100 )

#sets the start value to 0, with out this line the code will run with out pin output
my_pwm.start(0)

my_pwml=GPIO.PWM(analogPinl,100 )

my_pwm.start(0)

#math function to set a range from 0-100 for setting pwm stuff
def analog_to_pwm(value):
    value = ((100 * (value + 32767)) // 65534)
    return value

#controller inputs and what to do with the outputs. 
class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self,**kwargs)

    def on_x_press(self):
        GPIO.output(xPressPin, GPIO.HIGH)
    
    def on_x_release(self):
        GPIO.output(xPressPin, GPIO.LOW) 
    
    def on_L2_press(self, value):
        outl = analog_to_pwm(value)
        #debug print command not needed
        print(outl)
        my_pwml.ChangeDutyCycle(outl)
    
    def on_L2_release(self):
        my_pwml.ChangeDutyCycle(0)
    
    def on_R2_press(self, value):
        outr = analog_to_pwm(value)
        #debug print command not needed
        print(outr)
        my_pwmr.ChangeDutyCycle(outr)
    
    def on_R2_release(self):
        my_pwmr.ChangeDutyCycle(0)

#controller connection and listening path
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
