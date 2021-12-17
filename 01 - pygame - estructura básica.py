
import pygame
import sys
import time

ejecutando = True
frameRate = 60
frameCount = 0

pygame.init()

canvas = pygame.display.set_mode([600, 400],pygame.RESIZABLE)

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global ejecutando
            ejecutando = false


def update():
    events()
    pygame.display.flip()
    time.sleep(1/frameRate)
    global frameCount
    frameCount += 1


def draw():
    pygame.draw.rect(canvas, [frameCount % 255, 0, 0], [0, 0, 600, 400])

while ejecutando:
    draw()
    update()

sys.exit()
