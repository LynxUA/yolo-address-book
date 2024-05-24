from textwrap import wrap

class Note():
    def __init__(self, name:str, text:str):
        self.__name = name
        self.__text = text
        self.tags: set[str] = set()

    def __str__(self) -> str:
        return f"Note title: {self.__name}, body: {self.text}, tags: {', '.join(self.tags)}"

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text:str):
        self.__text = text

    def add_tags(self, *args):
        tags, = args
        for tag in tags:
            if isinstance(tag, str):
                self.tags.add(tag.strip())

    def remove_tags(self, *tags):
        for tag in tags:
            self.tags.remove(tag)

    def exists_tag(self, tag:str) -> bool:
        return self.tags.issuperset(tag)
    
    def to_dict(self) -> dict:
        return {"text": self.__text, "tags": list(self.tags)} if self.__text else None
    
    @classmethod
    def from_dict(cls, name:str, data:dict):
        note = cls(name, data.get("text"))
        if data.get("tags"):
            note.add_tags(data.get("tags"))
        return note
