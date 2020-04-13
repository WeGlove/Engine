from Engine import Shapes
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Simple import Simple
import numpy
from Engine import Intersection


class AAB(Simple):

    def __init__(self, position, width, height, identifier=-1):
        Simple.__init__(self, identifier)
        self.position = position

        self.width = width
        self.height = height

        self.up = position[1] + height / 2  # Assumes the canon COS
        self.down = position[1] - height / 2

        self.right = position[0] + width / 2
        self.left = position[0] - width / 2

    def set_position(self, position):
        self.position = position

        self.up = position[1] + self.height / 2
        self.down = position[1] - self.height / 2

        self.right = position[0] + self.width / 2
        self.left = position[0] - self.width / 2

    def intersect(self, ray, parents=None):
        up = self.up + ray.error
        down = self.down - ray.error

        left = self.left - ray.error
        right = self.right + ray.error

        if ray.direction[0] == 0:
            if ray.direction[1] == 0:
                if down <= ray.position[1] <= up and left <= ray.position[0] <= right:
                    return [Intersection.Intersection(0, numpy.array([0, 0]), self, parents),
                            Intersection.Intersection(0, numpy.array([0, 0]), self, parents)]
                else:
                    return []
            else:
                t0y = (down - ray.position[1]) / ray.direction[1]
                t1y = (up - ray.position[1]) / ray.direction[1]
                if left <= ray.position[0] <= right:
                    return [Intersection.Intersection(t0y, numpy.array([0, -1]), self, parents),
                            Intersection.Intersection(t1y, numpy.array([0, 1]), self, parents)] \
                            if t0y < t1y else \
                           [Intersection.Intersection(t1y, numpy.array([0, 1]), self, parents),
                            Intersection.Intersection(t0y, numpy.array([0, -1]), self, parents)]
                else:
                    return []
        else:
            if ray.direction[1] == 0:
                t0x = (left - ray.position[0]) / ray.direction[0]
                t1x = (right - ray.position[0]) / ray.direction[0]
                if left <= ray.position[0] <= right:
                    return [Intersection.Intersection(t0x, numpy.array([-1, 0]), self, parents),
                            Intersection.Intersection(t1x, numpy.array([1, 0]), self, parents)] \
                            if t0x < t1x else \
                           [Intersection.Intersection(t1x, numpy.array([1, 0]), self, parents),
                            Intersection.Intersection(t0x, numpy.array([-1, 0]), self, parents)]
                else:
                    return []

        tLeft = (left - ray.position[0]) / ray.direction[0]
        tRight = (right - ray.position[0]) / ray.direction[0]
        if tLeft > tRight:
            tLeft, tRight = tRight, tLeft

        tUp = (up - ray.position[1]) / ray.direction[1]
        tDown = (down - ray.position[1]) / ray.direction[1]
        if tDown > tUp:
            tDown, tUp = tUp, tDown

        if tLeft > tUp or tDown > tRight:
            return []
        else:
            intersections = []
            if tDown > tLeft:
                tMin = tDown
                normalMin = numpy.array([0,-1])
            else:
                tMin = tLeft
                normalMin = numpy.array([-1,0])

            if tUp < tRight:
                tMax = tUp
                normalMax = numpy.array([0,1])
            else:
                tMax = tRight
                normalMax = numpy.array([1,0])

            if tMin > tMax:
                tMin, tMax = tMax, tMin
                normalMin, normalMax = normalMax, normalMin
            intersections.extend([Intersection.Intersection(tMin, normalMin, self, parents),
                                  Intersection.Intersection(tMax, normalMax, self, parents)])
            return intersections

    def is_in(self, point):
        return self.position[0] - self.width / 2 <= point[0] <= self.position[0] + self.width / 2 and \
               self.position[1] - self.height / 2 <= point[1] <= self.position[1] + self.height / 2

    def get_at(self, point):
        if self.is_in(point):
            return [self]
        else:
            return []

    def get_bounding_box(self):
        return Shapes.factory.get_AABB(self.position, self.width, self.height)
