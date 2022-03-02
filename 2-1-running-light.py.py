import RPi.GPIO as GPIO
import time

#GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)   

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)


d = 0
while d < 3:
    for i in leds[::1]:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)
    d = d + 1

GPIO.output(leds, 0)
GPIO.cleanup()