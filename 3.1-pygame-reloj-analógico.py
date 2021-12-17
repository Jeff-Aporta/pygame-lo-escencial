import math
import datetime
import time
import sys
import pygame.gfxdraw
import pygame

# funciones de proyecto

def setup():
    setIcon("icono.png")
    setTitle("Reloj Analógico")


def draw():
    background("skyblue")
    centerX = width/2
    centerY = height/2
    color = "white"
    circle(centerX, centerY, 170, color)
    color = "black"
    hora = hour() % 12
    minuto = minute()
    segundo = second()
    angulo_hora = 2*PI*hora/12 - PI/2
    angulo_minuto = 2*PI*minuto/60  - PI/2
    angulo_segundo = 2*PI*segundo/60  - PI/2
    line(
        centerX,
        centerY,
        centerX + 150*cos(angulo_segundo),
        centerY + 150*sin(angulo_segundo)
    )
    line(
        centerX,
        centerY,
        centerX + 150*cos(angulo_minuto),
        centerY + 150*sin(angulo_minuto),
        color,
        2
    )
    line(
        centerX,
        centerY,
        centerX + 120*cos(angulo_hora),
        centerY + 120*sin(angulo_hora),
        color,
        4
    )
    for i in range(60):
        theta = 2*PI*i/60
        r = 1
        if(i%5==0):
            r=2
        if(i%15==0):
            r=3
        circle(
            centerX + 160*cos(theta), 
            centerY + 160*sin(theta), 
            r, 
            color
        )


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

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global ejecutando
            ejecutando = False


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
    if(len(color) == 4 and type(color) != str):
        pygame.gfxdraw.box(canvas, (x, y, w, h), color)
    else:
        pygame.draw.rect(canvas, color, (x, y, w, h))


def drawRect(x, y, w, h, color="black", weight=1):
    if(weight == 0):
        return

    if(weight == 1 and len(color) == 4 and type(color) != str):
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
    if weight == 1 and len(color) == 4 and type(color) != str:
        pygame.gfxdraw.line(canvas, x1, y1, x2, y2, color)
    else:
        if(weight == 1):
            pygame.draw.aaline(canvas, color, (x1, y1), (x2, y2))
        else:
            pygame.draw.line(canvas, color, (x1, y1), (x2, y2), weight)


def circle(x, y, r, color):
    if(len(color) == 4 and type(color) != str):
        pygame.gfxdraw.filled_circle(canvas, x, y, r, color)
    else:
        pygame.draw.circle(canvas, color, (x, y), r)

# looping y protocolo de ejecución


setup()

while ejecutando:
    draw()
    update()

sys.exit()
