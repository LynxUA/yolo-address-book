from faker import Faker
import json
import os

def generate_mock_contacts(num_contacts):
    fake = Faker()
    contacts = []
    for _ in range(num_contacts):
        contact = {
            "name": fake.name(),
            "address": fake.address(),
            "phone": fake.phone_number(),
            "email": fake.email(),
            "birthday": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')
        }
        contacts.append(contact)
    return contacts

def generate_mock_notes(num_notes):
    fake = Faker()
    notes = []
    for _ in range(num_notes):
        note = {
            "title": fake.sentence(),
            "content": fake.paragraphs(),
            "tags": fake.words(nb=3)
        }
        notes.append(note)
    return notes

def save_mock_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    num_contacts = 10
    num_notes = 10

    contacts = generate_mock_contacts(num_contacts)
    notes = generate_mock_notes(num_notes)

    save_mock_data(contacts, 'mock_contacts.json')
    save_mock_data(notes, 'mock_notes.json')

    print("Макет даних створено успішно!")