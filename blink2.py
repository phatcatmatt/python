import RPi.GPIO as GPIO
import time
import sys
import random

pin1 = int(sys.argv[1])
pin2 = int(sys.argv[2])

print "blinking on", pin1, pin2

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

while True:
    GPIO.output(pin1, GPIO.HIGH)
    time.sleep(random.random())
    GPIO.output(pin1, GPIO.LOW)
    time.sleep(random.random())
    GPIO.output(pin2, GPIO.HIGH)
    time.sleep(random.random())
    GPIO.output(pin2, GPIO.LOW)
    time.sleep(random.random())
