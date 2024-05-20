from collections import UserDict
from src.models.Note import Note
from src.models.Book import Book


class NoteBook(Book, UserDict[str, Note]):

    def add(self, item:Note):
        self.data[item.name] = item

    def find_by_name(self, name:str) -> Note | None:
        return self.data.get(name)

    def delete(self, name:str):
        del self.data[name]

    def find_by_text(self, partial_text:str) -> list[Note]:
        return filter(lambda note: partial_text in note.text, self.data.values())
