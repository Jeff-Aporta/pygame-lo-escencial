
import random
import datetime
import time
import pygame.gfxdraw
import pygame
import math

import os.path  # para verificar la existencia de un archivo
import urllib.request  # para descargarlo de internet

# funciones de proyecto

Imagen = None


def setup():
    setIcon("icono.png", "https://i.ibb.co/TRcFN4j/icono.png")
    setTitle("Pong solitario")
    setSize(600, 400, False)
    global Imagen
    Imagen = loadImage("img prueba.png", "https://i.ibb.co/GVLFSxH/00.png")


def draw():
    background("black")
    canvas.blit(Imagen, [mouseX, mouseY])

# IO


def loadImage(filename, url=None):
    if(url != None):
        if(not location_exists(filename)):
            download(filename, url)
    return pygame.image.load(filename)


def location_exists(filename):
    return os.path.exists(filename)


def download(filename, url):
    try:
        urllib.request.urlretrieve(url, filename)
        print("Archivo descargado " + url + " en " + filename)
    except:
        print("No se pudo descargar el archivo " + url)

# Variables de entorno y de control


ejecutando = True
frameRate = 60
frameCount = 0
width = 0
height = 0
centerX = 0
centerY = 0
mouseX = 0
mouseY = 0
pmouseX = 0
pmouseY = 0
movedX = 0
movedY = 0

pygame.init()

canvas = None

# funciones de personalización


def setIcon(ruta, url=None):
    try:
        pygame.display.set_icon(loadImage(ruta, url))
    except:
        pass


def setTitle(title):
    pygame.display.set_caption(title)


def setSize(w, h, resizable=True):
    global canvas, width, height, centerX, centerY
    width = w
    height = h
    centerX = width/2
    centerY = height/2
    if(resizable):
        canvas = pygame.display.set_mode([width, height], pygame.RESIZABLE)
    else:
        canvas = pygame.display.set_mode([width, height])


# control de eventos

def mouseEvents(event):
    if(event.type == pygame.MOUSEBUTTONDOWN):
        try:
            mousePressed(event)
        except:
            pass
    if(event.type == pygame.MOUSEBUTTONUP):
        try:
            mouseReleased(event)
        except:
            pass
    if(event.type == pygame.MOUSEMOTION):
        try:
            mouseDragged(event)
        except:
            pass


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
        mouseEvents(event)


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


def constrain(v, vmin, vmax):
    if(v < vmin):
        return vmin
    if(v > vmax):
        return vmax
    return v


def outside(v, vmin, vmax):
    return v < vmin or v > vmax

def randomize(start=None, stop=None):
    if(start!=None and stop!=None):
        return (stop-start)*random.random()+start
    if(start!=None):
        return random.random()*start
    return random.random()

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
    return pygame.Rect(x, y, w, h)


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
    return pygame.Rect(x-r, y-r, 2*r, 2*r)

# looping y protocolo de ejecución


setup()

while ejecutando:
    draw()
    update()

exit()
