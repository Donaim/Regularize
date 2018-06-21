import window
import cmap

reg = cmap.create_empty_map()

def finish():
    text = window.bool_map_to_text(reg)
    with open('out.txt', 'w+') as o:
        o.write(text)
    exit(0)



