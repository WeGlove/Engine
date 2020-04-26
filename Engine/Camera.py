import Engine
AAB = Engine.shape_factory.AAB
import numpy


class Camera(AAB):

    def __init__(self,  position, width, height, identifier=-1, resolution_x=None, resolution_y=None):
        AAB.__init__(self, position, width, height, identifier=identifier)
        self.resolution_x = resolution_x if resolution_x is not None else width
        self.resolution_y = resolution_y if resolution_y is not None else width

    def world_to_cam(self, position):
        new_position = position - numpy.array([self.left, self.down])
        new_position = new_position * numpy.array([self.resolution_x / self.width, self.resolution_y / self.height])
        return new_position

    def world_to_cam_scale_x(self, scalar):
        return scalar * self.resolution_x / self.width

    def world_to_cam_scale_y(self, scalar):
        return scalar * self.resolution_y / self.height

    def __str__(self):
        return f"Frustum: {super().__str__()}; Resolution = {self.resolution_x},{self.resolution_y}"
