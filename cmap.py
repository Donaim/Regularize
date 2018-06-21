import random

CELL_W = 3
CELL_H = 3

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
def equal_q(a: list, b: list) -> bool:
    if len(a) != len(b): 
        # print('wrong sizes: {} x {}'.format(len(a), len(b)))
        return False
    
    for x in range(len(a)):
        if len(a[x]) != len(b[x]): 
            # print('wrong sizes at {} : {} x {}'.format(x, len(a[x]), len(b[x])))
            return False
        for y in range(len(a[x])):
            if a[x][y] != b[x][y]: 
                # print('not equal at [{}][{}] : {} x {}'.format(x, y, a[x][y], b[x][y]))
                return False
    
    return True
