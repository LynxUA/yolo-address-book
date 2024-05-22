import json

from src.Storate import Storage
from src.models.AddressBook import AddressBook
from src.models.NoteBook import NoteBook
from src.serialization.json_serialization_strategy import JsonSerializationStrategy
from src.serialization.serialization_strategy import SerializationStrategy


class BookManager(Storage):
    def __init__(self, filename: str, strategy: SerializationStrategy = JsonSerializationStrategy(), read_modificator: str = "r", write_modification: str = "w", error_exception: Exception = json.JSONDecodeError):
        super().__init__(filename, strategy, read_modificator, write_modification, error_exception)
        self.address_book = AddressBook()
        self.note_book = NoteBook()
        self.opened = False

    def __enter__(self):
        self.opened = True
        data = super().load()
        if data:
                self.address_book = AddressBook.from_dict(data)
                self.note_book = NoteBook.from_dict(data)
        return self.address_book, self.note_book

    def __exit__(self, *args):
      if self.opened:
            self.opened = False
            address_book_data_to_save = self.address_book.to_dict()
            note_book_data_to_save = self.note_book.to_dict()

            if not address_book_data_to_save and not note_book_data_to_save:
                return

            data_to_save = {}
            if address_book_data_to_save:
                data_to_save.update(address_book_data_to_save)
            if note_book_data_to_save:
                data_to_save.update(note_book_data_to_save)

            if data_to_save:
               super().save(data_to_save)


            