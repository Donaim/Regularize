
import unittest
import pprint
import time

pp = pprint.PrettyPrinter()
def pprint(obj): pp.pprint(obj)

import window
import file_manager
import cmap
import updater

class TestC1(unittest.TestCase):

    def test_random(self):
        import random
        print(random.randint(1, 10))

    def test_random_map(self):
        window.show()

        ma = window.create_random_colorized_map()
        window.update_map(ma, False)

        inp = input()
        window.close()

    def test_second_init(self):
        window.show()

        ma = window.create_random_colorized_map()
        window.update_map(ma, False)

        inp = input()
        window.close()

        window.show()

        ma = window.create_random_colorized_map()
        window.update_map(ma, False)

        imp = input()
        window.close()

    def test_map_convertions(self):
        ma = window.create_random_colorized_map()
        pprint(ma)

        bma = window.uncolorize_map(ma)
        pprint(bma)

        tma = cmap.bool_map_to_text(bma)
        pprint(tma)

        bma2 = cmap.text_to_bool_map(tma)
        pprint(bma2)

        ma2 = window.colorize_bool_map(bma2)
        pprint(ma2)

        for x in range(len(ma)):
            for y in range(len(ma[x])):
                if ma[x][y] != ma2[x][y]: raise Exception('map convertions are bad: {} != {}'.format(ma[x][y], ma2[x][y]))
        print('map convertions passed')

    def test_open_file(self):
        window.show()

        fname = file_manager.create_temp()
        file  = file_manager.open_file('/usr/bin/gedit', fname)

        def check(): return file.returncode is None
        def callback(): updater.update_window(fname)

        file_manager.listen_file_sync(fname, check, callback)
        window.close()
