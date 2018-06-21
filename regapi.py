import window
import cmap

reg = cmap.create_empty_map()

def finish():
    text = window.bool_map_to_text(reg)
    with open('/tmp/tmp_regularize', 'w+') as o:
        o.write(text)
    exit(0)



