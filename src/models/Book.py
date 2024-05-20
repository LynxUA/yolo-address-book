from abc import abstractmethod

class Book():

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def find_by_name(self, name:str):
        pass

    @abstractmethod
    def delete(self, name:str):
        pass
