import Shapes
from Shapes.FinitelyBounded.Factories.StdFactory import StdFactroy
Shapes.set_factory(StdFactroy)
import unittest
import numpy


class LATests(unittest.TestCase):

    epsilon = 10

    def test_singular(self):
        Shapes.factory.get_LA([StdFactroy.get_AABB(numpy.array([0,0]), 10, 10, identifier=1)])

    def test_leaf_insert(self):
        Shapes.factory.get_LA([StdFactroy.get_AABB(numpy.array([0,0]), 10, 10, identifier=i) for i in range(Shapes.factory.get_LA.FILL)])

    def test_split_insert(self):
        Shapes.factory.get_LA([StdFactroy.get_AABB(numpy.array([0, 0]), 10, 10, identifier=i) for i in range(Shapes.factory.get_LA.FILL+1)])

    def test_split_insert_p1(self):
        Shapes.factory.get_LA([StdFactroy.get_AABB(numpy.array([0, 0]), 10, 10, identifier=i) for i in range(Shapes.factory.get_LA.FILL+2)])

