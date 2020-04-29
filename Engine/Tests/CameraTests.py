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

    def test_pos_0(self):
        cam = Camera(numpy.array([10, 10]), 20, 20)
        position = cam.world_to_cam(numpy.array([0,0]))
        self.assertEqual(0, position[0])
        self.assertEqual(0, position[1])

    def test_pos_1(self):
        cam = Camera(numpy.array([10, 10]), 20, 20)
        position = cam.world_to_cam(numpy.array([1,1]))
        self.assertEqual(1, position[0])
        self.assertEqual(1, position[1])

    def test_pos_0_scale(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, resolution_x=40, resolution_y=40)
        position = cam.world_to_cam(numpy.array([0,0]))
        self.assertEqual(0, position[0])
        self.assertEqual(0, position[1])

    def test_pos_1_scale(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, resolution_x=40, resolution_y=40)
        position = cam.world_to_cam(numpy.array([1,1]))
        self.assertEqual(2, position[0])
        self.assertEqual(2, position[1])

    def test_scalar(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, resolution_x=40, resolution_y=40)
        scalar = cam.world_to_cam_scale_x(1)
        self.assertEqual(2, scalar)