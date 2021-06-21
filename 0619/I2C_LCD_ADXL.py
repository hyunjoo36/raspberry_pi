# ADXL345_driver library
import ADXL345_driver as ADXL
# I2C_driver library
import I2C_driver as LCD
# time library
import time

mylcd = LCD.lcd()

# x-axis, y-axis, z-axis adress
x_adr = 0x32
y_adr = 0x34
z_adr = 0x36

def main():
    ADXL.init_ADXL345()
    
    while 1:
        a=int(input('Select Num : '))
        if a==1 :
            b=input('char input = ')
            mylcd.lcd_clear()
            mylcd.lcd_display_string(b,1)
            
        if a==2 :
            for i in range(1,4):
                x_acc = ADXL.measure_acc(x_adr)
                y_acc = ADXL.measure_acc(y_adr)
                z_acc = ADXL.measure_acc(z_adr)
                print ('X = %2.2f' % x_acc, '[g], Y = %2.2f' % y_acc, '[g], Z = %2.2f' % z_acc, '[g]')
                time.sleep(0.5)        
        
if __name__ == '__main__':
    main()