import abc

class Repository:
    @abc.abstractmethod
    def insert(self, data):
        pass

    @abc.abstractmethod
    def delete(self, condition):
        pass

    @abc.abstractmethod
    def update(self, data, comdition):
        pass