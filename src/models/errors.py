class InvalidPhone(ValueError):
    def __init__(self, *args, msg='Phone must be 10 digits long string',  **kwargs):
        super().__init__(msg, *args, **kwargs)

class InvalidName(ValueError):
    def __init__(self, *args, msg='Name must be non empty string', **kwargs):
        super().__init__(msg, *args, **kwargs)

class InvalidBirthday(ValueError):
    def __init__(self, *args, msg='Invalid date format. Use DD.MM.YYYY', **kwargs):
        super().__init__(msg, *args, **kwargs)
