import RPi.GPIO as GPIO
#import time

GPIO.setwarnings(False)


GPIO.setmode(GPIO.BCM)   

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)

aux = [22, 23, 27, 18, 15, 14, 3, 2]
GPIO.setup(aux, GPIO.IN)
GPIO.output(leds, 1)
i = 0
while(1):
    i = 0
    while i < 8:
        c = GPIO.input(aux[i])
        GPIO.output(leds[i], c)
        i += 1

GPIO.cleanup()

