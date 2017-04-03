import RPi.GPIO as GPIO
import time
import sys

pin = int(sys.argv[1])
print "blinking on", pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

while True:
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
