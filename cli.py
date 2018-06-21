import window
import file_manager
import cmap
import updater

class Parser:

    def __init__(self):
        self._forse_exit = False
        self._current_map = None

    def reload(self):
        print('reloading...')

        self._current_bmap = cmap.create_random_map()
        self._current_map = window.colorize_bool_map(self._current_bmap)
        window.update_map(self._current_map, False)

        print('reloaded!')
    def save(self):
        print('saving...')
        raise NotImplementedError()
        print('saved')

    def _parse_loop(self):
        
        funcs = filter(lambda name: name[0] != '_', dir(self))
        funcs = dict(map(lambda name: (name, getattr(self, name)), funcs))
        # print('vars=', funcs)
        
        while True:
            c = input('command=')

            if c == 'exit':
                self._forse_exit = True
                return
            elif c in funcs:
                funcs[c]()


