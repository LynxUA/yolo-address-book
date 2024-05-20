class Note():
    def __init__(self, name:str, text:str):
        self.__name = name
        self.__text = text
        self.__tags: set[str] = set()

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
