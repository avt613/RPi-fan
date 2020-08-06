import RPi.GPIO as GPIO
import os
import time
threshold_on = 35
fan_pin = 15
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#fan
GPIO.setup(fan_pin,GPIO.OUT)
GPIO.output(fan_pin,GPIO.LOW)
def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return float(temp.replace("temp=","").replace("'C",""))

while True:
    temp = measure_temp()
    print(temp)
    if temp > threshold_on:
        GPIO.output(fan_pin,GPIO.HIGH)
    else:
        GPIO.output(fan_pin,GPIO.LOW)
    time.sleep(1)
