from itertools import zip_longest
from src.constants import ERROR, INFO, UPDATED
from src.decorators import input_error
from src.models.AddressBook import AddressBook
from src.models.Record import Record

@input_error
def add_contact(args:list[str], contacts:AddressBook) -> str:
    defaults = [None, None, None, None, []]
    name, phone, email, address, *rest = (item for item, _ in zip_longest(args, defaults, fillvalue=None))
    if address and len(rest) > 0:
        address = address + "".join(rest)
    if not name:
        raise ValueError
    contact = contacts.find_by_name(name)
    msg =  UPDATED.format(class_name = "Contact",item_name = name)

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
    contact = contacts.find_by_name(name)

    if not contact:
        raise KeyError
    contact.edit_phone(old_phone, new_phone)
    if email:
        contact.add_email(email)
    if address:
        contact.add_address(address)
    return UPDATED.format(name)

@input_error
def phone_contact(args:list[str], contacts:AddressBook) -> str:
    name, = args
    contact = contacts.find_by_name(name)
    if not contact:
        raise KeyError
    return str(contact.phones)

def all_contact(contacts:AddressBook) -> str:
    if not contacts.data:
        return INFO + " You do not have any contacts saved"

    all = f"{'Name':<15}{'| Birthday':<14}{'| Phone':<13}{'| Email':<23}{'| Address'}\n" + "-"*80 + "\n"
    for name in contacts.data:
        phones_iter = contacts[name].phones.__iter__()
        birthday = contacts[name].birthday.value.strftime("%d.%m.%Y") if contacts[name].birthday else "-"
        email = contacts[name].email.value if contacts[name].email else "-"
        address = contacts[name].address.value  if contacts[name].address else "-"
        all += f"{name: <15}| {birthday: <12}| {next(phones_iter)} | {email: <20} | {address}\n"

        for phone in phones_iter:
            all += f"{' ': <15}| {' ': <12} | {phone} | {' ': <20} | {' '}\n"
    return all.strip()

@input_error
def add_birthday(args:list[str], contacts:AddressBook):
    name, birthday, = args
    contact = contacts.find_by_name(name)
    if not contact:
        raise KeyError
    contact.add_birthday(birthday)
    return UPDATED.format(name)

@input_error
def add_email(args:list[str], contacts:AddressBook):
    name, email, = args
    contact = contacts.find(name)
    if not contact:
        raise KeyError
    contact.add_email(email)
    return UPDATED.format(name)

@input_error
def add_address(args:list[str], contacts:AddressBook):
    name, *rest = args
    if len(rest) == 0:
        raise ValueError
    address = " ".join(rest)
    contact = contacts.find(name)
    if not contact:
        raise KeyError
    contact.add_address(address)
    return UPDATED.format(name)

@input_error
def show_birthday(args:list[str], contacts:AddressBook):
    name, = args
    contact = contacts.find_by_name(name)
    if not contact:
        raise KeyError
    if not contact.birthday:
        return ERROR + "Conntact does not have saved birthday date"
    return contact.birthday.value.strftime("%d.%m.%Y")

@input_error
def birthdays(arg, contacts:AddressBook):
    range = int(arg[0]) if arg else 7
    upcoming_birthdays = contacts.get_upcoming_birthdays(range)
    if not contacts.data:
        return INFO + " You do not have any contacts saved"
    if not upcoming_birthdays:
        return INFO + " There are no upcoming birthdays"

    res = f"{'Name':<15}{'| Birthday':<12}{'| Phone'}\n" + "-"*42 + "\n"
    for contact in upcoming_birthdays:
        phones_iter = contact.phones.__iter__()
        res += f"{contact.name.value: <15}| {contact.birthday.value.strftime("%d.%m.%Y"):<12}| {next(phones_iter).value}\n"
        for phone in phones_iter:
            res += f"{' ': <15}| {' ':<12}| {phone.value}\n"
    return res.strip()
