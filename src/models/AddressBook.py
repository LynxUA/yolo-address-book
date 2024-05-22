from collections import UserDict
from datetime import date, datetime
from src.models.Book import Book
from src.models.Record import Record

class AddressBook(Book, UserDict[str, Record]):

    def add(self, item:Record):
        self.data[item.name.value] = item

    def get(self, name:str) -> Record | None:
        return self.data.get(name)

    #TODO: change impl to perform inclusive search and return list
    def find_by_name(self, name:str) -> Record | None:
        return self.data.get(name)

    def delete(self, name:str):
        del self.data[name]

    def get_upcoming_birthdays(self, range) -> list[Record]:
        upcoming_birthdays = []
        for record in self.data.values():
            if not record.birthday:
                continue
            
            birthday_date:date = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
            birthday_this_year = birthday_date.replace(year=datetime.now().year)
            days_from_today = self.__get_days_from_today(birthday_this_year)
            #handle last 7 days of the year -> try BD next year
            if days_from_today < 0:
                birthday_next_year = birthday_date.replace(year=datetime.now().year+1)
                days_from_today = self.__get_days_from_today(birthday_next_year)
            if days_from_today <= range:
                upcoming_birthdays.append(record)
        return upcoming_birthdays


    @staticmethod
    def __get_days_from_today(congrats_date:date) -> int:
        date_now = datetime.now().date()
        return (congrats_date - date_now).days
    
    @classmethod
    def from_dict(cls, data):
        address_book = cls()
        book = data.get("address-book")
        for name, record in book.items():
            address_book[name] = Record.from_dict(name, record)
        return address_book
    
    def to_dict(self):
        return {"address-book": {name: record.to_dict() for name, record in self.data.items()}} if self.data else None
