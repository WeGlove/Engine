class Intersection:

    def __init__(self, t, normal, intersected):
        self.t = t
        self.normal = normal
        self.intersected = intersected

    def __str__(self):
        return f"Intersection: t={self.t} Normal={self.normal} Intersected: {self.intersected}"
