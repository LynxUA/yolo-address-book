from src.models.fields import Address, Birthday, Email, Name, Phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None
        self.email = None
        self.address = None

    # реалізація класу
    def add_phone(self, phone:str):
        self.phones.append(Phone(phone))

    def remove_phone(self, del_phone:str):
        phone = self.find_phone(del_phone)
        if phone:
            self.phones.remove(phone)

    def edit_phone(self, old_phone:str, new_phone:str):
        old = self.find_phone(old_phone)
        if old:
            old.value = new_phone

    def find_phone(self, phone:str) -> Phone | None:
        found_phone = list(filter(lambda p: p.value==phone, self.phones))[0]
        return found_phone if found_phone else None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_address(self, address):
        self.address = Address(address)

    def add_email(self, email):
        self.email = Email(email)

    def __str__(self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday.value if self.birthday else None}, email: {self.email}, address:{self.address}, phones: {'; '.join(p.value for p in self.phones)}"

    #prints Record nicely in print(AddressBook)
    def __repr__(self) -> str:
        return self.__str__()
