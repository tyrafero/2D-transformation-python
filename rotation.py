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
    pygame.display.set_caption("Rotation")
    return screen
screen = prepare_screen()
def rotat(x,y,a):
    a = np.math.radians(a)
    m =([x],
        [y],
        [1])
    transformM = ([np.math.cos(a),-np.math.sin(a),0],[np.math.sin(a),np.math.cos(a),0],[0,0,1])
    translatedPoints = np.dot(transformM, m)
    return translatedPoints[0],translatedPoints[1]
m = (200,600)
n = (300,200)
o = (400,250)
gfxdraw.filled_polygon(screen, [m,n,o], YELLOW)
m = rotat(m[0],m[1], 330)
n = rotat(n[0],n[1], 330)
o = rotat(o[0],o[1], 330)
gfxdraw.filled_polygon(screen, [m,n,o], GREEN)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()