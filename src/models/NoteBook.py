from collections import UserDict
from src.models.Note import Note
from src.models.Book import Book


class NoteBook(Book, UserDict[str, Note]):

    def add(self, item:Note):
        self.data[item.name] = item

    def get(self, name:str) -> Note | None:
        return self.data.get(name)

    def find_by_name(self, name:str) -> list[Note]:
        keys = filter(lambda key: name in key, self.data.keys())
        return [self.data.get(key) for key in keys]

    def delete(self, name:str):
        del self.data[name]

    def find_by_text(self, partial_text:str) -> list[Note]:
        return list(filter(lambda note: partial_text in note.text, self.data.values()))

    def get_by_name(self, name:str) -> Note:
        return self.data[name]
