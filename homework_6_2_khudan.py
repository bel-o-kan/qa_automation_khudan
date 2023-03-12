import random
import string

def create_email(domains, names):
    """
    Функція для генерації e-mail в форматі:
    прізвище.число_від_100_до_999@рандомна_стрічка_букв_довжиною_від_5_до_7_символів.домен
    """
    surname = random.choice(names)
    number = random.randint(100, 999)
    letters = string.ascii_lowercase
    random_str = ''.join(random.choice(letters) for i in range(random.randint(5, 7)))
    domain = random.choice(domains)
    email = f"{surname}.{number}@{random_str}.{domain}"
    return email
names = ["king", "octopus", "python" "miller", "kean"]
domains = ["net", "org", "eu" "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)