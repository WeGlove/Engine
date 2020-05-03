from Engine.Shapes.FinitelyBounded.Factories.StdFactory import StdFactroy
import Engine
Engine.shape_factory = StdFactroy()
import unittest
import numpy


class LATests(unittest.TestCase):

    epsilon = 10

    def test_singular(self):
        Engine.shape_factory.LeastAddition([Engine.shape_factory.AABB(numpy.array([0,0]), 10, 10, identifier=1)])

    def test_leaf_insert(self):
        Engine.shape_factory.LeastAddition([Engine.shape_factory.AABB(numpy.array([0,0]), 10, 10, identifier=i) for i in range(Engine.shape_factory.LeastAddition.FILL)])

    def test_split_insert(self):
        Engine.shape_factory.LeastAddition([StdFactroy.AABB(numpy.array([0, 0]), 10, 10, identifier=i) for i in range(Engine.shape_factory.LeastAddition.FILL+1)])

    def test_split_insert_p1(self):
        Engine.shape_factory.LeastAddition([StdFactroy.AABB(numpy.array([0, 0]), 10, 10, identifier=i) for i in range(Engine.shape_factory.LeastAddition.FILL+2)])

    def test_leaf_delete(self):
        LA = Engine.shape_factory.LeastAddition([StdFactroy.AABB(numpy.array([0, 0]), 10, 10, identifier=1)])
        LA.delete(1)
        self.assertEqual(0, len(LA.nodes), "Nodes not empty")

    def test_leaf_complex(self):
        LA = Engine.shape_factory.LeastAddition([StdFactroy.AABB(numpy.array([0, 0]), 10, 10, identifier=i) for i in range(Engine.shape_factory.LeastAddition.FILL+1)])
        LA.delete(Engine.shape_factory.LeastAddition.FILL)
        self.assertEqual(Engine.shape_factory.LeastAddition.FILL, len(LA.get_leaves()))

    def test_get_leaves(self):
        LA = Engine.shape_factory.LeastAddition([StdFactroy.AABB(numpy.array([0, 0]), 10, 10, identifier=i) for i in
                                    range(10)])
        for leaf in LA.get_leaves():
            print(leaf)


