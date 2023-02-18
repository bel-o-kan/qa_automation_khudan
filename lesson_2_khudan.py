# task_1.1

#
# name = input("Введіть ваше імʼя : ")
# surname = input("Введіть ваше прізвище: ")
# full_name = name + ' ' + surname
# print(full_name)
#
# # task_1.2
# print(full_name.title())
# print(full_name.lower())
#
# # task_1.3
# print((name + " ") * 5)
#
# # task_1.4
# name = input("Введіть ваше імʼя : ")
# surname = input("Введіть ваше прізвище: ")
#
# print(name.strip(), '\n', '\t', surname.strip())
#
# full_name_new = name.strip() + ' ' + surname.strip()

# task_2.1
import math


radius = float(input("Введіть радіус: "))

circuit = 2 * math.pi * radius
area_circle = math.pi * radius ** 2

print(f"Довжина кола = {circuit:.2f} \nПлоща кола = {area_circle:.2f}")


