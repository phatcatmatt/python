import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)

count = 0

while True:
    inputVal = GPIO.input(12)
    if (inputVal == True):
        count = count + 1
        print("Button pressed " +str(count) + " times.")
    time.sleep(.15)
