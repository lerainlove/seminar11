import json
import csv


class FinanceRecord:
    FILE_PATH = "finance.json"

    def __init__(self, record_id, amount, category, date, description=""):
        self.id = record_id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }

    @classmethod
    def load_records(cls):
        try:
            with open(cls.FILE_PATH, "r") as file:
                return [cls(**record) for record in json.load(file)]
        except FileNotFoundError:
            return []

    @classmethod
    def save_records(cls, records):
        with open(cls.FILE_PATH, "w") as file:
            json.dump([record.to_dict() for record in records], file, ensure_ascii=False, indent=4)

    @classmethod
    def create_record(cls, amount, category, date, description=""):
        records = cls.load_records()
        record_id = len(records) + 1
        new_record = cls(record_id, amount, category, date, description)
        records.append(new_record)
        cls.save_records(records)

    @classmethod
    def list_records(cls):
        records = cls.load_records()
        for record in records:
            print(f"ID: {record.id}, Amount: {record.amount}, Category: {record.category}, Date: {record.date}, Description: {record.description}")

    @classmethod
    def delete_record(cls, record_id):
        records = cls.load_records()
        updated_records = [record for record in records if record.id != record_id]
        cls.save_records(updated_records)
        print(f"Финансовая запись с ID {record_id} успешно удалена.")

    @classmethod
    def export_records_to_csv(cls):
        records = cls.load_records()
        with open("finance.csv", "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID", "Amount", "Category", "Date", "Description"])
            for record in records:
                writer.writerow([record.id, record.amount, record.category, record.date, record.description])

    @classmethod
    def import_records_from_csv(cls):
        with open("finance.csv", "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            records = [cls(int(row["ID"]), float(row["Amount"]), row["Category"], row["Date"], row["Description"]) for row in reader]
        cls.save_records(records)

