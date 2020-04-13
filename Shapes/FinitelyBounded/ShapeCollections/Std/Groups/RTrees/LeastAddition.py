from Shapes.FinitelyBounded.ShapeCollections.Std.Groups.RTrees.RTree import RTree
import Shapes


class LeastAddition(RTree):

    def __init__(self, nodes, head=True, identifier=-1):
        RTree.__init__(self, nodes, head, identifier)

    def _insert_heuristic(self, node):
        node_index = -1
        highest_area = -1
        box = node.get_bounding_box()
        for i in range(len(self.nodes)):
            overlap_box = Shapes.factory.get_AABB.overlap(box, self.nodes[i].get_bounding_box())
            area = overlap_box.get_surface_area()
            if area > highest_area:
                highest_area = area
                node_index = i
        self.nodes[node_index].add(node)

    def _split_heuristic(self):
        absolvents = self.nodes
        self.nodes = []
        for i in range(self.FILL):
            self.nodes.append(LeastAddition([absolvents[i]], head=False, identifier=i))
        self.leaf = False

