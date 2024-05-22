from abc import ABC, abstractmethod

class SerializationStrategy(ABC):
    @abstractmethod
    def serialize(self, data) -> bytes:
        pass

    @abstractmethod
    def deserialize(self, data: bytes):
        pass
    