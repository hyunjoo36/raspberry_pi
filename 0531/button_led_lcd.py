import RPi.GPIO as GPIO  #Import Raspberry Pi GPIO library
import I2C_driver as LCD
import time

GPIO.setmode(GPIO.BOARD)
Switch =10
LED=12

GPIO.setwarnings(False)  #Ignore warning for now
GPIO.setmode(GPIO.BOARD)  #Use physical pin numbering

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
#Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

mylcd= LCD.lcd()

while True:
    #GPIO.input(Switch) == GPIO.HIGH  AND
    if GPIO.input(Switch) == GPIO.HIGH:
        print("Button was pushed!")
        mylcd.lcd_display_string("LED ON",1)
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1.5)
    else:
        print("Button was not pushed!")
        mylcd.lcd_display_string("LED OFF",1)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1.5)
    mylcd.lcd_clear()