import json

from src.serialization.serialization_strategy import SerializationStrategy


class JsonSerializationStrategy(SerializationStrategy):
    def serialize(self, data: dict) -> str:
        return json.dumps(data)

    def deserialize(self, data: str) -> dict:
        return json.loads(data)
    