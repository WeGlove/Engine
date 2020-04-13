from src.Shapes.FinitelyBounded.Factories.ShapeFactory import ShapeFactory
from src.Shapes.FinitelyBounded.ShapeCollections.Std.AAB import AAB
from src.Shapes.FinitelyBounded.ShapeCollections.Std.AABB import AABB
from src.Shapes.FinitelyBounded.ShapeCollections.Std.Rectangle import Rectangle
from src.Shapes.FinitelyBounded.ShapeCollections.Std.Groups.RTrees.LeastAddition import LeastAddition


class StdFactroy(ShapeFactory):

    get_AAB = AAB

    get_AABB = AABB

    get_Rect = Rectangle

    get_LA = LeastAddition
