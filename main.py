
from prompt_toolkit import PromptSession
from src.faker_generator import generate_contacts, generate_notes
from src.constants import *
from src.decorators import *
from src.handlers import *
from src.notes_handlers import all_notes, add_note_flow, change_note_flow, delete_note, find_note
from src.BookManager import BookManager
from src.utiles import parse_input

def main():
    print(BANNER)
    print(GREETING)
    #lambda accepts not used arguments to ignore extra arguments
    command_dict = {
        "hello": lambda *_: "How can I help you?",
        "close": lambda *_: exit(),
        "exit": lambda *_: exit(),
        "add": lambda contacts, _, *args: add_contact(args, contacts),
        "all": lambda contacts, *_: all_contact(contacts),
        "change": lambda contacts, _, *args: change_contact(args, contacts),
        "phone": lambda contacts, _, *args: phone_contact(args, contacts),
        "add-birthday": lambda contacts, _, *args: add_birthday(args, contacts),
        "add-email": lambda contacts, _,*args: add_email(args, contacts),
        "add-address": lambda contacts, _,*args: add_address(args, contacts),
        "show-birthday": lambda contacts, _, *args: show_birthday(args, contacts),
        "delete": lambda contacts, _, *args: delete_contact(args, contacts),
        "birthdays": lambda contacts, _, *args: birthdays(args, contacts),
        "add-note": lambda _, notes, *__: add_note_flow(notes),
        "find-note": lambda _, notes, *args: find_note(args, notes),
        "all-notes": lambda _, notes, *__: all_notes(notes),
        "change-note": lambda _, notes, *args: change_note_flow(args, notes),
        "delete-note": lambda _, notes, *args: delete_note(args, notes),
        "generate-contacts": lambda contacts, _, *args: generate_contacts(args, contacts),
        "generate-notes": lambda _, notes, *args: generate_notes(args, notes),
        "help": lambda *_: HELP,
    }
    with BookManager("address_book.json") as (contacts, notes):
        session = PromptSession()
        while True:
            try:
                command, *args = parse_input(command_dict.keys(), session)
                print(command_dict[command](contacts, notes, *args))
            except KeyError:
                print(INVALID_COMMAND)
            except SystemExit as se:
                print("Goodbye!")
                raise se

if __name__ == "__main__":
    main()
