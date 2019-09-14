from abc import ABC


class AbstractNode(ABC):
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    def __str__(self):
        return str(self.__data)
