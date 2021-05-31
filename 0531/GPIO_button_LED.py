import RPi.GPIO as GPIO  #Import Raspberry Pi GPIO library
import time

GPIO.setmode(GPIO.BOARD)
Switch =10
LED=12

GPIO.setwarnings(False)  #Ignore warning for now
GPIO.setmode(GPIO.BOARD)  #Use physical pin numbering

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
#Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    #GPIO.input(Switch) == GPIO.HIGH  AND
    if GPIO.input(Switch) == GPIO.HIGH:
        print("Button was pushed!")
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
    else:
        print("Button was not pushed!")
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1)