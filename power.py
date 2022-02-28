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
    engine_left = 14
    engine_right = 15
    GPIO.setup(engine_left, GPIO.OUT)
    GPIO.setup(engine_right, GPIO.OUT)

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            main = False
            
        if (event.type==pygame.KEYDOWN):
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('LEFT DOWN')
                GPIO.output(engine_right, 1)
                sleep(0.1)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('RIGHT DOWN')
                GPIO.output(engine_left, 1)
                sleep(0.1)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('UP DOWN')
                GPIO.output(engine_left, 1)
                GPIO.output(engine_right, 1)
                sleep(0.1)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('DOWN DOWN')
                sleep(0.1)
            if event.key == pygame.K_ESCAPE:
                GPIO.cleanup()
                print('ENDE')
                exit()
            
        if (event.type==pygame.KEYUP):
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('LEFT UP')
                GPIO.output(engine_right, 0)
                sleep(0.1)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('RIGHT UP')
                GPIO.output(engine_left, 0)
                sleep(0.1)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('UP UP')
                GPIO.output(engine_left, 0)
                GPIO.output(engine_right, 0)
                sleep(0.1)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('DOWN UP')
                sleep(0.1)