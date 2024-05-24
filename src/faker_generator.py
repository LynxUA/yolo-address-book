
import random
from faker import Faker

from src.decorators import input_error
from src.models.Note import Note
from src.models.NoteBook import NoteBook
from src.models.Record import Record
from src.models.AddressBook import AddressBook
from src.constants import INFO

fake = Faker()

def generate_tags():
    possible_tags = ["work", "personal", "urgent", "important", "low-priority", "ideas", "to-do"]
    num_tags = random.randint(1, len(possible_tags))
    return random.sample(possible_tags, num_tags)

@input_error
def generate_contacts(args, book: AddressBook):
    number, = args
    address_book = {}

    for _ in range(int(number)):
        name = fake.first_name()

        address_book[name] = {
            "phones": str(fake.random_number(digits=10, fix_len=True)),
            "birthday": fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=90).strftime("%d.%m.%Y"),
            "email": fake.email(),
            "address": fake.address().replace("\n", ", ")
        }
        contact = Record(name)
        contact.add_phone(address_book[name]["phones"])
        contact.add_email(address_book[name]["email"])
        contact.add_address(address_book[name]["address"])
        contact.add_birthday(address_book[name]["birthday"])

        book.add(contact)

    return INFO + f" {number} contacts successfully generated"

@input_error
def generate_notes(args, book: NoteBook):
    number, = args
    note_book = {}

    for _ in range(int(number)):
        title = fake.word().capitalize()

        note_book[title] = {
            "text": fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None),
            "tags": generate_tags()
        }

        note = Note(title, note_book[title]["text"])
        note.add_tags(note_book[title]["tags"])

        book.add(note)
        
    return INFO + f" {number} notes successfully generated"

