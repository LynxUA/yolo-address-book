
# import pickle
# from src.serialization.pickle_serialization_strategy import PickleSerializationStrategy
from src.constants import *
from src.decorators import *
from src.handlers import *
from src.notes_handlers import all_notes, add_note, change_note, delete_note, find_note
from src.BookManager import BookManager

@interrupt_error
@input_error
def parse_input():
    user_input = input("Enter a command: ")
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print(BANNER)
    print(GREETING)
    #lambda accepts not used arguments to ignore extra arguments
    command_dict = {
        "hello": lambda contacts, notes, *args: "How can I help you?",
        "close": lambda contacts, notes, *args: exit(),
        "exit": lambda contacts, notes, *args: exit(),
        "add": lambda contacts, notes, *args: add_contact(args, contacts),
        "all": lambda contacts, notes, *args: all_contact(contacts),
        "change": lambda contacts, notes, *args: change_contact(args, contacts),
        "phone": lambda contacts, notes, *args: phone_contact(args, contacts),
        "add-birthday": lambda contacts, notes, *args: add_birthday(args, contacts),
        "add-email": lambda contacts, notes,*args: add_email(args, contacts),
        "add-address": lambda contacts, notes,*args: add_address(args, contacts),
        "show-birthday": lambda contacts, notes, *args: show_birthday(args, contacts),
        "birthdays": lambda contacts, notes, *args: birthdays(args, contacts),
        "add-note": lambda contacts, notes, *args: add_note(args, notes),
        "find-note": lambda contacts, notes, *args: find_note(args, notes),
        "all-notes": lambda contacts, notes, *args: all_notes(notes),
        "change-note": lambda contacts, notes, *args: change_note(args, notes),
        "delete-note": lambda contacts, notes, *args: delete_note(args, notes),
        "help": lambda contacts, notes, *args: HELP,
    }
    # Note: The line of code above is used to make testing my feature easier. When you comment out the line of code below, you can run it insead of current line of code.
    # BookManager("address_book.pkl", PickleSerializationStrategy(), "rb", "wb", pickle.PickleError)
    with BookManager("address_book.json") as (contacts, notes):
        while True:
            try:
                command, *args = parse_input()
                print(command_dict[command](contacts, notes, *args))
            except KeyError:
                print(INVALID_COMMAND)
            except SystemExit:
                print("Goodbye!")
                raise SystemExit

if __name__ == "__main__":
    main()
