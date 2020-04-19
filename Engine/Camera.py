import Engine
AAB = Engine.shape_factory.AAB


class Camera(AAB):

    def __init__(self,  position, width, height, identifier=-1, resolution_x=None, resolution_y=None):
        AAB.__init__(self, position, width, height, identifier=identifier)
        self.resolution_x = resolution_x if resolution_x is not None else width
        self.resolution_y = resolution_y if resolution_y is not None else width

    def __str__(self):
        return f"Frustum: {super().__str__()}; Resolution = {self.resolution_x},{self.resolution_y}"
