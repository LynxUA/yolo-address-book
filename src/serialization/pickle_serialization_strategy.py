import pickle

from src.serialization.serialization_strategy import SerializationStrategy


class PickleSerializationStrategy(SerializationStrategy):
    def serialize(self, obj):
        return pickle.dumps(obj)

    def deserialize(self, data):
        return pickle.loads(data)
