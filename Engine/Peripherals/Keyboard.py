from abc import abstractmethod


class Keyboard:

    @abstractmethod
    def isPressed(self, key):
        pass

    @abstractmethod
    def getPressed(self):
        pass

    @abstractmethod
    def arePressed(self, keys):
        pass

    @abstractmethod
    def update(self):
        pass