import pickle
from src.models.AddressBook import AddressBook


class AddressBookManager:
    def __init__(self, filename):
        self.address_book:AddressBook | None = None
        self.opened = False
        self.filename = filename

    def __enter__(self):
        self.opened = True
        try:
            with open(self.filename, "rb") as f:
                self.address_book= pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.address_book = AddressBook()
        return self.address_book

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            with open(self.filename, "wb") as f:
                pickle.dump(self.address_book, f)
                self.opened = False
