import unittest
import Engine
Engine.init()
from Engine.Camera import Camera
import numpy


class HashMapTests(unittest.TestCase):

    epsilon = 10

    def test_singular(self):
        cam = Camera(numpy.array([0,0]), 20, 20)
        print(cam)
