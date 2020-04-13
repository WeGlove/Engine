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

    def test_combine_empty_empty(self):
        emptyA = StdFactroy.get_AABB.empty()
        emptyB = StdFactroy.get_AABB.empty()

        box = emptyA.combine([emptyA, emptyB])
        self.assertTrue(box.empty, f"Expected True, got {box.empty}")

    def test_combine_empty_full(self):
        boxA = StdFactroy.get_AABB(numpy.array([10, 10]), 10, 10)
        boxB = StdFactroy.get_AABB.empty()

        box = boxA.combine([boxA, boxB])
        self.assertAlmostEqual(box.width, 10, self.epsilon, f"Expected width 10, got {box.width}")
        self.assertAlmostEqual(box.height, 10, self.epsilon, f"Expected width 10, got {box.height}")
        self.assertEqual(box.position[0], 10, f"Expected 10 got {box.position[0]}")
        self.assertEqual(box.position[1], 10, f"Expected 10 got {box.position[1]}")

    def test_combine_copmlex(self):
        boxA = StdFactroy.get_AABB(numpy.array([0,0]), 2, 10)
        boxB = StdFactroy.get_AABB(numpy.array([0,0]), 10, 2)

        box = boxA.combine([boxA, boxB])
        self.assertAlmostEqual(box.width, 10, self.epsilon, f"Expected width 10, got {box.width}")
        self.assertAlmostEqual(box.height, 10, self.epsilon, f"Expected width 10, got {box.height}")
        self.assertEqual(box.position[0], 0, f"Expected 0 got {box.position[0]}")
        self.assertEqual(box.position[1], 0, f"Expected 0 got {box.position[1]}")

    def test_overlap_euqal(self):
        boxA = StdFactroy.get_AABB(numpy.array([0,0]), 10, 10)
        boxB = StdFactroy.get_AABB(numpy.array([0,0]), 10, 10)

        box = boxA.overlap(boxA, boxB)

        self.assertAlmostEqual(box.width, 10, self.epsilon, f"Expected width 10, got {box.width}")
        self.assertAlmostEqual(box.height, 10, self.epsilon, f"Expected width 10, got {box.height}")
        self.assertEqual(box.position[0], 0, f"Expected 0 got {box.position[0]}")
        self.assertEqual(box.position[1], 0, f"Expected 0 got {box.position[1]}")

    def test_line_overlap_equal(self):
        lineA = numpy.array([0, 1])
        lineB = numpy.array([0, 1])

        line = Shapes.factory.get_AABB.line_overlap(lineA, lineB)
        self.assertEqual(line[0], 0, f"Expected 0 got {line[0]}")
        self.assertEqual(line[1], 1, f"Expected 0 got {line[1]}")
