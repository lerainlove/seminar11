import json
import csv


class Task:
    FILE_PATH = "tasks.json"

    def __init__(self, id, title, description="", done=False, priority="Средний", due_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date or ""

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "priority": self.priority,
            "due_date": self.due_date
        }

    @classmethod
    def load_tasks(cls):
        try:
            with open(cls.FILE_PATH, "r") as file:
                return [cls(**task) for task in json.load(file)]
        except FileNotFoundError:
            return []

    @classmethod
    def save_tasks(cls, tasks):
        with open(cls.FILE_PATH, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, ensure_ascii=False, indent=4)

    @classmethod
    def create_task(cls, title, description="", priority="Средний", due_date=None):
        tasks = cls.load_tasks()
        task_id = len(tasks) + 1
        new_task = cls(task_id, title, description, False, priority, due_date)
        tasks.append(new_task)
        cls.save_tasks(tasks)

    @classmethod
    def list_tasks(cls):
        tasks = cls.load_tasks()
        for task in tasks:
            status = "✔" if task.done else "✖"
            print(f"ID: {task.id}, Title: {task.title}, Priority: {task.priority}, Due Date: {task.due_date}, Done: {status}")

    @classmethod
    def mark_task_done(cls, task_id):
        tasks = cls.load_tasks()
        for task in tasks:
            if task.id == task_id:
                task.done = True
                cls.save_tasks(tasks)
                return
        print("Task not found!")

    @classmethod
    def delete_task(cls, task_id):
        tasks = cls.load_tasks()
        tasks = [task for task in tasks if task.id != task_id]
        cls.save_tasks(tasks)

    @classmethod
    def export_tasks_to_csv(cls):
        tasks = cls.load_tasks()
        with open("tasks.csv", "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID", "Title", "Description", "Done", "Priority", "Due Date"])
            for task in tasks:
                writer.writerow([task.id, task.title, task.description, task.done, task.priority, task.due_date])

    @classmethod
    def import_tasks_from_csv(cls):
        with open("tasks.csv", "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            tasks = [
                cls(
                    int(row["ID"]),
                    row["Title"],
                    row["Description"],
                    row["Done"].lower() == "true",
                    row["Priority"],
                    row["Due Date"]
                )
                for row in reader
            ]
        cls.save_tasks(tasks)

