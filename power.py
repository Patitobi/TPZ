from time import sleep
import RPi.GPIO as GPIO
import pygame
from pygame.locals import * 

pygame.init()
screen=pygame.display.set_mode((640, 480))
pygame.display.set_caption('Test')
pygame.mouse.set_visible(0)

while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            main = False
            break
            
        if (event.type==pygame.KEYDOWN):
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('LEFT DOWN')
                sleep(0.1)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('RIGHT DOWN')
                sleep(0.1)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('UP DOWN')
                sleep(0.1)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('DOWN DOWN')
                sleep(0.1)
            
        if (event.type==pygame.KEYUP):
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('LEFT UP')
                sleep(0.1)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('RIGHT UP')
                sleep(0.1)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('UP UP')
                
                sleep(0.1)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('DOWN UP')
                sleep(0.1)
    
    
    
    

