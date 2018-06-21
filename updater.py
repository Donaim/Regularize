
import window
import importlib
import sys
import os

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
        return m.reg
    except Exception as e:
        print('error:', e)
        return None