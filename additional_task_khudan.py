# task_1
from functools import reduce

array1 = [1, 2, 3, 4, 5, 6]
array2 = [4, 5, 6, 7, 8, 9]

intersection = list(filter(lambda x: x in array1, array2))

print(intersection)  # [4, 5, 6]

# task_2
is_number = lambda s: s.replace('.', '', 1).isdigit()

s1 = "123"
s2 = "3.14"
s3 = "hello"

print(is_number(s1))  # True
print(is_number(s2))  # True
print(is_number(s3))  # False

# task_3
words = ["hello", "world", "python", "programming", "code", "lambda"]

max_min_len = lambda lst: [max(lst, key=len), min(lst, key=len)]

print(max_min_len(words))  # ['programming', 'code']

# task_4
numbers = [1, 2, 3, 4, 5]

product = lambda lst: reduce(lambda x, y: x * y, lst)

print(product(numbers))  # 120



