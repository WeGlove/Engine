from abc import abstractmethod
from src.GameObjects.GameObject import GameObject


class Simple(GameObject):

    def __init__(self, identifier=-1):
        GameObject.__init__(self, identifier)

    @abstractmethod
    def intersect(self, ray):
        pass

    @abstractmethod
    def is_in(self, point):
        pass

    @abstractmethod
    def get_bounding_box(self):
        pass

    @abstractmethod
    def get_at(self, point):
        pass