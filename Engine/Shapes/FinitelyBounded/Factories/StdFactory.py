from Engine.Shapes.FinitelyBounded.Factories.ShapeFactory import ShapeFactory
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.AAB import AAB
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.AABB import AABB
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Rectangle import Rectangle
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Groups.RTrees.LeastAddition import LeastAddition
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Groups.Shallow import Shallow
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Shape import Shape


class StdFactroy(ShapeFactory):

    def __init__(self):
        self.AAB = AAB
        self.AABB = AABB
        self.Rectangle = Rectangle
        self.LeastAddition = LeastAddition
        self.Shallow = Shallow
        self.Shape = Shape
