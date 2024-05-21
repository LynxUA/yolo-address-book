from textwrap import wrap

class Note():
    def __init__(self, name:str, text:str):
        self.__name = name
        self.__text = text
        self.__tags: set[str] = set()

    def __str__(self) -> str:
        return (f"{self.__name}\n"
                "\n".join(wrap(f"{self.text}\n") + wrap(", ".join(self.__tags))))

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

    def add_tags(self, *tags):
        for tag in tags:
            if isinstance(tag, str):
                self.__tags.add(tag)

    def remove_tags(self, *tags):
        for tag in tags:
            self.__tags.remove(tag)

    def exists_tag(self, tag:str) -> bool:
        return self.__tags.issuperset(tag)
