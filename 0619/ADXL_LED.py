# ADXL345_driver library
import ADXL345_driver as ADXL
import RPi.GPIO as GPIO

# time library
import time

GPIO.setwarnings(False)  #Ignore warning for now
GPIO.setmode(GPIO.BOARD)  #Use physical pin numbering

LED=11
LED2=12

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)

# x-axis, y-axis, z-axis adress
x_adr = 0x32
y_adr = 0x34
z_adr = 0x36

def main():
    ADXL.init_ADXL345()

    while 1:
        x_acc = ADXL.measure_acc(x_adr)
        y_acc = ADXL.measure_acc(y_adr)
        z_acc = ADXL.measure_acc(z_adr)

        if x_acc <0:
            GPIO.output(LED, GPIO.HIGH)           
            GPIO.output(LED2, GPIO.LOW)
        elif x_acc == 0:
            GPIO.output(LED, GPIO.LOW)
            GPIO.output(LED2, GPIO.LOW)
        else:
            GPIO.output(LED, GPIO.LOW)           
            GPIO.output(LED2, GPIO.HIGH)
        
        
if __name__ == '__main__':
    main()