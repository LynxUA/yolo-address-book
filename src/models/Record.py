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
        phones = ", ".join(map(lambda phone: phone.value, self.phones))
        return (f"{'Name':<10}{"| "}{self.name}\n"
                f"{'Birthday':<10}{"| "}{self.birthday}\n"
                f"{'Phone':<10}{"| "}{phones}\n"
                f"{'Email':<10}{"| "}{self.email}\n"
                f"{'Address':<10}{"| "}{self.address}\n")

    #prints Record nicely in print(AddressBook)
    def __repr__(self) -> str:
        return self.__str__()

    #converts Record to dict for json
    @classmethod
    def from_dict(cls, name, data: dict):
        record = cls(name)
        if data.get("birthday"):
            record.add_birthday(data["birthday"])
        if data.get("phones"):
            for phone in data["phones"]:
                record.add_phone(phone)
        if data.get("email"):
            record.add_email(data["email"])
        if data.get("address"):
            record.add_address(data["address"])
        return record
    
    #converts dict to Record for json
    def to_dict(self):
        result = {}
        if self.phones:
            result["phones"] = [phone.value for phone in self.phones]
        if self.birthday:
            result["birthday"] = self.birthday.value
        if self.email:
            result["email"] = self.email.value
        if self.address:
            result["address"] = self.address.value
        return result
