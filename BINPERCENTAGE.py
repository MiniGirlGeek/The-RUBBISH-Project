import pygame, sys
from time import *
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((320, 240))
pygame.display.set_caption('The \'RUBBISH\' Project')

blueBin = pygame.image.load('blue_bin.png')
greyBin = pygame.image.load('grey_bin.png')
blackBin = pygame.image.load('black_bin.png')
greenBin = pygame.image.load('green_bin.png')
streetButton = pygame.image.load('street_button.png')
brickWall = pygame.image.load('brickWall.png')
starBanner = pygame.image.load('star_banner.png')
cog = pygame.image.load('cog.png')
infoButton =  pygame.image.load('info_button.png')
globe = pygame.image.load('globe.png')
back = pygame.image.load('back_arrow.fw.png')
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(172, 215, 0)
BLUE = pygame.Color(41, 207, 226)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
YELLOW = pygame.Color(251, 212, 0)
mousex, mousey = 0, 0
score =100
length = 5
screen = "home"
fontObj = pygame.font.Font('36daysag.ttf', 25)
msg = 'Heya Andrew :)'
whiteText = fontObj.render(msg, 1, WHITE)

soundObj = pygame.mixer.Sound('bounce.wav')

def home(length):
    if length == 263:
        length =0
    else:
        length += 1
    windowSurfaceObj.fill(BLUE)
    pygame.draw.rect(windowSurfaceObj, BLACK, (0, 200, 320, 40))
    pygame.draw.rect(windowSurfaceObj, GREEN, (0, 201, 320, 39))
    windowSurfaceObj.blit(blueBin, (7.2, 120))
    windowSurfaceObj.blit(greyBin, (70, 120))
    windowSurfaceObj.blit(blackBin, (133, 120))
    windowSurfaceObj.blit(greenBin, (196, 120))
    windowSurfaceObj.blit(brickWall, (262, -1))
    pygame.draw.rect(windowSurfaceObj, YELLOW, (0, 19, length, 52))
    windowSurfaceObj.blit(starBanner, (0, 19))
    windowSurfaceObj.blit(infoButton, (278, 9))
    windowSurfaceObj.blit(globe, (273, 85))
    windowSurfaceObj.blit(cog, (277, 130))
    windowSurfaceObj.blit(streetButton, (267, 46))

def clicked(text):
    windowSurfaceObj.fill(BLUE)
    msg = "This is the 'Rubbish Project!"
    windowSurfaceObj.blit(whiteText, (100, 25))
    windowSurfaceObj.blit(back, (10, 10))

def display(screen, length, whiteText):
    if screen == "home":
        home(length)
    if screen == "clicked":
        clicked(whiteText)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos 
	elif event.type == MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            if screen == "clicked" and mousey >= 10 and mousey <= 60 and mousex <= 81 and mousex >= 10:
                screen = "home"
            elif screen == "home" and mousey >= 9 and mousey <= 36 and mousex <= 305 and mousex >= 278:
                screen = "clicked"
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    display(screen, length, whiteText)

    pygame.display.update()
    fpsClock.tick(30)
