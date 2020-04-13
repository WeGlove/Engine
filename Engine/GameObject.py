class GameObject:

    def __init__(self, identifier=-1):
        self.identifier = identifier

    def __hash__(self):
        return self.identifier