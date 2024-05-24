from datetime import datetime
import re
from src.models.errors import InvalidBirthday, InvalidEmail, InvalidName, InvalidPhone

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self) -> str:
        return self.__str__()

class Name(Field):
    def __init__(self, value):
        if not (value and isinstance(value, str)):
            raise InvalidName
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not (isinstance(value, str) and len(value)==10 and value.isdecimal()):
            raise InvalidPhone
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
            datetime.strptime(value, "%d.%m.%Y")
            super().__init__(value)
        except ValueError as ve:
            raise InvalidBirthday from ve

class Address(Field):
    pass

class Email(Field):
    def __init__(self, value):
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value):
            super().__init__(value)
        else:
            raise InvalidEmail
