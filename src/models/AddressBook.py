from collections import UserDict
from datetime import date, datetime
from typing import List, Union
from src.models.Record import Record

class AddressBook(UserDict[str, Record]):

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, record_name:str) -> Union[Record, None]:
        return self.data.get(record_name)
     
    def search_contact_by_name(self, query: str) -> List[Record]:
        """
        Пошук контактів у книзі за заданим запитом.

        Args:
            query (str): Запит для пошуку контактів.

        Returns:
            List[Record]: Список знайдених контактів.
        """
        results: List[Record] = []
        for contact in self.data.values():    
            if query.lower() in contact.name.value.lower():
                results.append(contact)
        return results

    def delete(self, record_name:str):
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
