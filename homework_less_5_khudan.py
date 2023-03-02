# Task_1
# перший варіант
# Два вихідних списки чисел
list_1 = [1, 34, 3,  23, 13, 3, 5]
list_2 = [34, 4, 13, 25, 1, 16, 5, 1, 16, 5]
# Використовуємо функцію set() для отримання унікальних елементів кожного списку
set_1 = set(list_1)
set_2 = set(list_2)
# Знаходимо спільні елементи, використовуючи функцію перетину множин
common_elements = list(set_1.intersection(set_2))
# сортуємо отриманий результат
common_elements.sort()
print("Спільні елементи у порядку зростання:", common_elements)


# другий варіант (мені більше сподобався

# Два вихідних списки чисел
list_1 = [1, 34, 3,  23, 13, 3, 5]
list_2 = [34, 4, 13, 25, 1, 16, 5, 1, 16, 5]

# Використовуємо функцію set() для отримання унікальних елементів кожного списку
set1 = set(list_1)
set2 = set(list_2)

# Знаходимо спільні елементи, використовуючи оператор перетину множин &
common_elements = sorted(set1 & set2)

# Виводимо спільні елементи у порядку зростання
print("Спільні елементи у порядку зростання:", common_elements)


# task_2
# Створення словника з балами студентів
students = {
    'Іван': 86,
    'Марія': 90,
    'Петро': 75,
    'Олексій': 80,
    'Наталя': 95
}

# Обчислення середнього балу
average = sum(students.values()) / len(students)
# Виведення імен студентів з балами вищими за середній
# використовуємо спискове включення, щоб знайти імена студентів з балами вищими за середній
above_average = [name for name, score in students.items() if score > average]
print("Середній бал:", average)
print("Студенти з балами вищими за середній:", above_average)


# task_3
# введення списку цілих чисел
num_list = list(map(int, input("Введіть список цілих чисел, розділених пробілами: ").split()))

# створення множини унікальних значень та визначення її довжини
num_set = set(num_list)
num_count = len(num_set)

# виведення кількості різних значень
print("Кількість різних значень: ", num_count)


# task_4
# Введення двох списків чисел
list1 = list(map(int, input("Введіть числа першого списку через пробіл: ").split()))
list2 = list(map(int, input("Введіть числа другого списку через пробіл: ").split()))

# Створення множин чисел, що містяться в обох списках
set1 = set(list1)
set2 = set(list2)
common_set = set1.intersection(set2)

# Сортування та виведення чисел, що належать обом множинам
common_list = sorted(list(common_set))
for num in common_list:
    print(num)


# task_5
words = ('one', 'two', 'three', 'one', 'four', 'five', 'seven', 'ten', 'seven', 'one')

# створення словника та підрахунок кількості кожного слова
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1

    else:
        freq[word] = 1

# виведення слів та їхніх частот
for word, count in freq.items():
    print(f"({word}:{count})", end=' ')