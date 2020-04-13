from abc import abstractmethod


class ShapeFactory:

    @abstractmethod
    def get_AAB(position, width, height, identifier=-1):
        pass