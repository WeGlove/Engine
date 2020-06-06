from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.AAB import AAB
import numpy
import math


class Rectangle(AAB):

    def __init__(self, position, width, height, angle, identifier=-1):
        AAB.__init__(self, position, width, height, identifier)

        self.angle = angle

        # Rotates a point to the rectangle
        self.align_matrix = self.get_rotation_matrix(self.angle)
        self.rev_align_matrix = self.get_rotation_matrix(-self.angle)

    def set_angle(self, angle):
        self.angle = angle
        self.align_matrix = self.get_rotation_matrix(self.angle)
        self.rev_align_matrix = self.get_rotation_matrix(-self.angle)

    @staticmethod
    def get_rotation_matrix(angle):
        return numpy.array([numpy.array([math.cos(angle/360*2*math.pi), -math.sin(angle/360*2*math.pi)]),
                            numpy.array([math.sin(angle/360*2*math.pi),  math.cos(angle/360*2*math.pi)])]
                           )

    def intersect(self, ray):
        ray_copy = ray.copy()
        return super().intersect(ray_copy)
