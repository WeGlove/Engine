from src.Shapes.FinitelyBounded.ShapeCollections.Std.Simple import Simple
from abc import abstractmethod


class Group(Simple):

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
