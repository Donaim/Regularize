
import unittest
import pprint
import time

pp = pprint.PrettyPrinter()
def pprint(obj): pp.pprint(obj)

import window
import ui
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
        print('loop ended')

    def test_second_init(self):
        window.show()
        print('second loop started')

        ma = window.create_random_colorized_map()
        window.update_map(ma, False)

        imp = input()
        window.close()
    def test_open_file(self):
        window.show()

        fname = ui.create_temp()
        file  = ui.open_file('/usr/bin/gedit', fname)

        def check(): return file.returncode is None
        def callback(): updater.update_window(fname)

        ui.listen_file_sync(fname, check, callback)

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

