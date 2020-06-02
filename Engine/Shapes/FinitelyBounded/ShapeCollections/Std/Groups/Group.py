from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Shape import Shape
from abc import abstractmethod


class Group(Shape):

    def __init__(self, identifier=-1):
        Simple.__init__(self, identifier)

    @abstractmethod
    def is_leaf(self):
        pass

    @abstractmethod
    def is_head(self):
        pass

    @abstractmethod
    def add(self, node):
        pass

    @abstractmethod
    def delete(self, identifier):
        pass

    @abstractmethod
    def get_leaves(self):
        pass

    @abstractmethod
    def overlaps(self, bbox):
        pass
