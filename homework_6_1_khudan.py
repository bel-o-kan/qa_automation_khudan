def read_side():
    """
    Функція для зчитування введеного користувачем значення сторони.
    """
    side = float(input("Введіть довжину сторони: "))
    return side

def is_rectangle(a, b, c, d):
    """
    Функція, яка перевіряє, чи є заданий чотирикутник прямокутником.
    """
    sides = [a, b, c, d]
    sides.sort()
    if sides[0] == sides[1] and sides[2] == sides[3]:
        return True
    else:
        return False

def rectangle_area(a, b):
    """
    Функція, яка знаходить площу прямокутника з заданими сторонами.
    """
    area = a * b
    return area

# Зчитуємо сторони чотирикутника
a = read_side()
b = read_side()
c = read_side()
d = read_side()

# Перевіряємо, чи є заданий чотирикутник прямокутником
if is_rectangle(a, b, c, d):
    print("Це прямокутник")
    area = rectangle_area(a, b)
    print("Площа прямокутника: ", area)
else:
    print("Це не прямокутник")
