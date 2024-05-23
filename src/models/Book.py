from abc import abstractmethod

class Book():
    """Represent storage class for items"""
    @abstractmethod
    def add(self, item):
        """Adds item to the Book if it does not exist.
        Otherwise overrides existing one"""

    @abstractmethod
    def get(self, name:str):
        """Returns item with name exactly matched to the "name" if such item exists.
        Otherwise returns None"""

    @abstractmethod
    def find_by_name(self, name:str):
        """Performs search for items with name containing "name".
        Returns list with items"""

    @abstractmethod
    def delete(self, name:str):
        """Deletes item if it exists.
        Otherwise raises KeyError"""
