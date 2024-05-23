from collections import UserDict

from src.models.Note import Note
from src.models.Book import Book
from src.utiles import wrap_text


class NoteBook(Book, UserDict[str, Note]):

    def add(self, item:Note):
        self.data[item.name] = item

    def get(self, name:str) -> Note | None:
        return self.data.get(name)

    def find_by_name(self, name:str) -> list[Note]:
        keys = filter(lambda key: name.lower() in key.lower(),
                      self.data.keys())
        return [self.data.get(key) for key in keys]

    def delete(self, name:str):
        del self.data[name]

    def find_by_text(self, partial_text:str) -> list[Note]:
        return list(filter(lambda note: partial_text.lower() in note.text.lower(),
                           self.data.values()))

    def get_by_name(self, name:str) -> Note:
        return self.data[name]
    
    def format_notes(self) -> str:
        max_body_length = 90
        separator = "-" * max_body_length

        res = ""
        for title, note in self.data.items():
            res += separator + "\n"
            wrapped_title = wrap_text(title, max_body_length, "title:  |  ", " " * len("title:  |  "))
            res += wrapped_title + "\n"
            wrapped_body = wrap_text(note.text, max_body_length, "body:   |  ", " " * len("body:   |  "))
            res += wrapped_body + "\n"
            res += f"tags:   |  {', '.join(note.tags)}\n"
            res += separator + "\n"

        return res

    @classmethod
    def from_dict(cls, data):
        note_book = cls()
        book = data.get("note-book")
        if not book:
            return note_book
        for name, note in book.items():
            note_book[name] = Note.from_dict(name, note)
        return note_book

    def to_dict(self) -> dict:
        return { "note-book": {key: value.to_dict() for key, value in self.data.items()}} if self.data else None
