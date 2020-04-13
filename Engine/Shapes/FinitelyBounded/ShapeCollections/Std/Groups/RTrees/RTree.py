from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Groups.Shallow import Shallow
from abc import abstractmethod
from Engine import Shapes


class RTree(Shallow):

    FILL = 4
    MIN_FILL = 2

    def __init__(self, nodes, head=True, identifier=-1):
        self.bounding_box = Shapes.factory.get_AABB.empty(identifier)
        self.head = head
        self.leaf = True
        Shallow.__init__(self, nodes, identifier)


    def is_leaf(self):
        return self.leaf

    def is_head(self):
        return self.head

    def add(self, node):
        if self.leaf:
            if len(self.nodes) == self.FILL:
                self._split_heuristic()
                self.leaf = False
                self._insert_heuristic(node)
            else:
                self.nodes.append(node)
        else:
            self._insert_heuristic(node)

        self.bounding_box.extend([node.get_bounding_box()])

    @abstractmethod
    def _insert_heuristic(self, node):
        pass

    @abstractmethod
    def _split_heuristic(self):
        pass

    def delete(self, identifier):
        if self.leaf:
            self.nodes = [node for node in self.nodes if hash(node) == identifier]
        else:
            for node in self.nodes:
                node.delete(identifier)
                if len(node.nodes) <= self.MIN_FILL:
                    absolvents = node.nodes
                    for absolvent in absolvents:
                        self.add(absolvent)
        self.bounding_box = Shapes.factory.get_AABB.combine([node.get_bounding_box() for node in self.nodes])


