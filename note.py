import json
import csv
from datetime import datetime


class Note:
    FILE_PATH = "notes.json"

    def __init__(self, id, title, content, timestamp=None):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp or self.current_time()

    @staticmethod
    def current_time():
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):
        return {"id": self.id, "title": self.title, "content": self.content, "timestamp": self.timestamp}

    @classmethod
    def load_notes(cls):
        try:
            with open(cls.FILE_PATH, "r") as file:
                return [cls(**note) for note in json.load(file)]
        except FileNotFoundError:
            return []

    @classmethod
    def save_notes(cls, notes):
        with open(cls.FILE_PATH, "w") as file:
            json.dump([note.to_dict() for note in notes], file, ensure_ascii=False, indent=4)

    @classmethod
    def create_note(cls, title, content):
        notes = cls.load_notes()
        note_id = len(notes) + 1
        new_note = cls(note_id, title, content)
        notes.append(new_note)
        cls.save_notes(notes)

    @classmethod
    def list_notes(cls):
        notes = cls.load_notes()
        for note in notes:
            print(f"ID: {note.id}, Title: {note.title}, Timestamp: {note.timestamp}")

    @classmethod
    def view_note_details(cls, note_id):
        notes = cls.load_notes()
        for note in notes:
            if note.id == note_id:
                print(f"Title: {note.title}\nContent: {note.content}\nTimestamp: {note.timestamp}")
                return
        print("Note not found!")

    @classmethod
    def edit_note(cls, note_id, new_title=None, new_content=None):
        notes = cls.load_notes()
        for note in notes:
            if note.id == note_id:
                note.title = new_title or note.title
                note.content = new_content or note.content
                note.timestamp = cls.current_time()
                cls.save_notes(notes)
                return
        print("Note not found!")

    @classmethod
    def delete_note(cls, note_id):
        notes = cls.load_notes()
        notes = [note for note in notes if note.id != note_id]
        cls.save_notes(notes)

    @classmethod
    def export_notes_to_csv(cls):
        notes = cls.load_notes()
        with open("notes.csv", "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID", "Title", "Content", "Timestamp"])
            for note in notes:
                writer.writerow([note.id, note.title, note.content, note.timestamp])

    @classmethod
    def import_notes_from_csv(cls):
        with open("notes.csv", "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            notes = [cls(int(row["ID"]), row["Title"], row["Content"], row["Timestamp"]) for row in reader]
        cls.save_notes(notes)

