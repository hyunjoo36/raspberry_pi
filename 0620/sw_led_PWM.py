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

Freq =10
cnt=0
duty=0

while True:        
       
    if GPIO.input(SW2) == GPIO.HIGH:
        time.sleep(0.2)
        mylcd.lcd_clear()
        print (cnt)
        if cnt==0 :
            Freq=10
                    
        if cnt==1 :
            Freq = 50
             
        if cnt==2 :
            Freq = 100
            
        cnt1 = str(cnt)
        Freq1= str(Freq)
        mylcd.lcd_display_string("cnt :"+ cnt1,1)
        mylcd.lcd_display_string("Freq :"+ Freq1,2)
        
        PWM_LED2.ChangeFrequency(Freq)
        PWM_LED2.start(0)
        
        for duty in range(100):
            PWM_LED2.ChangeDutyCycle(duty)
            time.sleep(0.05)
        cnt += 1
        if cnt==3:
            cnt=0


                
