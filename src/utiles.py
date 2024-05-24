
import textwrap

from src.constants import INFO, INVALID_COMMAND

def wrap_text(text, width, initial_indent, subsequent_indent):
    return textwrap.fill(text, width=width, initial_indent=initial_indent, subsequent_indent=subsequent_indent)

def parse_input_add_note():
    created_note = {}
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

    created_note['title'] = title
    created_note['body'] = body
    created_note['tags'] = tags.split(",")

    return created_note

def parse_input_edit_note(old_note: dict):
    title_to_be_updated = list(old_note.keys())[0]
    note_to_be_updated = old_note[title_to_be_updated]
    body_to_be_updated = note_to_be_updated.text
    tags_to_be_updated = list(note_to_be_updated.tags)

    updated_note = {"title": title_to_be_updated, "text": body_to_be_updated, "tags": tags_to_be_updated}
    
    while True:
        new_title = input(f"Enter the new title of the note or press Enter to keep the old one (current title: {title_to_be_updated}): ")
        if not new_title:
            print(INFO + " Keep the title the same as it was before")
            break
        print(INFO + " Title successfully updated")
        updated_note["title"] = new_title
        break
    while True:
        new_body = input(f"Enter the new text of the note or press Enter to keep the old one (current text: {body_to_be_updated}): ")
        if not new_body:
            print(INFO + " Keep text the same as was before")
            break
        print(INFO + " Text successfully updated")
        updated_note["text"] = new_body
        break
    while True:
        new_tags = input(f"Enter new tags separated by commas or press Enter to keep the old ones (current tags: {', '.join(tags_to_be_updated)}): ")
        if not new_tags:
            print(INFO + " Keep tags the same as they were before")
            break
        print(INFO + " Tags successfully updated")
        updated_note["tags"] = new_tags.split(",")
        break

    if (title_to_be_updated == updated_note["title"] and
            body_to_be_updated == updated_note["text"] and
            tags_to_be_updated == updated_note["tags"]):
        return
    
    return updated_note
    
