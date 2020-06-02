from abc import abstractmethod
from Engine.GameObject import GameObject


class Shape(GameObject):
    """
    Ans abstract class for a bounded shape.
    """

    def __init__(self, identifier=-1):
        GameObject.__init__(self, identifier)

    @abstractmethod
    def intersect(self, ray):
        """
        Intersects the Shape with ray.
        Returns ALL intersections points.
        :param ray:
        :return:
        """
        pass

    @abstractmethod
    def is_in(self, point):
        """
        Checks whether point is in the Shape
        :param point:
        :return:
        """
        pass

    @abstractmethod
    def get_bounding_box(self):
        """
        Returns the smallest axis aligned bounding box (AABB) including the shape.
        :return:
        """
        pass

    @abstractmethod
    def get_at(self, point):
        """
        Returns a list of shapes that include point.
        :param point:
        :return:
        """
        pass
