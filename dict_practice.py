# ПРАКТИКА СО СЛОВАРЯМИ - ЭТАП 1

print("=== ПРАКТИКА СО СЛОВАРЯМИ ===")

# 1. СОЗДАНИЕ СЛОВАРЯ
student = {
    "имя": "Илья",
    "возраст": 33,
    "курс": "Python Backend",
    "оценки": [85, 90, 78, 92]
}
print(f"1. Словарь студента: {student}")

# 2. ДОСТУП К ЗНАЧЕНИЯМ
print(f"2. Доступ к значениям:")
print(f"   Имя: {student['имя']}")  # через ключ
print(f"   Имя (через get): {student.get('имя')}")  # безопасно
print(f"   Email (если нет): {student.get('email', 'не указан')}")

# 3. ИЗМЕНЕНИЕ И ДОБАВЛЕНИЕ
student["город"] = "Москва"
print(f"3. После добавления города: {student}")

student["возраст"] = 26
print(f"   После изменения возраста: {student}")

# 4. ПРОВЕРКА НАЛИЧИЯ КЛЮЧА
print(f"4. Проверка ключей:")
print(f"   Есть ключ 'курс'? {'курс' in student}")
print(f"   Есть ключ 'телефон'? {'телефон' in student}")

# 5. ПЕРЕБОР СЛОВАРЯ
print(f"5. Перебор словаря:")
for key, value in student.items():
    print(f"   {key}: {value}")

# 6. ПОЛЕЗНЫЕ МЕТОДЫ
print(f"6. Методы словаря:")
print(f"   Все ключи: {list(student.keys())}")
print(f"   Все значения: {list(student.values())}")

# 7. РАБОТА С ВЛОЖЕННЫМИ ДАННЫМИ
print(f"7. Работа с вложенными данными:")
average_grade = sum(student["оценки"]) / len(student["оценки"])
student["средний_балл"] = round(average_grade, 2)
print(f"   Средний балл: {student['средний_балл']}")

print("\n=== ПРАКТИКА ЗАВЕРШЕНА ===")