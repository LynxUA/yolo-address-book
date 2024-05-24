
import textwrap

from src.constants import INFO, INVALID_COMMAND

def wrap_text(text, width, initial_indent, subsequent_indent):
    return textwrap.fill(text, width=width, initial_indent=initial_indent, subsequent_indent=subsequent_indent)

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

def parse_input_edit_note(old_note: dict):
    title_to_be_updated = list(old_note.keys())[0]
    note_to_be_updated = old_note[title_to_be_updated]
    body_to_be_updated = note_to_be_updated.text
    tags_to_be_updated = list(note_to_be_updated.tags)

    updated_note = {"title": title_to_be_updated, "text": body_to_be_updated, "tags": tags_to_be_updated}
    
    while True:
        new_title = input(f"Enter the new title of the note (current title: {title_to_be_updated}): ")
        if new_title == "":
            print(INFO + " Keep title the same as was before")
            break
        if new_title:
            print(INFO + " Title successfully updated")
            updated_note["title"] = new_title
            break
        print(INVALID_COMMAND + " Title cannot be empty")
    while True:
        new_body = input(f"Enter the new text of the note (current text: {body_to_be_updated}): ")
        if new_body == "":
            print(INFO + " Keep text the same as was before")
            break
        if new_body:
            print(INFO + " Text successfully updated")
            updated_note["text"] = new_body
            break
        print(INVALID_COMMAND + " Text cannot be empty")
    while True:
        new_tags = input(f"Enter new tags separated by commas (current tags: {', '.join(tags_to_be_updated)}): ")
        if new_tags == "":
            print(INFO + " Keep tags the same as were before")
            break
        if new_tags:
            print(INFO + " Tags successfully updated")
            updated_note["tags"] = new_tags.split(",")
            break

    if (title_to_be_updated == updated_note["title"] and
            body_to_be_updated == updated_note["text"] and
            tags_to_be_updated == updated_note["tags"]):
        print(INFO + " No changes were made")
        return None
    
    return updated_note
    


