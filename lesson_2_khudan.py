# task_1.1


name = input("Введіть ваше імʼя : ")
surname = input("Введіть ваше прізвище: ")
full_name = name + ' ' + surname
print(full_name)

# task_1.2
print(full_name.title())
print(full_name.lower())

# task_1.3
print((name + " ") * 5)

# task_1.4
name = input("Введіть ваше імʼя : ")
surname = input("Введіть ваше прізвище: ")

print(name.strip(), '\n', '\t', surname.strip())

full_name_new = name.strip() + ' ' + surname.strip()

# task_2.1
import math


r = int(input("Введіть радіус в см: "))

circuit = 2 * math.pi * r
area_circle = (math.pi*r)**2

print(f"Довжина кола = {circuit} см \nПлоща кола = {area_circle} см^2")
