from time import sleep
import RPi.GPIO as GPIO
import pygame
from pygame.locals import * 

pygame.init()
screen=pygame.display.set_mode((640, 480))
pygame.display.set_caption('Test')
pygame.mouse.set_visible(0)

while True:
    print('go')
    
    for event in pygame.event.get():
        if (event.type==KEYUP) or (event.type==KEYDOWN):
            print('entlich')
            sleep(0.1)

while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14,GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    print('Ein') 
    GPIO.output(14,GPIO.HIGH)
    GPIO.output(15,GPIO.HIGH)

    sleep(5)
    print('Aus')
    GPIO.cleanup()
    
    print('weiter = 1 stop = 0')
    eingabe = int(input())
    if eingabe == 0 :
        GPIO.cleanup()
        print('beenden Teil 1')
        break
    
    
    
    

