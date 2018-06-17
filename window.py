import pygame 
from threading import Thread
import random

RED = (255, 0, 0)
BLUE = (0, 0, 255)
CELL_SIZE = 30
CELL_W = 10
CELL_H = 10

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

def create_random_map():
    re = []
    for x in range(0, CELL_W):
        row = []
        for y in range(0, CELL_H):
            row.append(random.choice([RED, BLUE]))
        re.append(row)
    return re



