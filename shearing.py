import pygame
from pygame import gfxdraw
import numpy as np

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN =  (0,128,0)
BLUE = (0, 56, 147)

isp = False
x1 = y1 = x2 = y2 = 0
ps = (x1, y1)
pe = (x2, y2)

def prepare_screen():
    """
    Create the initial screen.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    screen.fill((0,0,0))
    pygame.display.set_caption("Shearing")
    return screen

def shearX(x,y,shx):
    mat =([x],
        [y],
        [1])
    
    transformMat = ([1,shx,0],[0,1,0],[0,0,1])

    translatedPoints = np.dot(transformMat, mat)

    return translatedPoints[0],translatedPoints[1]

def shearY(x,y,shy):
    mat =([x],
        [y],
        [1])
    
    transformMat = ([1,0,0],[shy,1,0],[0,0,1])

    translatedPoints = np.dot(transformMat, mat)

    return translatedPoints[0],translatedPoints[1]

screen = prepare_screen()
a = (80,180)
b = (110,250)
c = (120,210)
gfxdraw.filled_polygon(screen, [a,b,c], YELLOW)
ax = shearX(a[0],a[1], 0.5)
bx = shearX(b[0],b[1], 0.5)
cx = shearX(c[0],c[1], 0.5)
gfxdraw.filled_polygon(screen, [ax,bx,cx], GREEN)

ay = shearY(a[0],a[1], 1)
by = shearY(b[0],b[1], 1)
cy = shearY(c[0],c[1], 1)
gfxdraw.filled_polygon(screen, [ay,by,cy], BLUE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()