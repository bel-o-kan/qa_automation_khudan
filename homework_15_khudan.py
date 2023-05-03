# task_1
class Singleton:
    _instance = None  # зберігаємо єдиний екземпляр класу

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True


# task_2
from abc import ABC, abstractmethod

# Абстрактний клас Dish
class Dish(ABC):
    def __init__(self, name, description, ingredients):
        self.name = name
        self.description = description
        self.ingredients = ingredients

    @abstractmethod
    def get_price(self):
        pass

# Підкласи Dish
class Risotto(Dish):
    def __init__(self, name, description, ingredients):
        super().__init__(name, description, ingredients)
        self.price = 10.99

    def get_price(self):
        return self.price

class Pasta(Dish):
    def __init__(self, name, description, ingredients):
        super().__init__(name, description, ingredients)
        self.price = 8.99

    def get_price(self):
        return self.price

class Pizza(Dish):
    def __init__(self, name, description, ingredients):
        super().__init__(name, description, ingredients)

# Клас OrderPart
class OrderPart:
    def __init__(self, dish_factory):
        self.dish_factory = dish_factory

    def get_dish(self, dish_type):
        dish = self.dish_factory.create_dish(dish_type)
        return dish

# Фабрика DishFactory
class DishFactory:
    def create_dish(self, dish_type):
        if dish_type == 'risotto':
            return Risotto('Mushroom Risotto', 'A delicious mushroom risotto.', ['rice', 'mushrooms', 'cheese'])
        elif dish_type == 'pasta':
            return Pasta('Spaghetti Carbonara', 'A classic Italian dish.', ['pasta', 'bacon', 'eggs'])
        elif dish_type == 'pizza':
            return Pizza('Margherita Pizza', 'A traditional Italian pizza.', ['dough', 'tomatoes', 'cheese'])
        else:
            raise ValueError('Invalid dish type')

# Використання класу OrderPart
dish_factory = DishFactory()
order_part = OrderPart(dish_factory)

dish1 = order_part.get_dish('risotto')
dish2 = order_part.get_dish('pasta')

print(dish1.name) # Виведе: Mushroom Risotto
print(dish1.description) # Виведе: A delicious mushroom risotto.
print(dish1.ingredients) # Виведе: ['rice', 'mushrooms', 'cheese']
print(dish1.get_price()) # Виведе: 10.99

print(dish2.name) # Виведе: Spaghetti Carbonara
print(dish2.description) # Виведе: A classic Italian dish.
print(dish2.ingredients) # Виведе: ['pasta', 'bacon', 'eggs']
print(dish2.get_price()) # Виведе: 8.99

