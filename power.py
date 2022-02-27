from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
while True:
    print('Ein') 
    GPIO.output(14,GPIO.HIGH)

    sleep(5)
    print('Aus')

    GPIO.output(14, GPIO.LOW)
    
    print('weiter = 1 stop = 0')
    eingabe = int(input())
    if eingabe == 0 :
        break
        print('beenden')
    
GPIO.cleanup()
    

