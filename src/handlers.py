from itertools import zip_longest
from src.constants import DELETED, ERROR, INFO, UPDATED
from src.decorators import input_error
from src.models.AddressBook import AddressBook
from src.models.Record import Record

@input_error
def add_contact(args:list[str], contacts:AddressBook) -> str:
    defaults = [None, None, None, None, []]
    name, phone, email, address, *rest = (item for item, _ in zip_longest(args, defaults, fillvalue=None))
    if address and len(rest) > 0:
        address = address + " " + " ".join(rest)
    if not name:
        raise ValueError
    contact = contacts.get(name)
    msg =  UPDATED.format(class_name = "Contact", item_name = name)

    if not contact:
        contact = Record(name)
        contacts.add(contact)
        msg = INFO + f" Contact {name} successfully created."
    if phone:
        contact.add_phone(phone)
    if email:
        contact.add_email(email)
    if address:
        contact.add_address(address)
    return msg

@input_error
def change_contact(args:list[str], contacts:AddressBook) -> str:
    defaults = [None, None, None, None, None, []]
    name, old_phone, new_phone, email, address, *rest = (item for item, _ in zip_longest(args, defaults, fillvalue=None))
    if address and len(rest) > 0:
        address = address + " " + " ".join(rest)
    if not name or not old_phone or not new_phone:
        raise ValueError
    contact = contacts.get(name)

    if not contact:
        raise KeyError
    contact.edit_phone(old_phone, new_phone)
    if email:
        contact.add_email(email)
    if address:
        contact.add_address(address)
    return UPDATED.format(class_name = "Contact",item_name = name)

@input_error
def phone_contact(args:list[str], contacts:AddressBook) -> str:
    name, = args

    found_contacts = contacts.find_by_name(name)
    if not found_contacts:
        raise KeyError
    result = ""
    for contact in found_contacts:
        result += f"Contact: {contact.name}\n"
        for phone in contact.phones:
            result += f"Phone: {phone}\n"
    return result

def all_contact(contacts:AddressBook) -> str:
    if not contacts.data:
        return INFO + " You do not have any contacts saved"

    res = ""
    for name in contacts.data:
        res += "-"*80 + "\n"
        res += str(contacts.get(name))
        res += "-"*80 + "\n"
    return res.strip()

@input_error
def delete_contact(args: list[str], contacts: AddressBook):
    name, = args
    contacts.delete(name)
    return DELETED.format(class_name = "Contact", item_name="name")

@input_error
def add_birthday(args:list[str], contacts:AddressBook):
    name, birthday, = args
    contact = contacts.get(name)
    if not contact:
        raise KeyError
    contact.add_birthday(birthday)
    return UPDATED.format(class_name = "Contact",item_name = name)

@input_error
def add_email(args:list[str], contacts:AddressBook):
    name, email, = args
    contact = contacts.get(name)
    if not contact:
        raise KeyError
    contact.add_email(email)
    return UPDATED.format(class_name = "Contact",item_name = name)

@input_error
def add_address(args:list[str], contacts:AddressBook):
    name, *rest = args
    if len(rest) == 0:
        raise ValueError
    address = " ".join(rest)
    contact = contacts.get(name)
    if not contact:
        raise KeyError
    contact.add_address(address)
    return UPDATED.format(class_name = "Contact",item_name = name)

@input_error
def show_birthday(args:list[str], contacts:AddressBook):
    name, = args
    contact = contacts.get(name)
    if not contact:
        raise KeyError
    if not contact.birthday:
        return ERROR + "Conntact does not have saved birthday date"
    return contact.birthday.value

@input_error
def birthdays(arg, contacts:AddressBook):
    bd_range = int(arg[0]) if arg else 7
    upcoming_birthdays = contacts.get_upcoming_birthdays(bd_range)
    if not contacts.data:
        return INFO + " You do not have any contacts saved"
    if not upcoming_birthdays:
        return INFO + " There are no upcoming birthdays"

    res = f"{'Name':<15}{'| Birthday':<13}{'| Phone'}\n" + "-"*42 + "\n"
    for contact in upcoming_birthdays:
        phones_iter = iter(contact.phones)
        res += (f"{contact.name.value:<15}| {contact.birthday.value:<11}"
                f"| {next(phones_iter, "-" + " "*9)}\n")
        for phone in phones_iter:
            res += f"{' ': <15}| {' ':<11}| {phone.value}\n"
    return res.strip()
