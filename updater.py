
import window
import importlib
import sys
import os
import cmap

module = None
def load_module(path: str) -> module:
    d = os.path.dirname(path)
    name = os.path.basename(path)
    name = '.'.join( name.split('.')[:-1] )

    if not d is None:
        sys.path.append(d)
    
    global module
    if module is None:
        module = importlib.import_module(name)
    else:
        module = importlib.reload(module)

    if not d is None:
        sys.path.remove(d)
    
    return module

def load_map(fname: str):
    try:
        m = load_module(fname)
        if len(m.reg) != cmap.CELL_W or (any(map(lambda x: len(x) != cmap.CELL_H, m.reg))):
            raise Exception('Wrong dimensions of reg. Have to be {}x{}'.format(cmap.CELL_W, cmap.CELL_H))
        return m.reg
    except Exception as e:
        print('error:', e)
        return None
def update_right_map(bma):
    global right_bmap
    global right_map

    right_bmap = bma
    right_map = window.colorize_bool_map(right_bmap)
    window.update_map(right_map, True)

left_bmap = None
left_map = None
right_bmap = None
right_map = None

def init_maps():
    global left_bmap
    global left_map
    global right_bmap
    global right_map
    
    left_bmap = cmap.create_random_map()
    left_map = window.colorize_bool_map(left_bmap)
    right_bmap = cmap.create_empty_map()
    right_map = window.colorize_bool_map(right_bmap)

def update_maps():
    window.update_map(left_map, False)
    window.update_map(right_map, True)

