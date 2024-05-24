from colorama import Fore


BANNER = """
   _                                       
  /   _  ._  _|_  _.  _ _|_  _   |_   _ _|_ 
  \\_ (_) | |  |_ (_| (_  |_ _>   |_) (_) |_ 
"""
GREETING = """Hi! I am your bot-helper! I will help you to manage your contacts list.
Enter `help` for more information"""
HELP = """
hello                                                   : responds "How can I help you?" in console
add username [phone] [email] [address]                  : saves new contact
change username old_phone new_phone [email] [address]   : updates existing phone number
phone username                                          : prints phone number for username
all                                                     : prints all saved contacts
add-birthday username DD.MM.YYYY                        : add or update a birthday date for the contact
add-email username email                                : add or update an email for the contact
add-address username address                            : add or update an address for the contact
show-birthday username                                  : show birthday of the contact
delete username                                         : delete contact
birthdays [range]                                       : show upcoming birthdays in the next 7 days or, if you provide range, in the next range days
add-note                                                : saves new note. This command will ask you to enter title, text and tags each separately
find-note [search_str] or [#tag]                        : find note which contains search_str in name or text
all-notes                                               : prints all saved notes
change-note [search words]                              : updates existing note. You will see the multy-step dialog to find and update note
delete-note title                                       : delete existing note
generate-contacts [number]                              : generates random contacts. You can specify the number of contacts to generate
generate-notes [number]                                 : generates random notes. You can specify the number of notes to generate
close, exit                                             : prints "Good bye!" and finishes bot
help                                                    : prints this help"""


USE_HELP = "Use 'help' for more information"
INFO = Fore.GREEN + "[INFO]" + Fore.RESET
ERROR = Fore.RED + "[ERROR]" + Fore.RESET
INVALID_COMMAND = ERROR + " Invalid command. " + USE_HELP
NOT_EXISTS = ERROR + " This name does not exists"
UNKNOWN = ERROR + " Unknow error happend. Please try again. " + USE_HELP
UPDATED = INFO + " {class_name} {item_name} successfully updated."
DELETED = INFO + " {class_name} {item_name} successfully deleted."
