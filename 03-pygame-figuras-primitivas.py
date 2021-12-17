
import pygame
import pygame.gfxdraw
import time
import math

ejecutando = True
frameRate = 60
frameCount = 0
width = 600
height = 400
mouseX = 0
mouseY = 0
pmouseX = 0
pmouseY = 0
movedX = 0
movedY = 0

pygame.init()

canvas = pygame.display.set_mode([width, height], pygame.RESIZABLE)

def setIcon(ruta):
    try:
        icon = pygame.image.load(ruta)
        pygame.display.set_icon(icon)
    except:
        pass


def setTitle(title):
    pygame.display.set_caption(title)


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global ejecutando
            ejecutando = false


def updateVariables():
    global width, height
    global mouseX, mouseY
    global pmouseX, pmouseY
    global movedX, movedY
    sz = pygame.display.get_window_size()
    width = sz[0]
    height = sz[1]
    mouse = pygame.mouse.get_pos()
    pmouseX = mouseX
    pmouseY = mouseY
    mouseX = mouse[0]
    mouseY = mouse[1]
    movedX = mouseX - pmouseX
    movedY = mouseY - pmouseY


def updateFrame():
    global frameCount
    pygame.display.flip()
    time.sleep(1/frameRate)
    frameCount += 1


def update():
    updateVariables()
    events()
    updateFrame()

# funciones de dibujo


def background(color):
    rect(0, 0, width, height, color)


def rect(x, y, w, h, color="white"):
    if(len(color) == 4 and (type(color) == tuple or type(color) == list)):
        pygame.gfxdraw.box(canvas, (x, y, w, h), color)
    else:
        pygame.draw.rect(canvas, color, (x, y, w, h))


def drawRect(x, y, w, h, color="black", weight=1):
    if(weight == 0):
        return

    if(weight == 1 and len(color) == 4 and (type(color) == tuple or type(color) == list)):
        pygame.gfxdraw.rectangle(canvas, (x, y, w, h), color)
    else:
        pygame.draw.rect(canvas, color, (x, y, w, h), weight)


def hline(y, color):
    pygame.gfxdraw.hline(canvas, width, 0, y, color)


def vline(x, color):
    pygame.gfxdraw.vline(canvas, x, height, 0, color)


def circle(x, y, r, color):
    if(len(color) == 4 and (type(color) == tuple or type(color) == list)):
        pygame.gfxdraw.filled_circle(canvas, x, y, r, color)
    else:
        pygame.draw.circle(canvas, color, (x, y), r)


def draw():
    background("skyblue")
    color = (255, 255, 255, 100)
    circle(mouseX, mouseY, 50, color)
    color = (0, 0, 0, 100)
    rect(mouseX, mouseY, 50, 50, color)
    hline(mouseY, color)
    vline(mouseX, color)
    color = "red"
    drawRect(mouseX, mouseY, 50, 50, color)
    r = math.sqrt(math.pow(movedX, 2)+math.pow(movedY, 2))
    color = "white"
    circle(mouseX, mouseY, r, color)


setIcon("icono.png")
setTitle("Figuras primitivas")

while ejecutando:
    draw()
    update()

exit()
