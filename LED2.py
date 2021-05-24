import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LED = 12
LED2 = 16

def main():
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)

    while 1:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED2, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1)
        GPIO.output(LED2, GPIO.LOW)
        time.sleep(1)
        
if __name__=='__main__':
    main()