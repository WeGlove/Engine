from Engine.Shapes.FinitelyBounded.Factories.StdFactory import StdFactroy
import Engine
Engine.shape_factory = StdFactroy()
import unittest
import numpy
from Engine.Ray import Ray


class LA(unittest.TestCase):

    epsilon = 10

    def test_case_1(self):
        shapes = [
            Engine.shape_factory.AAB(numpy.array([16, 17]), 10, 2, 3),
            Engine.shape_factory.AAB(numpy.array([13, 21]), 10, 2, 4),
            Engine.shape_factory.AAB(numpy.array([25, 17]), 10, 2, 5),
            Engine.shape_factory.AAB(numpy.array([79, 59]), 10, 2, 6),
            Engine.shape_factory.AAB(numpy.array([60, 71]), 10, 2, 7),
            Engine.shape_factory.AAB(numpy.array([44, 73]), 10, 2, 8),
            Engine.shape_factory.AAB(numpy.array([11, 83]), 10, 2, 9),
            Engine.shape_factory.AAB(numpy.array([2, 62]), 10, 2, 10),
            Engine.shape_factory.AAB(numpy.array([9, 38]), 10, 2, 11),
            Engine.shape_factory.AAB(numpy.array([41, 7]), 10, 2, 12),
            Engine.shape_factory.AAB(numpy.array([99, 44]), 10, 2, 13),
            Engine.shape_factory.AAB(numpy.array([89, 66]), 10, 2, 14),
            Engine.shape_factory.AAB(numpy.array([74, 76]), 10, 2, 15),
            Engine.shape_factory.AAB(numpy.array([26, 76]), 10, 2, 16),
            Engine.shape_factory.AAB(numpy.array([34, 73]), 10, 2, 17),
            Engine.shape_factory.AAB(numpy.array([13, 77]), 10, 2, 18),
            Engine.shape_factory.AAB(numpy.array([33, 71]), 10, 2, 19),
            Engine.shape_factory.AAB(numpy.array([50, 69]), 10, 2, 20),
            Engine.shape_factory.AAB(numpy.array([46, 83]), 10, 2, 21),
            Engine.shape_factory.AAB(numpy.array([20, 71]), 10, 2, 22),
            Engine.shape_factory.AAB(numpy.array([44, 68]), 10, 2, 23),
            Engine.shape_factory.AAB(numpy.array([63, 66]), 10, 2, 24),
            Engine.shape_factory.AAB(numpy.array([75, 20]), 10, 2, 25),
            Engine.shape_factory.AAB(numpy.array([83, 22]), 10, 2, 26),
            Engine.shape_factory.AAB(numpy.array([79, 24]), 10, 2, 27),
            Engine.shape_factory.AAB(numpy.array([38, 47]), 10, 2, 28)
        ]
        tree = Engine.shape_factory.LeastAddition(shapes)
        ray = Ray(numpy.array([16,52]), numpy.array([1,1]), error=2)
        tree_intersections = tree.intersect(ray)
        group_intersections = []
        for shape in shapes:
            group_intersections += shape.intersect(ray)
        self.assertTrue(len(tree_intersections) == len(group_intersections),
                        f"Expected equal number of intersections for both structures. Got, tree: {len(tree_intersections)} group: {len(group_intersections)}")

    def test_case_2(self):
        shapes = [
            Engine.shape_factory.AABB(numpy.array([16, 17]), 10, 2, False, 3),
            Engine.shape_factory.AABB(numpy.array([13, 21]), 10, 2, False, 4),
            Engine.shape_factory.AABB(numpy.array([25, 17]), 10, 2, False, 5),
            Engine.shape_factory.AABB(numpy.array([79, 59]), 10, 2, False, 6),
            Engine.shape_factory.AABB(numpy.array([60, 71]), 10, 2, False, 7),
            Engine.shape_factory.AABB(numpy.array([44, 73]), 10, 2, False, 8),
            Engine.shape_factory.AABB(numpy.array([11, 83]), 10, 2, False, 9),
            Engine.shape_factory.AABB(numpy.array([2, 62]), 10, 2, False, 10),
            Engine.shape_factory.AABB(numpy.array([9, 38]), 10, 2, False, 11),
            Engine.shape_factory.AABB(numpy.array([41, 7]), 10, 2, False, 12),
            Engine.shape_factory.AABB(numpy.array([99, 44]), 10, 2, False, 13),
            Engine.shape_factory.AABB(numpy.array([89, 66]), 10, 2, False, 14),
            Engine.shape_factory.AABB(numpy.array([74, 76]), 10, 2, False, 15),
            Engine.shape_factory.AABB(numpy.array([26, 76]), 10, 2, False, 16),
            Engine.shape_factory.AABB(numpy.array([34, 73]), 10, 2, False, 17),
            Engine.shape_factory.AABB(numpy.array([13, 77]), 10, 2, False, 18),
            Engine.shape_factory.AABB(numpy.array([33, 71]), 10, 2, False, 19),
            Engine.shape_factory.AABB(numpy.array([50, 69]), 10, 2, False, 20),
            Engine.shape_factory.AABB(numpy.array([46, 83]), 10, 2, False, 21),
            Engine.shape_factory.AABB(numpy.array([20, 71]), 10, 2, False, 22),
            Engine.shape_factory.AABB(numpy.array([44, 68]), 10, 2, False, 23),
            Engine.shape_factory.AABB(numpy.array([63, 66]), 10, 2, False, 24),
            Engine.shape_factory.AABB(numpy.array([75, 20]), 10, 2, False, 25),
            Engine.shape_factory.AABB(numpy.array([83, 22]), 10, 2, False, 26),
            Engine.shape_factory.AABB(numpy.array([79, 24]), 10, 2, False, 27),
            Engine.shape_factory.AABB(numpy.array([38, 47]), 10, 2, False, 28)
        ]
        empty = Engine.shape_factory.AABB.empty()
        for shape in shapes:
            empty.extend([shape])
        pass

    def test_case_3(self):
        shapes = [
            Engine.shape_factory.AAB(numpy.array([16, 17]), 10, 2, 3),
            Engine.shape_factory.AAB(numpy.array([13, 21]), 10, 2, 4),
            Engine.shape_factory.AAB(numpy.array([25, 17]), 10, 2, 5),
            Engine.shape_factory.AAB(numpy.array([79, 59]), 10, 2, 6),
            Engine.shape_factory.AAB(numpy.array([60, 71]), 10, 2, 7),
            Engine.shape_factory.AAB(numpy.array([44, 73]), 10, 2, 8),
            Engine.shape_factory.AAB(numpy.array([11, 83]), 10, 2, 9),
            Engine.shape_factory.AAB(numpy.array([2, 62]), 10, 2, 10),
            Engine.shape_factory.AAB(numpy.array([9, 38]), 10, 2, 11),
            Engine.shape_factory.AAB(numpy.array([41, 7]), 10, 2, 12),
            Engine.shape_factory.AAB(numpy.array([99, 44]), 10, 2, 13),
            Engine.shape_factory.AAB(numpy.array([89, 66]), 10, 2, 14),
            Engine.shape_factory.AAB(numpy.array([74, 76]), 10, 2, 15),
            Engine.shape_factory.AAB(numpy.array([26, 76]), 10, 2, 16),
            Engine.shape_factory.AAB(numpy.array([34, 73]), 10, 2, 17),
            Engine.shape_factory.AAB(numpy.array([13, 77]), 10, 2, 18),
            Engine.shape_factory.AAB(numpy.array([33, 71]), 10, 2, 19),
            Engine.shape_factory.AAB(numpy.array([50, 69]), 10, 2, 20),
            Engine.shape_factory.AAB(numpy.array([46, 83]), 10, 2, 21),
            Engine.shape_factory.AAB(numpy.array([20, 71]), 10, 2, 22),
            Engine.shape_factory.AAB(numpy.array([44, 68]), 10, 2, 23),
            Engine.shape_factory.AAB(numpy.array([63, 66]), 10, 2, 24),
            Engine.shape_factory.AAB(numpy.array([75, 20]), 10, 2, 25),
            Engine.shape_factory.AAB(numpy.array([83, 22]), 10, 2, 26),
            Engine.shape_factory.AAB(numpy.array([79, 24]), 10, 2, 27),
            Engine.shape_factory.AAB(numpy.array([38, 47]), 10, 2, 28)
        ]
        tree = Engine.shape_factory.LeastAddition(shapes)
        tree.delete(23)
        shape = Engine.shape_factory.AAB(numpy.array([44, 68]), 10, 2, 23)
        overlaps = tree.overlaps(shape.get_bounding_box())
        for overlap in overlaps:
            self.assertTrue(shape.get_bounding_box().overlaps(shape.get_bounding_box(), overlap.get_bounding_box()))

    def test_case_4(self):
        shapes = [
            Engine.shape_factory.AAB(numpy.array([16, 17]), 10, 2, 3),
            Engine.shape_factory.AAB(numpy.array([13, 21]), 10, 2, 4),
            Engine.shape_factory.AAB(numpy.array([25, 17]), 10, 2, 5),
            Engine.shape_factory.AAB(numpy.array([79, 59]), 10, 2, 6),
            Engine.shape_factory.AAB(numpy.array([60, 71]), 10, 2, 7),
            Engine.shape_factory.AAB(numpy.array([44, 73]), 10, 2, 8),
            Engine.shape_factory.AAB(numpy.array([11, 83]), 10, 2, 9),
            Engine.shape_factory.AAB(numpy.array([2, 62]), 10, 2, 10),
            Engine.shape_factory.AAB(numpy.array([9, 38]), 10, 2, 11),
            Engine.shape_factory.AAB(numpy.array([41, 7]), 10, 2, 12),
            Engine.shape_factory.AAB(numpy.array([99, 44]), 10, 2, 13),
            Engine.shape_factory.AAB(numpy.array([89, 66]), 10, 2, 14),
            Engine.shape_factory.AAB(numpy.array([74, 76]), 10, 2, 15),
            Engine.shape_factory.AAB(numpy.array([26, 76]), 10, 2, 16),
            Engine.shape_factory.AAB(numpy.array([34, 73]), 10, 2, 17),
            Engine.shape_factory.AAB(numpy.array([13, 77]), 10, 2, 18),
            Engine.shape_factory.AAB(numpy.array([33, 71]), 10, 2, 19),
            Engine.shape_factory.AAB(numpy.array([50, 69]), 10, 2, 20),
            Engine.shape_factory.AAB(numpy.array([46, 83]), 10, 2, 21),
            Engine.shape_factory.AAB(numpy.array([20, 71]), 10, 2, 22),
            Engine.shape_factory.AAB(numpy.array([44, 68]), 10, 2, 23),
            Engine.shape_factory.AAB(numpy.array([63, 66]), 10, 2, 24),
            Engine.shape_factory.AAB(numpy.array([75, 20]), 10, 2, 25),
            Engine.shape_factory.AAB(numpy.array([83, 22]), 10, 2, 26),
            Engine.shape_factory.AAB(numpy.array([79, 24]), 10, 2, 27),
            Engine.shape_factory.AAB(numpy.array([38, 47]), 10, 2, 28)
        ]
        tree = Engine.shape_factory.LeastAddition(shapes)
        tree.delete(19)
        tree.delete(23)
        ray = Ray(numpy.array([89.66666667, 25.33333333]), numpy.array([1, -1]), error=2)
        tree_intersections = tree.intersect(ray)
        group_intersections = []
        for shape in shapes:
            if not shape.identifier ==  19 and not shape.identifier == 23:
                group_intersections += shape.intersect(ray)
        self.assertTrue(len(tree_intersections) == len(group_intersections),
                        f"Expected equal number of intersections for both structures. Got, tree: {len(tree_intersections)} group: {len(group_intersections)}")

