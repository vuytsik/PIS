groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]

def filter_by_average(students, min_avg):
    print(f"Студенты со средним баллом выше {min_avg}:")
    found = False
    for student in students:
        marks = student["marks"]
        avg = sum(marks) / len(marks)
        if avg > min_avg:
            found = True
            print(f"{student['name']} {student['surname']} — ср. балл: {avg:.2f}")
    if not found:
        print("Таких студентов нет.")


try:
    user_min_avg = float(input("Введите минимальный средний балл: "))
    filter_by_average(groupmates, user_min_avg)
except ValueError:
    print("Ошибка: нужно ввести число.")