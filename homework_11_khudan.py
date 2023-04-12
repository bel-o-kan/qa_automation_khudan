# task_1
class Cat:
    species = "Red cat"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} говорить мяу!")

    @staticmethod
    def sleep(hours):
        print(f"Кіт спить {hours} годин на добу.")


Cat.sleep(18)


# task_2
class Acme:
    company_name = "Acme Corporation"  # назва компанії
    employee_count = 0  # кількість працівників

    def __init__(self, name, title):
        self.name = name  # ім'я працівника
        self.title = title  # посада працівника
        Acme.employee_count += 1

    def work(self):
        print(f"{self.name} працює на посаді {self.title}.")

    @classmethod
    def get_employee_count(cls):
        print(f"Кількість працівників в компанії {cls.company_name}: {cls.employee_count}")


Acme.get_employee_count()

