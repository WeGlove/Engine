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
        return numpy.array([numpy.array([math.cos(angle), -math.sin(angle)]),
                            numpy.array([math.sin(angle), math.cos(angle)])]
                           )

    def intersect(self, ray):
        ray_copy = ray.copy()
        return super().intersect(ray_copy)
