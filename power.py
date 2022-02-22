from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)

i = 1
while i >= 1:
    print(i)
    
    GPIO.output(23,GPIO.HIGH)
    
    sleep(5)
    
    GPIO.output(23, GPIO.LOW)
    
    sleep(2)
    
    i += 1
    try:
        x = input()
        print ('Try using KeyboardInterrupt')
    except KeyboardInterrupt(f):
        print ('KeyboardInterrupt exception is caught')
    else:
        print ('Valla')
    
GPIO.cleanup()