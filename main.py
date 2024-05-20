
from src.AddressBookManager import AddressBookManager
from src.constants import *
from src.decorators import *
from src.handlers import *

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
        "hello": lambda contacts, *args: "How can I help you?",
        "close": lambda contacts, *args: exit(),
        "exit": lambda contacts, *args: exit(),
        "add": lambda contacts, *args: add_contact(args, contacts),
        "all": lambda contacts, *args: all_contact(contacts),
        "change": lambda contacts, *args: change_contact(args, contacts),
        "phone": lambda contacts, *args: phone_contact(args, contacts),
        "add-birthday": lambda contacts, *args: add_birthday(args, contacts),
        "show-birthday": lambda contacts, *args: show_birthday(args, contacts),
        "birthdays": lambda contacts, *args: birthdays(contacts),
        "help": lambda contacts, *args: HELP,
    }
    with AddressBookManager("contacts.bin") as contacts:
        while True:
            try:
                command, *args = parse_input()
                print(command_dict[command](contacts, *args))
            except KeyError:
                print(INVALID_COMMAND)
            except SystemExit:
                print("Goodbye!")
                raise SystemExit

if __name__ == "__main__":
    main()
