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
        return {key: self.data.get(key) for key in keys}
    
    def update(self, old_name:str, new_note:Note):
        if old_name in self.data:
            self.delete(old_name)
        self.data[new_note.name] = new_note

    def delete(self, name:str):
        del self.data[name]

    def find_by_text(self, partial_text:str) -> list[Note]:
        return {note.name: note for note in self.data.values() if partial_text.lower() in note.text.lower()}
    
    def find_by_tag(self, tag:str) -> list[Note]:
        return {item.name: item for item in self.data.values() if tag.lower() in map(str.lower, item.tags)}

    def get_by_name(self, name:str) -> Note:
        return self.data[name]
    
    def format_notes(self, data: dict) -> str:
        max_body_length = 90
        separator = "-" * max_body_length
        res = ""
        for title, note in data.items():
            res += separator + "\n"
            wrapped_title = wrap_text(title, max_body_length, "title:  |  ", " " * len("title:  |  "))
            res += wrapped_title + "\n"
            wrapped_body = wrap_text(note.text, max_body_length, "body:   |  ", " " * len("body:   |  "))
            res += wrapped_body + "\n"
            wrapped_tags = wrap_text(", ".join(note.tags), max_body_length, "tags:   |  ", " " * len("tags:   |  "))
            res += wrapped_tags + "\n"
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
