from abc import abstractmethod


class ShapeFactory:

    @abstractmethod
    def AAB(self, position, width, height, identifier=-1):
        pass
