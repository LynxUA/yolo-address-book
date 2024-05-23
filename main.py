
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from src.constants import *
from src.decorators import *
from src.handlers import *
from src.notes_handlers import all_notes, add_note, change_note, delete_note, find_note
from src.BookManager import BookManager

@interrupt_error
@input_error
def parse_input(cmd_list:list[str], session:PromptSession):
    cmd_completer = FuzzyWordCompleter(cmd_list, WORD=True)
    user_input = session.prompt("Enter a command: ",
                                completer=cmd_completer,
                                complete_style=CompleteStyle.MULTI_COLUMN,
                                reserve_space_for_menu=5,
                                auto_suggest=AutoSuggestFromHistory())
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@interrupt_error
@input_error
def parse_input_add_note(nots, callback):
    args = {}
    while True:
        title = input("Enter the title of the note: ")
        if title:
            print(INFO + " Title successfully added")
            break
        print(INVALID_COMMAND + " Title cannot be empty")

    while True:
        body = input("Enter the text of the note: ")
        if body:
            print(INFO + " Text successfully added")
            break
        print(INVALID_COMMAND + " Text cannot be empty")

    while True:
        tags = input("Enter tags separated by commas: ")
        if tags:
            print(INFO + " Tags successfully added")
            break
        print(INVALID_COMMAND + " Tags cannot be empty")

    args['title'] = title
    args['body'] = body
    args['tags'] = tags.split(",")

    return callback(nots, **args)


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
        "birthdays": lambda contacts, _, *args: birthdays(args, contacts),
        "add-note": lambda _, notes, *__: parse_input_add_note(notes, add_note),
        "find-note": lambda _, notes, *args: find_note(args, notes),
        "all-notes": lambda _, notes, *__: all_notes(notes),
        "change-note": lambda _, notes, *args: change_note(args, notes),
        "delete-note": lambda _, notes, *args: delete_note(args, notes),
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
            except SystemExit:
                print("Goodbye!")
                raise SystemExit

if __name__ == "__main__":
    main()
