import json

file = 'data2.json'

def menu():
    data = load()

    while True:
        print("1.Показать проекты")
        print("2.Создать проект")
        print("3.Добавить задачу")
        print("4.Показать задачи в проекте")
        print("5.Изменение статусов проектов")
        print("6.Выход")
        choice = input("введите число: ").strip()
        if choice == '1':
            show_project(data)
        elif choice == '2':
            create_project(data)
        elif choice == '3':
            add_task(data)
        elif choice == '4':
            show_task(data)
        elif choice == '5':
            status(data)
        else:
            break

def load():
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save(data):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def show_project(data):
    if not data:
        print("проекты не найден")
        return
    else:   
        for i, p in enumerate(data, 1):
            print(f"{i}. ID:{p['id']} | {p['name']} | {p['status']}")
    

def create_project(data):
    name = input("Название проекта: ").strip()
    project = {
        'id': str(len(data) + 1),
        'name': name,
        'status': 'Планирование',
        'tasks': []
    }
    data.append(project)
    save(data)
    print("проект создан")

def add_task(data):
    show_project(data)

    id = input("id проекта:").strip()
    project = next((p for p in data if p['id'] == id), None)
    if not project:
        print("проект не найден")
        return
    task = input("название задачи: ")
    if not project:
        print("задача не найдена")
        return
    project['tasks'].append({'name': task, 'done': False})
    save(data)
    print("задача добавлена")

def show_task(data):
    show_project(data)

    id = input("ID проекта: ").strip()
    project = next((p for p in data if p['id'] == id), None)
    if not project:
        print("проект не найден")
        return
    for i, t in enumerate(project['tasks'], 1):
        print(f"{i}. {t['name']}")

def status(data):
    show_project(data)

    id = input("ID проекта: ").strip()
    project = next((p for p in data if p['id'] == id), None)
    if not project:
        print("проект не найден")
        return
    print("1.Планирование")
    print("2.Реализация")
    print("3.Готов")

    coice_status = int(input("введите число: "))
    if coice_status == 1:
        project['status'] = "Планирование"
        print("изменения сохранены")
    elif coice_status == 2:
        project['status'] = "Реализация"
        print("изменения сохранены")
    elif coice_status == 3:
        project['status'] = "Готов"
        print("изменения сохранены")
    else:
        print("-_0")
    save(data)


menu()