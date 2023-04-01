# task_1
import re

def check_string(string):
    pattern = "^[A-Za-z0-9_]*$"
    return bool(re.match(pattern, string))

# Приклад використання:
print(check_string("Hello_World123"))  # True
print(check_string("hello world"))    # False



# task_2
strings = ["example (.com)", "github (.com)", "stackoverflow (.com)"]

for string in strings:
    result = re.sub(r' \(.+?\)', '', string)
    print(result)


# task_3

text = input("Введіть текст: ")
formatted_text = re.sub(r'(?<!^)(?=[A-ZА-Я])', ' ', text)

print("Відформатований текст:", formatted_text)