
import math
import datetime
import time
import sys
import pygame.gfxdraw
import pygame

# funciones de proyecto

x = 0
y = 0
dx = 0
dy = 0


def setup():
    setIcon("icono.png")
    setTitle("Título personalizado")
    global x, y
    x = width/2
    y = height/2

def draw():
    global x, y
    background("skyblue")
    color = "white"
    circle(x, y, 50, color)
    x+=dx
    y+=dy

def keyPressed(event):
    global dx, dy
    if(event.key == pygame.K_RIGHT):
        dx = 1
    if(event.key == pygame.K_LEFT):
        dx = -1
    if(event.key == pygame.K_UP):
        dy = -1
    if(event.key == pygame.K_DOWN):
        dy = 1

def keyReleased(event):
    global dx, dy
    if(event.key == pygame.K_RIGHT):
        dx = 0
    if(event.key == pygame.K_LEFT):
        dx = 0
    if(event.key == pygame.K_UP):
        dy = 0
    if(event.key == pygame.K_DOWN):
        dy = 0

def windowClosing():
    print("Hasta pronto...")

def windowResizing(event):
    global x, y
    x = event.w/2
    y = event.h/2

# Variables de entorno y de control

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

# funciones de personalización


def setIcon(ruta):
    try:
        icon = pygame.image.load(ruta)
        pygame.display.set_icon(icon)
    except:
        pass


def setTitle(title):
    pygame.display.set_caption(title)


# control de eventos

def keyEvents(event):
    if event.type == pygame.KEYDOWN:
        try:
            keyPressed(event)
        except:
            pass
    if event.type == pygame.KEYUP:
        try:
            keyReleased(event)
        except:
            pass

def windowEvent(event):
    if event.type == pygame.VIDEORESIZE:
        try:
            windowResizing(event)
        except:
            pass
    if event.type == pygame.QUIT:
            try:
                windowClosing()
            except:
                pass
            global ejecutando
            ejecutando = False

def events():
    for event in pygame.event.get():
        windowEvent(event)
        keyEvents(event)


# funciones de actualización

def updateVariables():
    global width
    global height
    global mouseX
    global mouseY
    global pmouseX
    global pmouseY
    global movedX
    global movedY
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
    pygame.display.flip()
    time.sleep(1/frameRate)
    global frameCount
    frameCount += 1


def update():
    updateVariables()
    events()
    updateFrame()

# funciones y variables matematicas


PI = math.pi


def cos(theta):
    return math.cos(theta)


def sin(theta):
    return math.sin(theta)

# funciones de tiempo


def now():
    return datetime.datetime.now()


def second():
    return now().second


def minute():
    return now().minute


def hour():
    return now().hour

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


def line(x1, y1, x2, y2, color="black", weight=1):
    if(weight == 0):
        return
    if weight == 1 and len(color) == 4 and (type(color) == tuple or type(color) == list):
        pygame.gfxdraw.line(canvas, x1, y1, x2, y2, color)
    else:
        if(weight == 1):
            pygame.draw.aaline(canvas, color, (x1, y1), (x2, y2))
        else:
            pygame.draw.line(canvas, color, (x1, y1), (x2, y2), weight)


def circle(x, y, r, color):
    if(len(color) == 4 and (type(color) == tuple or type(color) == list)):
        pygame.gfxdraw.filled_circle(canvas, x, y, r, color)
    else:
        pygame.draw.circle(canvas, color, (x, y), r)

# looping y protocolo de ejecución


setup()

while ejecutando:
    draw()
    update()

sys.exit()
