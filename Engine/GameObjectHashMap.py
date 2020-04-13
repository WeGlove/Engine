class GameObjectHashMap(dict):

    def __init__(self):
        dict.__init__(self)
        self.ids = []
        self.maximum = 0

    def getNextID(self):
        if len(self.ids) == 0:
            self.maximum += 1
            return self.maximum - 1
        else:
            return_id = self.ids[0]
            self.pop(0)
            return return_id

    def pop(self, identifier):
        dict.pop(self, identifier)
        self.ids.append(identifier)
        for i in range(len(self.ids)-1, 0, -1):
            if self.ids[i] == self.maximum-1:
                self.maximum -= 1
                self.ids.pop(-1)
            else:
                break

