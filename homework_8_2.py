'''Створіть обробку одного будь-якого exception, який не використався як приклад на занятті.
Виведіть результат в консоль'''
# try:
#     with open("nonexistent_file.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found!")


'''Реалізуйте функцію, яка додає або віднімає від заданої дати певну кількість днів. 
Приймає на вхід будь-яку дату та час (datetime), а також значення днів(int), 
і знак(True або False, які репрезентують + і -). Повертає datetime. 
В цій задачі скористайтесь datetime.timedelta'''
# from datetime import datetime, timedelta

# date1 = datetime.now()
# def add_or_subtract_days(date: datetime, days: int, sign: bool) -> datetime:
#     if sign:
#         new_date = date + timedelta(days=days)
#     else:
#         new_date = date - timedelta(days=days)
#     return new_date
#
# print(add_or_subtract_days(date1, 5, True))

'''Реалізуйте функцію, яка вираховує ваш точний вік(не обов'язково вказувати свої данні), 
вираховуючі різницю між наданим значеням і значенням datetime.now(). 
Приймає дату та час(datetime), повертає два значення: datetime і datetime.timestamp. 
В цій задачі скористайтесь для конвертації datetime.timestamp. Виведіть результат в консоль'''

import datetime

birthdate = datetime.datetime(1986, 8, 5, 12, 30)
def calculate_age(birthdate):
    today = datetime.datetime.now()
    age = today.year - birthdate.year
    age_date = datetime.datetime(today.year - age, birthdate.month, birthdate.day, birthdate.hour, birthdate.minute)
    age_timestamp = age_date.timestamp()
    return age, age_timestamp

age, age_timestamp = calculate_age(birthdate)

print("Your age is:", age)
print("Timestamp of your last birthday:", age_timestamp)





