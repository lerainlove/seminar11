import json
import csv

class Contact:
    FILE_PATH = "contacts.json"

    def __init__(self, id, name, phone="", email=""):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"id": self.id, "name": self.name, "phone": self.phone, "email": self.email}

    @classmethod
    def load_contacts(cls):
        try:
            with open(cls.FILE_PATH, "r") as file:
                return [cls(**contact) for contact in json.load(file)]
        except FileNotFoundError:
            return []

    @classmethod
    def save_contacts(cls, contacts):
        with open(cls.FILE_PATH, "w") as file:
            json.dump([contact.to_dict() for contact in contacts], file, ensure_ascii=False, indent=4)

    @classmethod
    def create_contact(cls, name, phone="", email=""):
        contacts = cls.load_contacts()
        contact_id = len(contacts) + 1
        new_contact = cls(contact_id, name, phone, email)
        contacts.append(new_contact)
        cls.save_contacts(contacts)

    @classmethod
    def list_contacts(cls):
        contacts = cls.load_contacts()
        for contact in contacts:
            print(f"ID: {contact.id}, Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    @classmethod
    def search_contact(cls, search_term):
        contacts = cls.load_contacts()
        found_contacts = [c for c in contacts if search_term.lower() in c.name.lower() or search_term in c.phone]
        if not found_contacts:
            print("No contacts found.")
        for contact in found_contacts:
            print(f"ID: {contact.id}, Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    @classmethod
    def delete_contact(cls, contact_id):
        contacts = cls.load_contacts()
        contacts = [c for c in contacts if c.id != contact_id]
        cls.save_contacts(contacts)

    @classmethod
    def export_contacts_to_csv(cls):
        contacts = cls.load_contacts()
        with open("contacts.csv", "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID", "Name", "Phone", "Email"])
            for contact in contacts:
                writer.writerow([contact.id, contact.name, contact.phone, contact.email])

    @classmethod
    def import_contacts_from_csv(cls):
        with open("contacts.csv", "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            contacts = [cls(int(row["ID"]), row["Name"], row["Phone"], row["Email"]) for row in reader]
        cls.save_contacts(contacts)

