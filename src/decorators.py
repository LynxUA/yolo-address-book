from functools import wraps
from src.constants import INVALID_COMMAND, NOT_EXISTS, UNKNOWN

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return INVALID_COMMAND
        except KeyError:
            return NOT_EXISTS
        except Exception:
            return UNKNOWN
    return inner

#converts error to nice exit
def interrupt_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            exit()
    return inner
