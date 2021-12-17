
import pygame
import time

ejecutando = True
frameRate = 60
frameCount = 0
width = 600
height = 400
pmouseX = 0
pmouseY = 0
mouseX = 0
mouseY = 0
movedX = 0
movedY = 0

pygame.init()

canvas = pygame.display.set_mode([width, height], pygame.RESIZABLE)


def setIcon(ruta):
    try:
        Icon = pygame.image.load(ruta)
        pygame.display.set_icon(Icon)
    except:
        pass


def setTitle(Title):
    pygame.display.set_caption(Title)


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global ejecutando
            ejecutando = False


def updateVariables():
    global frameCount
    global width, height
    global mouseX, mouseY
    global pmouseX, pmouseY
    global movedX, movedY
    sz = pygame.display.get_window_size()
    width = sz[0]
    height = sz[1]
    mp = pygame.mouse.get_pos()
    pmouseX = mouseX
    pmouseY = mouseY
    mouseX = mp[0]
    mouseY = mp[1]
    movedX = mouseX-pmouseX
    movedY = mouseY-pmouseY


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


def rect(x, y, w, h, color):
    pygame.draw.rect(canvas, color, [x, y, w, h])


def draw():
    background("skyblue")
    rect(mouseX, mouseY, 100, 100, "white")


setIcon("icono.png")
setTitle("Variables de entorno")

while ejecutando:
    draw()
    print((mouseX, mouseY))
    update()

exit()
