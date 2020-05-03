from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Groups.Group import Group
import Engine


class Shallow(Group):

    def __init__(self, leaves, identifier=-1):
        Group.__init__(self, identifier)
        self.bounding_box = Engine.shape_factory.AABB.empty(identifier)
        self.nodes = []
        for leaf in leaves:
            self.add(leaf)

    def intersect(self, ray):
        if len(self.bounding_box.intersect(ray)) > 0:
            intersections = []
            for leaf in self.nodes:
                intersections += leaf.intersect(ray)
            return intersections
        else:
            return []

    def is_in(self, point):
        for leaf in self.nodes:
            if leaf.is_in(point):
                return True
        return False

    def get_bounding_box(self):
        return self.bounding_box

    def get_at(self, point):
        simples = []
        for node in self.nodes:
            if node.is_in(point):
                simples += node.get_at(point)
        return simples

    def is_leaf(self):
        return True

    def is_head(self):
        return True

    def add(self, node):
        self.nodes.append(node)
        self.bounding_box.extend([node.get_bounding_box()])

    def delete(self, identifier):
        self.nodes = [leaf for leaf in self.nodes if hash(leaf) != identifier]
        if len(self.nodes) == 0:
            self.bounding_box = Engine.shape_factory.AABB.empty()
        else:
            self.bounding_box = Engine.shape_factory.AABB.combine([node.get_bounding_box() for node in self.nodes])

    def get_leaves(self):
        return self.nodes
