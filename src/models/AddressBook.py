from collections import UserDict
from datetime import date, datetime
from src.models.Record import Record

class AddressBook(UserDict[str, Record]):

    def add_record(self, record:Record):
        self.data[record.name.value] = record

    def find(self, record_name:str) -> Record | None:
        return self.data.get(record_name)

    def delete(self, record_name:str):
        keys_to_delete = [key for key, record in self.data.items()
                          if record.record_name == record_name]
        for key in keys_to_delete:
            del self.data[record_name]

    def get_upcoming_birthdays(self) -> list[Record]:
        upcoming_birthdays = []
        for record in self.data.values():
            if not record.birthday:
                continue
            birthday_date:date = record.birthday.value
            birthday_this_year = birthday_date.replace(year=datetime.now().year)
            days_from_today = self.__get_days_from_today(birthday_this_year)
            #handle last 7 days of the year -> try BD next year
            if days_from_today < 0:
                birthday_next_year = birthday_date.replace(year=datetime.now().year+1)
                days_from_today = self.__get_days_from_today(birthday_next_year)
            if days_from_today <= 7:
                upcoming_birthdays.append(record)
        return upcoming_birthdays


    @staticmethod
    def __get_days_from_today(congrats_date:date) -> int:
        date_now = datetime.now().date()
        return (congrats_date - date_now).days
