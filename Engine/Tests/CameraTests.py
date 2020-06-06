import unittest
from Engine.Camera import Camera
import numpy


class CameraTests(unittest.TestCase):

    epsilon = 10

    def test_singular(self):
        cam = Camera(numpy.array([0,0]), 20, 20, 0)
        print(cam)

    def test_pos_0(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, 0)
        position = cam.world_to_cam(numpy.array([0,0]))
        self.assertEqual(0, position[0])
        self.assertEqual(0, position[1])

    def test_pos_1(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, 0)
        position = cam.world_to_cam(numpy.array([1,1]))
        self.assertEqual(1, position[0])
        self.assertEqual(1, position[1])

    def test_pos_0_scale(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, 0, resolution_x=40, resolution_y=40)
        position = cam.world_to_cam(numpy.array([0,0]))
        self.assertEqual(0, position[0])
        self.assertEqual(0, position[1])

    def test_pos_1_scale(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, 0, resolution_x=40, resolution_y=40)
        position = cam.world_to_cam(numpy.array([1,1]))
        self.assertEqual(2, position[0])
        self.assertEqual(2, position[1])

    def test_scalar(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, 0, resolution_x=40, resolution_y=40)
        scalar = cam.world_to_cam_scale_x(1)
        self.assertEqual(2, scalar)

    def test_cam_anchor_left_up(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, 0, anchor=(True, False))
        position = cam.world_to_cam(numpy.array([0, 0]))
        self.assertAlmostEqual(0, position[0], self.epsilon)
        self.assertAlmostEqual(20, position[1], self.epsilon)

    def test_cam_anchor_right_down(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, 0, anchor=(False, True))
        position = cam.world_to_cam(numpy.array([0, 0]))
        self.assertAlmostEqual(20, position[0], self.epsilon)
        self.assertAlmostEqual(0, position[1], self.epsilon)

    def test_cam_anchor_right_up(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, 0, anchor=(False, False))
        position = cam.world_to_cam(numpy.array([0, 0]))
        self.assertAlmostEqual(20, position[0], self.epsilon)
        self.assertAlmostEqual(20, position[1], self.epsilon)

    def test_cam_anchor_90(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, -90)
        position = cam.world_to_cam(numpy.array([0, 0]))
        self.assertAlmostEqual(20, position[0], self.epsilon)
        self.assertAlmostEqual(0, position[1], self.epsilon)

    def test_cam_anchor_180(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, -180)
        position = cam.world_to_cam(numpy.array([0, 0]))
        self.assertAlmostEqual(20, position[0], self.epsilon)
        self.assertAlmostEqual(20, position[1], self.epsilon)

    def test_cam_anchor_270(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, -270)
        position = cam.world_to_cam(numpy.array([0, 0]))
        self.assertAlmostEqual(0, position[0], self.epsilon)
        self.assertAlmostEqual(20, position[1], self.epsilon)

    def test_cam_back_90(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, -270)
        position = cam.world_to_cam(numpy.array([0, 0]))
        position = cam.cam_to_world(position)
        self.assertAlmostEqual(0, position[0], self.epsilon)
        self.assertAlmostEqual(0, position[1], self.epsilon)

    def test_cam_back_anchor_right_up(self):
        cam = Camera(numpy.array([10, 10]), 20, 20, 0, anchor=(False, False))
        position = cam.world_to_cam(numpy.array([0, 0]))
        position = cam.cam_to_world(position)
        self.assertAlmostEqual(0, position[0], self.epsilon)
        self.assertAlmostEqual(0, position[1], self.epsilon)

