import RPi.GPIO as GPIO  #Import Raspberry Pi GPIO library

GPIO.setmode(GPIO.BOARD)
Switch =10

GPIO.setwarnings(False)  #Ignore warning for now
GPIO.setmode(GPIO.BOARD)  #Use physical pin numbering

#Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    #GPIO.input(Switch) == GPIO.HIGH  AND
    if GPIO.input(Switch) == GPIO.HIGH:
        print("Button was pushed!")
    else:
        print("Button was not pushed!")
