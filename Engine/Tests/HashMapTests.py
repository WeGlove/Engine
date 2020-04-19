import unittest
from Engine.GameObjectHashMap import GameObjectHashMap


class HashMapTests(unittest.TestCase):

    epsilon = 10

    def test_singular(self):
        hmap = GameObjectHashMap()
        hmap = [hmap.getNextID() for _ in range(100)]
        print(hmap)