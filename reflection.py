import pygame
from pygame import gfxdraw
import numpy as np


WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN =  (0,128,0)
  
isp = False
x1 = y1 = x2 = y2 = 0
ps = (x1, y1)
pe = (x2, y2)

def prepare_screen():
    """
    Create the initial screen.
    """
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    screen.fill((0,0,0))
    pygame.display.set_caption("Reflection")
    return screen

def reflection(x,y):
    mat =([x],
        [y],
        [1])
    
    transformMat = ([0,1,0],[1,0,0],[0,0,1])

    translatedPoints = np.dot(transformMat, mat)

    return translatedPoints[0],translatedPoints[1]

screen = prepare_screen()
gfxdraw.line(screen,0,0,1000,1000, WHITE)
a = (160,280)
b = (210,350)
c = (220,310)
gfxdraw.filled_polygon(screen, [a,b,c], YELLOW)
a = reflection(a[0],a[1])
b = reflection(b[0],b[1])
c = reflection(c[0],c[1])
gfxdraw.filled_polygon(screen, [a,b,c], GREEN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()