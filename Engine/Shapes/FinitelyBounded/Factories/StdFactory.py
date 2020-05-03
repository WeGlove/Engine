from Engine.Shapes.FinitelyBounded.Factories.ShapeFactory import ShapeFactory
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.AAB import AAB
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.AABB import AABB
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Rectangle import Rectangle
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Groups.RTrees.LeastAddition import LeastAddition
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Groups.Shallow import Shallow


class StdFactroy(ShapeFactory):

    AAB = AAB

    AABB = AABB

    Rectangle = Rectangle

    LeastAddition = LeastAddition

    Shallow = Shallow
