import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)   

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
number = [0, 0, 0, 0, 0, 0, 1, 0]



#for i in leds[::1]:
#    GPIO.output(i, 1)
#    time.sleep(0.2)
#    GPIO.output(i, 0)

number = [1, 1, 0, 0, 0, 0, 0, 0]


GPIO.output(dac, number)
time.sleep(15)
GPIO.output(dac, 0)
GPIO.cleanup()