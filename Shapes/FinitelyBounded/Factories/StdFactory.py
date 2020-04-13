from Shapes.FinitelyBounded.Factories.ShapeFactory import ShapeFactory
from Shapes.FinitelyBounded.ShapeCollections.Std.AAB import AAB
from Shapes.FinitelyBounded.ShapeCollections.Std.AABB import AABB
from Shapes.FinitelyBounded.ShapeCollections.Std.Rectangle import Rectangle
from Shapes.FinitelyBounded.ShapeCollections.Std.Groups.RTrees.LeastAddition import LeastAddition


class StdFactroy(ShapeFactory):

    get_AAB = AAB

    get_AABB = AABB

    get_Rect = Rectangle

    get_LA = LeastAddition
