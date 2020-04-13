class Intersection:

    def __init__(self, t, normal, intersected, parents=None):
        self.t = t
        self.normal = normal
        self.intersected = intersected
        self.parents = [] if parents is None else parents

    def add_parent(self, parent):
        self.parents.append(parent)

    def __str__(self):
        return f"Intersection: t={self.t} Normal={self.normal} Intersected: {self.intersected}"
