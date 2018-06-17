
import unittest
import pprint
import time

pp = pprint.PrettyPrinter()
def pprint(obj): pp.pprint(obj)

import window

class TestC1(unittest.TestCase):

    def test_random(self):
        import random
        print(random.randint(1, 10))

    def test_random_map(self):
        window.show()

        ma = window.create_random_map()
        window.update_map(ma)

        inp = input()
        window.close()
        print('loop ended')

    def test_second_init(self):
        window.show()
        print('second loop started')

        ma = window.create_random_map()
        window.update_map(ma)

        imp = input()
        window.close()

