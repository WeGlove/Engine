shape_factory = None


def init():
    global shape_factory
    from Engine.Shapes.FinitelyBounded.Factories.StdFactory import StdFactroy
    shape_factory = StdFactroy()
