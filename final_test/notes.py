import json
import datetime

def read_notes():
    try:
        with open('notes.json', 'r', encoding='utf8') as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open('notes.json', 'w', encoding='utf8') as f:
        json.dump(notes, f)

def get_notes(query=None):
    notes = read_notes()
    if query:
        notes = [note for note in notes if note['date'] == query]
    if not notes:
        print("Notes list empty")
    return notes

def view_note(note_id):
    notes = read_notes()
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        return note
    else:
        return None        

def add_note():
    title = input("Please enter note's title: ")
    body = input("Please enter note's body: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {'id': len(notes) + 1, 'title': title, 'body': body, 'timestamp': timestamp}
    notes.append(note)
    save_notes(notes)
    print("Thank you. Your note added.")

def edit_note():
    note_id = int(input("Please enter note's id for editing: "))
    for note in notes:
        if note['id'] == note_id:
            title = input("Please enter note's updated title: ")
            body = input("Please enter note's updated body: ")
            note['title'] = title
            note['body'] = body
            note['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_notes(notes)
            print("Thank you. Your note updated.")
        else:
            print("Sorry. This note cannot be found.")

def delete_note():
    note_id = int(input("Please enter note's id for deleting: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Thank you. Note deleted.")
        else:
            print("Sorry. This note cannot be found.")

def print_notes():
    for note in notes:
        print(f'id: {note["id"]}, Title: {note["title"]}, body: {note["body"]}, creation / modification time: {note["timestamp"]}')

notes = read_notes()


def action():
    print("Welcome to notes' menu.\n \nPress 1 to add new note  \nPress 2 to edit note \nPress 3 to delete note \nPress 4 to show all notes \nPress 0 to exit \n")
    while True:
        command = input("Please enter your choice: ")
        if command == '1':
            add_note()
        elif command == '2':
            edit_note()
        elif command == '3':
            delete_note()
        elif command == '4':
            print_notes()
        elif command == '0':
            print("Good bye.")
            break
        else:
            print("Unidentified command.")

action()