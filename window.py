import pygame 
from threading import Thread
from cmap import *

RED = (255, 0, 0)
BLUE = (0, 0, 255)
CELL_SIZE = 30

windowSurface = None
clock = pygame.time.Clock()

def draw_cell(color : (int, int, int), x, y):
    pygame.draw.rect(windowSurface, color, (CELL_SIZE * x, CELL_SIZE * y, CELL_SIZE, CELL_SIZE))

def update_map(m : list):
    for x in range(0, len(m)):
        for y in range(0, len(m[0])):
            draw_cell(m[x][y], x, y)
    pygame.display.update()

running = False
def game_loop():
    global running
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                running = False
                return
        clock.tick(60)
def show():
    global running
    if (running):
        raise Exception("already started")
    else: 
        running = True

    global windowSurface
    pygame.init()
    windowSurface = pygame.display.set_mode((CELL_SIZE * CELL_W, CELL_SIZE * CELL_H))
    
    loop_th = Thread(target=game_loop)
    loop_th.start()
def close():
    global running
    running = False
    pygame.quit()

def create_random_colorized_map():
    return colorize_bool_map( create_random_map() )
def colorize_bool_map(arr: list):
    if len(arr) != CELL_W:
        raise Exception('Wrong width {}, has to be {}'.format(len(arr), CELL_W))

    re = []
    for x in range(0, CELL_W):
        if len(arr[x]) != CELL_H:
            raise Exception('Wrong height {}, has to be {}'.format(len(arr[x]), CELL_H))

        row = []
        for y in range(0, CELL_H):
            row.append(RED if arr[x][y] else BLUE)
        re.append(row)
    return re
def uncolorize_map(arr: list) -> list:
    if len(arr) != CELL_W:
        raise Exception('Wrong width {}, has to be {}'.format(len(arr), CELL_W))

    re = []
    for x in range(0, CELL_W):
        if len(arr[x]) != CELL_H:
            raise Exception('Wrong height {}, has to be {}'.format(len(arr[x]), CELL_H))

        row = []
        for y in range(0, CELL_H):
            row.append(True if arr[x][y] == RED else False)
        re.append(row)
    return re