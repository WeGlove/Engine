from Shapes.FinitelyBounded.ShapeCollections.Std.Groups.Group import Group
import Shapes

class Shallow(Group):

    def __init__(self, leaves, identifier=-1):
        Group.__init__(self, identifier)
        self.bounding_box = Shapes.factory.get_AABB.empty(identifier)
        self.nodes = []
        for leaf in leaves:
            self.add(leaf)

    def intersect(self, ray):
        intersections = []
        for leaf in self.nodes:
            intersections += leaf.intersect(ray)
        return intersections

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
        self.bounding_box.extend(node.get_bounding_box())

    def delete(self, identifier):
        self.nodes = [leaf for leaf in self.nodes if hash(leaf) == identifier]
        self.bounding_box = Shapes.factory.get_AABB.combine([node.get_bounding_box() for node in self.nodes])
