# task_1
def print_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' was called.")
        return func(*args, **kwargs)
    return wrapper

@print_function_name
def add_numbers(a, b):
    return a + b

@print_function_name
def multiply_numbers(a, b):
    return a * b

print(add_numbers(2, 3))
print(multiply_numbers(2, 3))


# task_2
from random import randint


numbers = [randint(1, 10) for _ in range(100)]
counts = {num: numbers.count(num) for num in set(numbers)}

for num, count in counts.items():
    print(f"{num} зустрічається {count} разів.")
