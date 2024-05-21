from src.constants import INFO, UPDATED
from src.models.Note import Note
from src.models.NoteBook import NoteBook
from src.decorators import input_error


@input_error
def add_note(args:list[str], notes:NoteBook) -> str:
    name, *text = args
    notes.add(Note(name, " ".join(text)))
    return INFO + f" Note {name} successfully added"

@input_error
def change_note(args:list[str], notes:NoteBook) -> str:
    name, *text = args
    note = notes.get(name)
    if not note:
        raise KeyError
    note.text = " ".join(text)
    return UPDATED.format(class_name = "Note",item_name = name)

@input_error
def delete_note(args:list[str], notes:NoteBook) -> str:
    name, = args
    notes.delete(name)
    return INFO + f" Note {name} successfully deleted"

@input_error
def find_note(args:list[str], notes:NoteBook) -> str:
    search_request, = args
    if not notes.data:
        return INFO + " You do not have any notes saved"
    notes_by_name = notes.find_by_name(search_request)
    notes_by_text = notes.find_by_text(search_request)
    res =""
    if notes_by_name:
        res += "-"*30 + "\nNotes with matching name\n" + "-"*30 + "\n"
    for note in notes_by_name:
        res += str(note)+"\n"+ "-"*30 + "\n"
    if notes_by_text:
        res += "Notes with matching text\n" + "-"*30 + "\n"
    for note in notes_by_text:
        res += str(note)+"\n"+ "-"*30 + "\n"
    if not res:
        return INFO + f" No notes with '{search_request}' in name or text were found"
    return res.strip()

def all_notes(notes:NoteBook) -> str:
    if not notes.data:
        return INFO + " You do not have any notes saved"
    res=""
    for note in notes.values():
        res += str(note)+"\n"+ "-"*30 + "\n"
    return res.strip()
