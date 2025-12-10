# ПРАКТИКА СО СПИСКАМИ - ЭТАП 1

print("=== ПРАКТИКА СО СПИСКАМИ ===")

# 1. СОЗДАНИЕ СПИСКА
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"1. Исходный список: {numbers}")

# 2. ДОБАВЛЕНИЕ ЭЛЕМЕНТОВ
numbers.append(11)  # в конец
print(f"2. После append(11): {numbers}")

numbers.insert(0, 0)  # в начало
print(f"   После insert(0, 0): {numbers}")

# 3. УДАЛЕНИЕ ЭЛЕМЕНТОВ
numbers.remove(5)  # по значению
print(f"3. После remove(5): {numbers}")

popped = numbers.pop()  # последний элемент
print(f"   После pop(): удалили {popped}, список: {numbers}")

# 4. СРЕЗЫ (SLICING)
print(f"4. Срезы:")
print(f"   numbers[:3] = {numbers[:3]}")      # первые 3
print(f"   numbers[3:7] = {numbers[3:7]}")    # с 3 по 6
print(f"   numbers[-3:] = {numbers[-3:]}")    # последние 3

# 5. ПОЛЕЗНЫЕ МЕТОДЫ
print(f"5. Длина списка: {len(numbers)} элементов")
print(f"   Максимальный: {max(numbers)}")
print(f"   Минимальный: {min(numbers)}")
print(f"   Сумма: {sum(numbers)}")

# 6. СПИСКОВЫЕ ВКЛЮЧЕНИЯ (LIST COMPREHENSION)
squares = [x ** 2 for x in numbers]
print(f"6. Квадраты чисел: {squares}")

even_numbers = [x for x in numbers if x % 2 == 0]
print(f"   Чётные числа: {even_numbers}")

print("\n=== ПРАКТИКА ЗАВЕРШЕНА ===")