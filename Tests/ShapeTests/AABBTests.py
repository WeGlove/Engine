import Shapes
from Shapes.FinitelyBounded.Factories.StdFactory import StdFactroy
Shapes.set_factory(StdFactroy)
import unittest
import numpy

class AABBTests(unittest.TestCase):

    epsilon = 10

    def test_combine(self):
        boxA = StdFactroy.get_AABB(numpy.array([-5,-5]), 10, 10)
        boxB = StdFactroy.get_AABB(numpy.array([5,5]), 10, 10)

        box = boxA.combine([boxA, boxB])
        self.assertAlmostEqual(box.width, 20, self.epsilon, f"Expected width 10, got {box.width}")
        self.assertAlmostEqual(box.height, 20, self.epsilon, f"Expected width 10, got {box.height}")

    def test_combine_empty(self):
        emptyA = StdFactroy.get_AABB.empty()
        emptyB = StdFactroy.get_AABB.empty()

        box = emptyA.combine([emptyA, emptyB])
        self.assertTrue(box.empty, f"Expected True, got {box.empty}")
