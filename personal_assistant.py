from note import Note
from contact import Contact
from task import Task
from finance import FinanceRecord


def main_menu():
    while True:
        print("\nДобро пожаловать в Персональный помощник!")
        print("Выберите действие:")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            manage_notes()
        elif choice == "2":
            manage_tasks()
        elif choice == "3":
            manage_contacts()
        elif choice == "4":
            manage_finances()
        elif choice == "5":
            calculator()
        elif choice == "6":
            print("Выход из приложения. До свидания!")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")


def manage_notes():
    print("\nУправление заметками:")
    print("1. Добавить новую заметку")
    print("2. Просмотреть список заметок")
    print("3. Просмотреть подробности заметки")
    print("4. Редактировать заметку")
    print("5. Удалить заметку")
    print("6. Экспорт заметок в CSV")
    print("7. Импорт заметок из CSV")
    print("8. Назад")

    choice = input("Выберите действие: ")

    if choice == "1":
        title = input("Введите заголовок заметки: ")
        content = input("Введите содержимое заметки: ")
        Note.create_note(title, content)
        print("Заметка успешно добавлена!")
    elif choice == "2":
        Note.list_notes()
    elif choice == "3":
        note_id = int(input("Введите ID заметки: "))
        note = next((n for n in Note.load_notes() if n.id == note_id), None)
        if note:
            print(f"Заметка ID {note.id}: {note.title}\nСодержание: {note.content}")
        else:
            print("Заметка не найдена.")
    elif choice == "4":
        note_id = int(input("Введите ID заметки: "))
        new_title = input("Введите новый заголовок: ")
        new_content = input("Введите новое содержимое: ")
        Note.edit_note(note_id, new_title, new_content)
        print("Заметка успешно обновлена!")
    elif choice == "5":
        note_id = int(input("Введите ID заметки для удаления: "))
        Note.delete_note(note_id)
        print("Заметка удалена.")
    elif choice == "6":
        Note.export_notes_to_csv()
        print("Заметки экспортированы в CSV.")
    elif choice == "7":
        Note.import_notes_from_csv()
        print("Заметки импортированы из CSV.")
    elif choice == "8":
        return


def manage_tasks():
    print("\nУправление задачами:")
    print("1. Добавить новую задачу")
    print("2. Просмотреть задачи")
    print("3. Отметить задачу как выполненную")
    print("4. Редактировать задачу")
    print("5. Удалить задачу")
    print("6. Экспорт задач в CSV")
    print("7. Импорт задач из CSV")
    print("8. Назад")

    choice = input("Выберите действие: ")

    if choice == "1":
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        priority = input("Выберите приоритет (Высокий/Средний/Низкий): ")
        due_date = input("Введите срок выполнения (ДД-ММ-ГГГГ): ")
        Task.create_task(title, description, priority, due_date)
        print("Задача успешно добавлена!")
    elif choice == "2":
        Task.list_tasks()
    elif choice == "3":
        task_id = int(input("Введите ID задачи для отметки как выполненной: "))
        Task.mark_task_done(task_id)
        print("Задача отмечена как выполненная.")
    elif choice == "4":
        task_id = int(input("Введите ID задачи для редактирования: "))
        new_title = input("Введите новое название: ")
        new_description = input("Введите новое описание: ")
        Task.create_task(task_id, new_title, new_description)
        print("Задача успешно обновлена!")
    elif choice == "5":
        task_id = int(input("Введите ID задачи для удаления: "))
        Task.delete_task(task_id)
        print("Задача удалена.")
    elif choice == "6":
        Task.export_tasks_to_csv()
        print("Задачи экспортированы в CSV.")
    elif choice == "7":
        Task.import_tasks_from_csv()
        print("Задачи импортированы из CSV.")
    elif choice == "8":
        return


def manage_contacts():
    print("\nУправление контактами:")
    print("1. Добавить новый контакт")
    print("2. Поиск контакта")
    print("3. Редактировать контакт")
    print("4. Удалить контакт")
    print("5. Экспорт контактов в CSV")
    print("6. Импорт контактов из CSV")
    print("7. Назад")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Введите имя контакта: ")
        phone = input("Введите номер телефона: ")
        email = input("Введите email: ")
        Contact.create_contact(name, phone, email)
        print("Контакт успешно добавлен!")
    elif choice == "2":
        search_term = input("Введите имя или номер телефона для поиска: ")
        Contact.search_contact(search_term)
    elif choice == "3":
        contact_id = int(input("Введите ID контакта для редактирования: "))
        new_name = input("Введите новое имя: ")
        new_phone = input("Введите новый номер телефона: ")
        Contact.create_contact(contact_id, new_name, new_phone)
        print("Контакт успешно обновлен!")
    elif choice == "4":
        contact_id = int(input("Введите ID контакта для удаления: "))
        Contact.delete_contact(contact_id)
        print("Контакт удален.")
    elif choice == "5":
        Contact.export_contacts_to_csv()
        print("Контакты экспортированы в CSV.")
    elif choice == "6":
        Contact.import_contacts_from_csv()
        print("Контакты импортированы из CSV.")
    elif choice == "7":
        return


def manage_finances():
    print("\nУправление финансовыми записями:")
    print("1. Добавить новую запись")
    print("2. Просмотреть все записи")
    print("3. Генерация отчёта")
    print("4. Удалить запись")
    print("5. Экспорт финансовых записей в CSV")
    print("6. Импорт финансовых записей из CSV")
    print("7. Назад")

    choice = input("Выберите действие: ")

    if choice == "1":
        amount = float(input("Введите сумму операции: "))
        category = input("Введите категорию: ")
        date = input("Введите дату (ДД-ММ-ГГГГ): ")
        description = input("Введите описание: ")
        FinanceRecord.create_record(amount, category, date, description)
        print("Финансовая запись добавлена!")
    elif choice == "2":
        FinanceRecord.list_records()
    elif choice == "3":
        start_date = input("Введите начальную дату (ДД-ММ-ГГГГ): ")
        end_date = input("Введите конечную дату (ДД-ММ-ГГГГ): ")
        FinanceRecord.create_record(start_date, end_date)
    elif choice == "4":
        record_id = int(input("Введите ID записи для удаления: "))
        FinanceRecord.delete_record(record_id)
        print("Запись удалена.")
    elif choice == "5":
        FinanceRecord.export_records_to_csv()
        print("Финансовые записи экспортированы в CSV.")
    elif choice == "6":
        FinanceRecord.import_records_from_csv()
        print("Финансовые записи импортированы из CSV.")
    elif choice == "7":
        return


def calculator():
    print("\nКалькулятор:")
    expression = input("Введите выражение для вычисления: ")
    try:
        result = eval(expression)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка в вычислении: {e}")


if __name__ == "__main__":
    main_menu()
