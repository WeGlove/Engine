import numpy
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Rectangle import Rectangle


class Camera(Rectangle):
    """
    A 2D camera. Looks at a section of a 2d plane in a canon COS
    """

    def __init__(self, position: numpy.ndarray, width: int, height: int, angle: float=0, identifier=-1,
                 resolution_x: int=None, resolution_y: int=None, anchor=None):
        """
        :param position: The middle point of the Camera
        :param width: The width of the rectangle
        :param height:
        :param angle:
        :param identifier:
        :param resolution_x:
        :param resolution_y:
        :param anchor: A tuple (bool, bool)
        """
        Rectangle.__init__(self, position, width, height, angle, identifier=identifier)

        # The anchor point of the rectangle
        if anchor is None:
            anchor = (True, True)
        x = self.left if anchor[0] else self.right
        y = self.down if anchor[1] else self.up
        self.anchor = numpy.array([x,y])

        # The COS spanned by the anchor
        self.cos = numpy.array([[1 if anchor[0] else -1, 0],
                                [0, 1 if anchor[1] else -1]])

        # The stretching over the COS
        self.resolution_x = resolution_x if resolution_x is not None else width
        self.resolution_y = resolution_y if resolution_y is not None else height

    def world_to_cam(self, point):
        """
        Translates a point from canon COS to a point in reference to anchor angle and resolution
        :param point:
        :return:
        """
        # Rotate the COS by the angle
        angled_cos = self.align_matrix.dot(self.cos)

        # Determine the new position of the anchor after rotating by angle
        pos_to_anchor = self.anchor - self.position
        pos_to_anchor_angled = numpy.dot(self.align_matrix, pos_to_anchor)
        angled_anchor = self.position + pos_to_anchor_angled

        # Determine the position of the point in the new COS
        angled_anchor_to_point = point - angled_anchor
        new_position = angled_anchor_to_point.dot(angled_cos)

        # Stretch new_position by Camera resolution
        new_position = new_position * numpy.array([self.resolution_x / self.width, self.resolution_y / self.height])
        return new_position

    def world_to_cam_scale_x(self, scalar):
        """
        Scale a scalar to the stretch of the camera in the x coordinates.
        :param scalar:
        :return:
        """
        return scalar * self.resolution_x / self.width

    def world_to_cam_scale_y(self, scalar):
        """
        Scale a scalar to the stretch of the camera in the y coordinates.
        :param scalar:
        :return:
        """
        return scalar * self.resolution_y / self.height

    def cam_to_world(self, point):
        """
        Reverses the world_to_cam operation
        :param point:
        :return:
        """
        # Rotate the COS by the angle
        angled_cos = self.align_matrix.dot(self.cos)

        # Determine the new position of the anchor after rotating by angle
        pos_to_anchor = self.anchor - self.position
        pos_to_anchor_angled = numpy.dot(self.align_matrix, pos_to_anchor)
        angled_anchor = self.position + pos_to_anchor_angled

        # Stretch point back to normal
        new_position = point * numpy.array([self.width / self.resolution_x, self.height / self.resolution_y])

        # Determine the position of the point in the canon COS
        angled_anchor_to_point = new_position.dot(numpy.transpose(angled_cos))
        point = angled_anchor_to_point + angled_anchor
        return point

    def cam_to_world_scale_x(self, scalar):
        """
        Scale a scalar to the stretch of the camera in the x coordinates.
        :param scalar:
        :return:
        """
        return scalar * self.width / self.resolution_x

    def cam_to_world_scale_y(self, scalar):
        """
        Scale a scalar to the stretch of the camera in the y coordinates.
        :param scalar:
        :return:
        """
        return scalar * self.height /  self.resolution_y


    # TODO vector to camera space

    def __str__(self):
        return f"Frustum: {super().__str__()}; Resolution = {self.resolution_x},{self.resolution_y}; Angle = {self.angle}"
