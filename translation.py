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
    screen = pygame.display.set_mode((800, 800))
    screen.fill((0,0,0))
    pygame.display.set_caption("Translation")
    return screen

def translate(x,y, tx, ty):
    mat =([x],
        [y],
        [1])

    transformMat = ([1,0,tx],[0,1,ty],[0,0,1])

    translatedPoints = np.dot(transformMat, mat)

    return translatedPoints[0],translatedPoints[1]

screen = prepare_screen()
a = (160,280)
b = (210,350)
c = (220,310)
gfxdraw.filled_polygon(screen, [a,b,c], YELLOW)
a = translate(a[0],a[1], 150, 150)
b = translate(b[0],b[1], 150, 150)
c = translate(c[0],c[1], 150, 150)
gfxdraw.filled_polygon(screen, [a,b,c], GREEN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()