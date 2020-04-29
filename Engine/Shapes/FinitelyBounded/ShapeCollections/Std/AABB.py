import Engine
import numpy
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.AAB import AAB


class AABB(AAB):

    def __init__(self, position, width, height, empty=False, identifier=-1):
        AAB.__init__(self, position, width, height, identifier)
        self.empty = empty

    def extend(self, boxes):
        down_left = None
        up_right = None

        for box in boxes + [self]:
            if not box.empty:
                if self.empty:
                    self.override(box)
                else:
                    a, b = box.to_coordinates()
                    if down_left is None:
                        down_left = a
                    else:
                        if down_left[0] > a[0]:
                            down_left[0] = a[0]
                        if down_left[1] > a[1]:
                            down_left[1] = a[1]

                    if up_right is None:
                        up_right = b
                    else:
                        if up_right[0] < b[0]:
                            up_right[0] = b[0]
                        if up_right[1] < b[1]:
                            up_right[1] = b[1]

        if not self.empty:
            self.override(self.from_coordinates(down_left, up_right))

    def override(self, box):
        self.position = box.position
        self.width = box.width
        self.height = box.height
        self.empty = box.empty

    def to_coordinates(self):
        """
        Returns a coordinate representation of the Box
        It holds that left <= right and down <= up
        :return:
        """
        return numpy.array([self.left, self.down]), numpy.array([self.right, self.up])

    def get_surface_area(self):
        if self.empty:
            return 0
        else:
            return (self.up - self.down) * (self.right - self.left)

    @staticmethod
    def overlap(first_box, second_box):
        if first_box.empty or second_box.empty:
            return AABB.empty()

        first_line = numpy.array([first_box.left, first_box.right])
        second_line = numpy.array([second_box.down, second_box.up])
        horizontal_overlap = AABB.line_overlap(first_line, second_line)
        if horizontal_overlap is None:
            return AABB.empty(-1)

        first_line = numpy.array([first_box.left, first_box.right])
        second_line = numpy.array([first_box.down, first_box.up])
        vertical_overlap = AABB.line_overlap(first_line, second_line)
        if vertical_overlap is None:
            return AABB.empty(-1)

        return AABB.from_coordinates(numpy.array([horizontal_overlap[0], vertical_overlap[0]]),
                                     numpy.array([horizontal_overlap[1], vertical_overlap[1]]))

    @staticmethod
    def line_overlap(first_line, second_line):
        A, B = first_line
        X, Y = second_line

        # second line is right of first_line
        BX = X - B
        if BX > 0:
            return None

        # second line is left of first line
        YA = A - Y
        if YA > 0:
            return None

        AX = X - A
        if AX >= 0:
            alpha = X
        else:
            alpha = A

        BY = Y - B
        if BY <= 0:
            beta = Y
        else:
            beta = B

        return numpy.array([alpha, beta])

    @staticmethod
    def empty(identifier=-1):
        return AABB(numpy.array([0,0]), 0, 0, empty=True, identifier=identifier)

    @staticmethod
    def combine(boxes):
        combination = boxes[0]
        if len(boxes) > 1:
            combination.extend(boxes[1:])
        return combination

    @staticmethod
    def from_coordinates(down_left, up_right):
        position = down_left + (up_right - down_left) / 2
        return Engine.shape_factory.AABB(position, abs(up_right[0] - down_left[0]), abs(up_right[1] - down_left[1]))

    def __str__(self):
        return f"AABB: ID:{self.identifier} Pos:{self.position} Dim:({self.width} {self.height}) Empty:{self.empty}"
