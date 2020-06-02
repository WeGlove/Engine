from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.AABPrototype import AABPrototype
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.AABB import AABB


class AAB(AABPrototype):
    """
        An Axis Aligned Box.
        Differentiates from ABBB because it can't be empty.
    """

    def __init__(self, position, width, height, identifier=-1):
        AABPrototype.__init__(self, position, width, height, identifier)

    def get_bounding_box(self):
        return AABB(self.position, self.width, self.height)

