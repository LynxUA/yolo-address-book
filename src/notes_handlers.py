from src.constants import INFO
from src.models.Note import Note
from src.models.NoteBook import NoteBook
from src.decorators import input_error
from src.utiles import parse_input_edit_note


@input_error
def add_note(notes:NoteBook, **kwargs) -> str:
    title = kwargs.get('title')
    body = kwargs.get('body')
    tags = kwargs.get('tags')
    note = Note(title, body)
    note.add_tags(tags)
    notes.add(note)
    return INFO + f" Note {title} successfully added"

@input_error
def change_note_flow(args:list[str], notes:NoteBook) -> str:
    found_note = find_note_to_update(args, notes)
    if not found_note:
        return
    print(INFO + " Note to be updated:")
    print(notes.format_notes(found_note))
    updated_note = parse_input_edit_note(found_note)
    if not updated_note:
        return
    old_title = list(found_note.keys())[0]
    change_note(notes, old_title, updated_note)

@input_error
def find_note_to_update(args:list[str], notes:NoteBook) -> str:
    search_request = " ".join(args)
    found_note: dict = find_note_data(search_request, notes)
    if not found_note:
         print(INFO + f" No notes with '{search_request}' in name or text were found")
         return
    if len(found_note) > 1:
        print(INFO + f" Multiple notes with '{search_request}' in name or text were found. Please specify the note you want to change")
        return notes.format_notes(found_note)
    return found_note

@input_error
def change_note(notes:NoteBook, old_title: str, new_note: dict) -> str:
    note = Note(new_note["title"], new_note["text"])
    note.add_tags(new_note["tags"])
    notes.update(old_title, note)
    print(INFO + " Note successfully updated")

@input_error
def delete_note(args:list[str], notes:NoteBook) -> str:
    search_request = " ".join(args)
    found_note: dict = find_note_data(search_request, notes)
    if not found_note:
        return INFO + f" No notes with '{search_request}' in name or text were found"
    if len(found_note) > 1:
        print(INFO + f" Multiple notes with '{search_request}' in name or text were found. Please specify the note you want to delete")
        return notes.format_notes(found_note)
    found_key = next(iter(found_note))
    notes.delete(found_key)
    return INFO + f" Note {found_key} successfully deleted"

@input_error
def find_note_data(search_request, notes:NoteBook) -> str:
    if "#" in search_request:
        search_request = search_request.replace("#", "")
        return notes.find_by_tag(search_request)
    else:
        notes_by_name = notes.find_by_name(search_request)
        notes_by_text = notes.find_by_text(search_request)
        if notes_by_name:
           return notes_by_name
        if notes_by_text:
           return notes_by_text

@input_error
def find_note(args:list[str], notes:NoteBook) -> Note:
    search_request, = " ".join(args),
    found_note = find_note_data(search_request, notes)
    if found_note:
        return notes.format_notes(found_note)
    return INFO + f" No notes with '{search_request}' in name or text were found"

def all_notes(notes:NoteBook) -> str:
    if not notes.data:
        return INFO + " You do not have any notes saved"
    
    return notes.format_notes(notes.data)