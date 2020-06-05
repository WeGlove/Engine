import numpy
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Rectangle import Rectangle


class Camera(Rectangle):
    """
    A 2D camera. Looks at a section of a 2d plane in a canon COS
    """

    def __init__(self, position: numpy.ndarray, width: int, height: int, angle: float, identifier=-1, resolution_x: int=None, resolution_y: int=None):
        Rectangle.__init__(self, position, width, height, angle, identifier=identifier)
        self.resolution_x = resolution_x if resolution_x is not None else width
        self.resolution_y = resolution_y if resolution_y is not None else height

    def world_to_cam(self, position):
        new_position = position - self.align_matrix.dot(numpy.array([self.left, self.down]) - self.position)
        new_position = new_position * numpy.array([self.resolution_x / self.width, self.resolution_y / self.height])
        return new_position

    def world_to_cam_scale_x(self, scalar):
        return scalar * self.resolution_x / self.width

    def world_to_cam_scale_y(self, scalar):
        return scalar * self.resolution_y / self.height

    def __str__(self):
        return f"Frustum: {super().__str__()}; Resolution = {self.resolution_x},{self.resolution_y}; Angle = {self.angle}"
