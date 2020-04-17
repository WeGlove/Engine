from abc import abstractmethod


class Mouse:

    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def clicked(self):
        pass

    @abstractmethod
    def left_clicked(self):
        pass

    @abstractmethod
    def middle_clicked(self):
        pass

    @abstractmethod
    def right_clicked(self):
        pass

    @abstractmethod
    def update(self):
        pass