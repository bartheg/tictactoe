#!/usr/bin/python2
import pygame, sys #pygame.mixer
from pygame.locals import *
pygame.init()

screenSize = (500,320)
sizeTura = (50,50)
spriteO = pygame.image.load('img/poleo.png')
spriteX = pygame.image.load('img/polex.png')
spriteN = pygame.image.load('img/pole.png')
spriteLabelTura = pygame.image.load('img/label.png')
spriteLabelEnd = pygame.image.load('img/end.png')
spriteLabel = spriteLabelTura
spriteTuraO = pygame.transform.scale(spriteO, sizeTura)
spriteTuraX = pygame.transform.scale(spriteX, sizeTura)
spriteTura = spriteTuraO
spriteButton = pygame.image.load('img/button.png')
xypola = [(10,10),(110,10),(210,10),(10,110),(110,110),(210,110),(10,210),(110,210),(210,210)]
xylabel = (325,50)
xytura = (425,50)
xybutton = (325,150)
sizeofpole = 100
sizeofbutton = (150,70)
gun = pygame.mixer.Sound('snd/gun.wav')
fanfare = pygame.mixer.Sound('snd/fanfare.wav')
drums = pygame.mixer.Sound('snd/drums.wav')
bgcolor = (10,10,10)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
pola = ['n','n','n','n','n','n','n','n','n']
tura = 'o'
iswinner = False

def drawScreen():
    screen.fill(bgcolor)
    def drawPole(index):
        if pola[index] == 'n':
            screen.blit(spriteN,xypola[index])
        elif pola[index] == 'x':
            screen.blit(spriteX,xypola[index])
        else:
            screen.blit(spriteO,xypola[index])
    for i in range(9):
        drawPole(i)
    screen.blit(spriteLabel, xylabel)
    screen.blit(spriteTura, xytura)
    screen.blit(spriteButton, xybutton)
        
def odNowa():
    global pola
    global tura
    global spriteLabelTura
    global spriteLabel
    global iswinner
    iswinner = False
    pola = ['n','n','n','n','n','n','n','n','n']
    tura = 'o'
    spriteLabel = spriteLabelTura
    drums.play()

def sprawdz():
    o3 = ['o','o','o']
    x3 = ['x','x','x']
    # poziomo
    if pola[0:3] == o3 or pola[0:3] == x3:
        return pola[0] 
    elif pola[3:6] == o3 or pola[3:6] == x3:
        return pola[3] 
    elif pola[6:9] == o3 or pola[6:9] == x3:
        return pola[6] 
    # pionowo
    elif pola[0::3] == o3 or pola[0::3] == x3:
        return pola[0] 
    elif pola[1::3] == o3 or pola[1::3] == x3:
        return pola[1] 
    elif pola[2::3] == o3 or pola[2::3] == x3:
        return pola[2] 
    # przekatne
    elif pola[0::4] == o3 or pola[0::4] == x3:
        return pola[0] 
    elif pola[2:7:2] == o3 or pola[2:7:2] == x3:
        return pola[2] 
    else:
        return 'n'

def ruchNaPole(index):
    global iswinner
    if pola[index] == 'n' and iswinner == False:
        global tura
        global spriteTura
        global spriteTuraO
        global spriteturaX
        global spriteLabel
        global spriteLabelEnd
        pola[index] = tura
        if sprawdz() == 'n':
            gun.play()
            if tura == 'o':
                tura = 'x'
                spriteTura = spriteTuraX
            else:
                tura = 'o'
                spriteTura = spriteTuraO
        else:
            spriteLabel = spriteLabelEnd
            fanfare.play()
            iswinner = True
odNowa()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_KP1:
            ruchNaPole(6)
        elif event.type == KEYDOWN and event.key == K_KP2:
            ruchNaPole(7)
        elif event.type == KEYDOWN and event.key == K_KP3:
            ruchNaPole(8)
        elif event.type == KEYDOWN and event.key == K_KP4:
            ruchNaPole(3)
        elif event.type == KEYDOWN and event.key == K_KP5:
            ruchNaPole(4)
        elif event.type == KEYDOWN and event.key == K_KP6:
            ruchNaPole(5)
        elif event.type == KEYDOWN and event.key == K_KP7:
            ruchNaPole(0)
        elif event.type == KEYDOWN and event.key == K_KP8:
            ruchNaPole(1)
        elif event.type == KEYDOWN and event.key == K_KP9:
            ruchNaPole(2)
        elif event.type == KEYDOWN and event.key == K_r:
            odNowa()
        elif event.type == KEYDOWN and event.key == K_KP0:
            odNowa()
        elif event.type == MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos() 
            if spriteButton.get_rect().collidepoint(mousepos[0]-xybutton[0],mousepos[1]-xybutton[1]):
                odNowa()
            elif spriteN.get_rect().collidepoint(mousepos[0]-xypola[0][0],mousepos[1]-xypola[0][1]):
                ruchNaPole(0)
            elif spriteN.get_rect().collidepoint(mousepos[0]-xypola[1][0],mousepos[1]-xypola[1][1]):
                ruchNaPole(1)
            elif spriteN.get_rect().collidepoint(mousepos[0]-xypola[2][0],mousepos[1]-xypola[2][1]):
                ruchNaPole(2)
            elif spriteN.get_rect().collidepoint(mousepos[0]-xypola[3][0],mousepos[1]-xypola[3][1]):
                ruchNaPole(3)
            elif spriteN.get_rect().collidepoint(mousepos[0]-xypola[4][0],mousepos[1]-xypola[4][1]):
                ruchNaPole(4)
            elif spriteN.get_rect().collidepoint(mousepos[0]-xypola[5][0],mousepos[1]-xypola[5][1]):
                ruchNaPole(5)
            elif spriteN.get_rect().collidepoint(mousepos[0]-xypola[6][0],mousepos[1]-xypola[6][1]):
                ruchNaPole(6)
            elif spriteN.get_rect().collidepoint(mousepos[0]-xypola[7][0],mousepos[1]-xypola[7][1]):
                ruchNaPole(7)
            elif spriteN.get_rect().collidepoint(mousepos[0]-xypola[8][0],mousepos[1]-xypola[8][1]):
                ruchNaPole(8)
    drawScreen() 
    pygame.display.flip()
