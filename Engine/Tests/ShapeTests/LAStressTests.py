from Engine import Shapes
from Engine.Shapes.FinitelyBounded.Factories.StdFactory import StdFactroy
Shapes.set_factory(StdFactroy)
import unittest
import numpy
import time


class LAStressTests(unittest.TestCase):

    epsilon = 10

    def test_massive_equal(self):
        tree = Shapes.factory.get_LA([])
        objects = [StdFactroy.get_AABB(numpy.array([0,0]), 10, 10, identifier=i) for i in range(1000)]
        before = time.time()
        for obj in objects:
            tree.add(obj)
        elapsed_time = time.time() - before

        print(f"Elapsed time {elapsed_time}")

    def test_massive_row(self):
        tree = Shapes.factory.get_LA([])
        objects = [StdFactroy.get_AABB(numpy.array([i*11,i*11]), 10, 10, identifier=i) for i in range(1000)]
        before = time.time()
        for obj in objects:
            tree.add(obj)
        elapsed_time = time.time() - before

        print(f"Elapsed time {elapsed_time}")
