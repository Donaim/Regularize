import window
import file_manager
import cmap
import updater


class Parser:

    def __init__(self):
        self._forse_exit = False

    def reload(self):
        print('reloading...')

        updater.init_maps()
        updater.update_maps()

        print('reloaded!')
    def save(self):
        print('saving...')
        raise NotImplementedError()
        print('saved')
    def change_width(self):
        args = self._parse_arguments(1)
        new_width = int(args[0])
        cmap.CELL_W = new_width
        cmap.CELL_H = new_width
        window.resize()
        self.reload()

    def _parse_arguments(self, expected_num: int) -> list:
        sp = self._command.split()
        if len(sp) < expected_num + 1:
            print('expected {} arguments but {} were given'.format(expected_num, len(sp) - 1))
            return None
        return sp[1:]
    def _parse_loop(self):
        
        funcs = filter(lambda name: name[0] != '_', dir(self))
        funcs = dict(map(lambda name: (name, getattr(self, name)), funcs))
        # print('vars=', funcs)
        
        while True:
            self._command = input('command=')
            func = self._command.split()[0]

            if func == 'exit':
                self._forse_exit = True
                return
            elif func in funcs:
                funcs[func]()
            else:
                print('command "{}" not found. available={}'.format(func, list(funcs.keys())))

