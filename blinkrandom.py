import RPi.GPIO as GPIO
import time
import sys
import random

pin1 = int(sys.argv[1])
pin2 = int(sys.argv[2])
pin1Val = False
pin2Val = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

print("blinking on", pin1, pin2)

while True:
    pin = random.randint(pin1,pin2)
    if pin == pin1:
        pin1Val = not pin1Val
        GPIO.output(pin1, GPIO.HIGH if pin1Val else GPIO.LOW)
    elif pin == pin2:
        pin2Val = not pin2Val
        GPIO.output(pin2, GPIO.HIGH if pin2Val else GPIO.LOW)
    time.sleep(random.uniform(0, .7))
