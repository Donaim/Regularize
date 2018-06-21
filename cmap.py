import random

CELL_W = 10
CELL_H = 10

def create_random_map():
    re = []
    for x in range(0, CELL_W):
        row = []
        for y in range(0, CELL_H):
            row.append(random.choice([True, False]))
        re.append(row)
    return re
def create_empty_map():
    re = []
    for x in range(0, CELL_W):
        row = []
        for y in range(0, CELL_H):
            row.append(False)
        re.append(row)
    return re
def bool_map_to_text(arr: list) -> str:
    if len(arr) != CELL_W:
        raise Exception('Wrong width {}, has to be {}'.format(len(arr), CELL_W))
    
    re = ''
    for x in range(0, CELL_W):
        if len(arr[x]) != CELL_H:
            raise Exception('Wrong height {}, has to be {}'.format(len(arr[x]), CELL_H))
        for y in range(0, CELL_H):
            re += '1' if arr[x][y] else '0'
    return re
def text_to_bool_map(text: str) -> list:
    if len(text) != CELL_H * CELL_W:
        raise Exception('Wrong text size {}, has to be {}'.format(len(text), CELL_H * CELL_W))

    re = []
    for x in range(0, CELL_W):
        row = []
        for y in range(0, CELL_H):
            b = text[x * CELL_H + y] != '0'
            row.append(b)
        re.append(row)
    return re

