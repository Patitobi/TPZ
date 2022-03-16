from cgitb import text
from time import sleep
from turtle import color
import RPi.GPIO as GPIO
import pygame
from pygame.locals import *

#Fenster einstellen (Board Computer/ Vogel perspektive auf den Panzer)
pygame.init()
screenwidth = 800
screenheight = 600
screen=pygame.display.set_mode((screenwidth, screenheight))
color = (77, 77, 77) #Schwarz
screen.fill(color)
pygame.display.update() #updated den screen einmal um die farbe zu ändern
pygame.display.set_caption('Board Computer')
#pygame.mouse.set_visible(0)

Panzerneutralimg = pygame.image.load('PanzerNeutral.png') #Bild des Panzers in neutraler ausrichtung
PanzerRechtsimg = pygame.image.load('PanzerRechts.png') #Bild des Panzers in rechter ausrichtung
PanzerLinksimg = pygame.image.load('PanzerLinks.png') #Bild des Panzers in linker ausrichtung

Pfeilneutralimg = pygame.image.load('Pfeilneutral.png') #Pfeilneutral
PfeilRechtsimg = pygame.image.load('PfeilRechts.png') #PfeilRechts
PfeilLinksimg = pygame.image.load('PfeilLinks.png') #PfeilLinks
PfeilBackimg = pygame.image.load('PfeilBack.png') #PfeilBack

def ControllerConnect(): #Konzept für einen Controller Connect waiting Screen
    font = pygame.font.Font('freesansbold.ttf', 20) #Schriftart und Schriftgröße
    Controllertext = font.render('Verbinden sie einen Controller...', True,)#Schrift einfügen
    Controller = 0
    while Controller == 0:
        screen.blit(Controllertext)
        sleep(2)
        #if #Controller Connection == true:
        #   Controller += 1




def Panzernull():
    screen.fill(color)
    screen.blit(Panzerneutralimg, (screenwidth / 2 - 128 / 2, screenheight / 2 - 191 / 2)) #Panzer wenn keine Taste gedrückt wird

def Panzerneutral():
    screen.fill(color)
    screen.blit(Panzerneutralimg, (screenwidth / 2 - 128 / 2, screenheight / 2 - 191 / 2)) #Bildschirmbreite / 2 - Bildbreite / 2, Bildschirmlänge / 2 - Bildlänge / 2 (Gecentert)
    screen.blit(Pfeilneutralimg, (screenwidth / 2 - 68 / 2, screenheight / 2 - 112 / 2 - 200))


def PanzerRechts():
    screen.fill(color)
    screen.blit(PanzerRechtsimg, (screenwidth / 2 - 174 / 2, screenheight / 2 - 219 / 2))
    screen.blit(PfeilRechtsimg, (screenwidth / 2 - 68 / 2 + 55, screenheight / 2 - 112 / 2 - 200))

def PanzerLinks():
    screen.fill(color)
    screen.blit(PanzerLinksimg, (screenwidth / 2 - 174 / 2, screenheight / 2 - 219 / 2))
    screen.blit(PfeilLinksimg, (screenwidth / 2 - 68 / 2 - 55, screenheight / 2 - 112 / 2 - 200))

def PanzerBack():
    screen.fill(color)
    screen.blit(Panzerneutralimg, (screenwidth / 2 - 128 / 2, screenheight / 2 - 191 / 2))
    screen.blit(PfeilBackimg, (screenwidth / 2 - 68 / 2, screenheight / 2 - 112 / 2 + 200))

#Auf Controller Warten
#ControllerConnect()
#Panzer auf Null(Gerade) stellen bei Start
Panzernull()
pygame.display.update()

while True:
    GPIO.setmode(GPIO.BCM)
    engine_left = 14
    engine_right = 15
    GPIO.setup(engine_left, GPIO.OUT)
    GPIO.setup(engine_right, GPIO.OUT)

    
    
    for event in pygame.event.get():

        if (event.type==pygame.KEYDOWN):
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                main = False
                
            
        if (event.type==pygame.KEYDOWN):
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('LEFT DOWN')
                GPIO.output(engine_right, 0)
                PanzerLinks()
                pygame.display.update() # Panzer wird im Board Computer nach links ausgerichtet
                
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('RIGHT DOWN')
                GPIO.output(engine_left, 0)
                PanzerRechts()
                pygame.display.update() # Panzer wird im Board Computer nach rechts ausgerichtet
                
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('UP DOWN')
                GPIO.output(engine_left, 0)
                GPIO.output(engine_right, 0)
                Panzerneutral()
                pygame.display.update() # Panzer wird im Bord Computer Geradeaus gerichtet
                
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('DOWN DOWN')
                PanzerBack()
                pygame.display.update() # Panzer wird im Bord Computer Geradeaus gerichtet(Pfeil zeigt nach hinten)

            if event.key == pygame.K_ESCAPE:
                GPIO.cleanup()
                print('ENDE')
                exit()

        if (event.type==pygame.KEYUP):
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('LEFT UP')
                GPIO.output(engine_right, 1)
                Panzernull()
                pygame.display.update() # Panzer wird im Bord Computer Geradeaus gerichtet
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('RIGHT UP')
                GPIO.output(engine_left, 1)
                Panzernull()
                pygame.display.update() # Panzer wird im Bord Computer Geradeaus gerichtet
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('UP UP')
                GPIO.output(engine_left, 1)
                GPIO.output(engine_right, 1)
                Panzernull()
                pygame.display.update() # Panzer wird im Bord Computer Geradeaus gerichtet
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('DOWN UP')
                Panzernull()
                pygame.display.update() # Panzer wird im Bord Computer Geradeaus gerichtet