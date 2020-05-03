from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Groups.Shallow import Shallow
from abc import abstractmethod
import Engine


class RTree(Shallow):

    FILL = 4
    MIN_FILL = 2

    def __init__(self, nodes, head=True, identifier=-1):
        self.bounding_box = Engine.shape_factory.AABB.empty(identifier)
        self.head = head
        self.leaf = True
        self.identifiers = []
        Shallow.__init__(self, nodes, identifier)

    def is_leaf(self):
        return self.leaf

    def is_head(self):
        return self.head

    def add(self, node):
        self.identifiers.append(hash(node))
        self.bounding_box.extend([node.get_bounding_box()])

        if self.leaf:
            self.nodes.append(node)
            if len(self.nodes) > self.FILL:
                self._split_heuristic()
        else:
            for add_node in self._insert_heuristic(node):
                add_node.add(node)



    @abstractmethod
    def _insert_heuristic(self, node):
        """
        A heuristic by which the Tree decides to which nodes to add the node to
        :param node:
        :return:
        """
        return []

    @abstractmethod
    def _split_heuristic(self):
        """
        A heuristic by which the Tree decides how to split nodes into sub trees
        :return:
        """
        pass

    def delete(self, identifier):
        if self.leaf:
            if identifier in self.identifiers:
                self.identifiers.remove(identifier)
            super().delete(identifier)
            if not self.head:
                if len(self.nodes) < self.MIN_FILL:
                    return [(True, self.nodes)]
                else:
                    return []
        else:
            if identifier in self.identifiers:
                self.identifiers.remove(identifier)
                absolvents = []
                for node in self.nodes:
                    new_absolvents = node.delete(identifier)
                    absolvents += new_absolvents
                    if len(node.nodes) < self.MIN_FILL:
                        self.nodes.remove(node)
                if len(self.nodes) < self.MIN_FILL:
                    absolvents += [(False, self.nodes)]
                if not self.head:
                    return absolvents
                else:
                    for leaf, absolvent in absolvents:
                        if leaf:
                            self.add(absolvent)
                        else:
                            self.merge_tree(absolvent)

            self.bounding_box = Engine.shape_factory.AABB.combine([node.get_bounding_box() for node in self.nodes])

    def merge_tree(self, tree):
        if self.leaf:
            raise Exception()
        else:
            bbox = tree.get_bounding_box()
            area = None
            node_selection = None
            for node in self.nodes:
                node_bbox = node.get_bounding_box()
                overlap = node_bbox.overlap(bbox)
                new_area = overlap.surface_area()
                if area is None or new_area < area:
                    area = new_area
                    node_selection = node
            if area == 0:
                if node_selection.leaf:
                    self.nodes.append(tree)
                else:
                    for node in self._insert_heuristic(node_selection):
                        node.add(tree)
            self.identifiers += tree.identifiers

    def get_leaves(self):
        if self.leaf:
            return self.nodes
        else:
            leaves = []
            for node in self.nodes:
                leaves += node.get_leaves()
            return leaves

