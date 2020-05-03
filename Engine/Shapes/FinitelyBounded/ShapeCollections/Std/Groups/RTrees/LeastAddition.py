from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Groups.RTrees.RTree import RTree
import Engine


class LeastAddition(RTree):

    def __init__(self, nodes, head=True, identifier=-1):
        RTree.__init__(self, nodes, head, identifier)

    def _insert_heuristic(self, node):
        node_index = -1
        highest_area = -1
        box = node.get_bounding_box()
        for i in range(len(self.nodes)):
            overlap_box = Engine.shape_factory.AABB.overlap(box, self.nodes[i].get_bounding_box())
            area = overlap_box.get_surface_area()
            if area > highest_area or (area == highest_area and len(self.nodes[i].identifiers) > len(self.nodes[node_index].identifiers)):
                highest_area = area
                node_index = i
        return [self.nodes[node_index]]

    def _split_heuristic(self):
        absolvents = self.nodes
        self.nodes = []
        for i in range(self.MIN_FILL):
            self.nodes.append(LeastAddition([], head=False, identifier=i))
        for absolvent in absolvents:
            area, add_node = None, None
            for node in self.nodes:
                abbox = absolvent.get_bounding_box()
                nbbox = node.get_bounding_box()
                overlap_box = Engine.shape_factory.AABB.overlap(abbox, nbbox)
                new_area = overlap_box.get_surface_area()
                if area is None:
                    area = new_area
                    add_node = node
                elif area == new_area:
                    if len(add_node.identifiers) > len(node.identifiers):
                        area = new_area
                        add_node = node
                else:
                    area = new_area
                    add_node = node

            add_node.add(absolvent)
        self.leaf = False

