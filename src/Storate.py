from src.serialization.serialization_strategy import SerializationStrategy


class Storage:
    def __init__(self, file_name: str, strategy: SerializationStrategy, read_modificator: str, write_modification: str, error_exception: Exception = SyntaxError):
        self.file_name = file_name
        self.read_modificator = read_modificator
        self.write_modification = write_modification
        self.error_exception = error_exception
        self.strategy = strategy

    def save(self, data: dict):
        with open(self.file_name, self.write_modification) as file:
            file.write(self.strategy.serialize(data))

    def load(self) -> dict:
        try:
            with open(self.file_name, self.read_modificator) as file:
                return self.strategy.deserialize(file.read())
        except (self.error_exception):
            # Note: If file is empty, return empty dictionary. We need it when we will handle the errors' messages
            return {}
        except (FileNotFoundError):
            # Note: If file does not exist, return empty dictionary. We need it when we will handle the errors' messages
            return {}