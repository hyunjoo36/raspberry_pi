import RPi.GPIO as GPIO
import I2C_driver as LCD
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED2 = 12
SW2 = 16

GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

PWM_LED2= GPIO.PWM(LED2, 50)
PWM_LED2.start(0)

mylcd= LCD.lcd()

cnt=0
duty=0

while True:        
       
    if GPIO.input(SW2) == GPIO.HIGH:
        time.sleep(0.2)
        mylcd.lcd_clear()
        print (cnt)
        if cnt==0 :
            duty=20
                    
        if cnt==1 :
            duty=50
             
        if cnt==2 :
            duty=90
            
        cnt1 = str(cnt)
        Duty1= str(duty)
        mylcd.lcd_display_string("cnt :"+ cnt1,1)
        mylcd.lcd_display_string("Duty :"+ Duty1,2)
        
        PWM_LED2.start(0)
        PWM_LED2.ChangeDutyCycle(duty)

        cnt += 1
        if cnt==3:
            cnt=0