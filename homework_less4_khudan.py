# словник буде наповнюватися кожного разу, після виконання команди "add"
notes = []

# цикл while, працює доти, доки користувач не введе команду "Exit".
while True:
    command = input("Введіть команду (add/earliest/latest/longest/shortest/Exit): ")
# наповнення словника
    if command == "add":
        note = input("Введіть нотатку: ")
        notes.append(note)
        print("Нотатку додано")
# сортуємо список нотаток від найновішої до найпізнішої
    elif command == "earliest":
        notes_copy = notes.copy()
        notes_copy.sort()
        print("Список нотаток від найновішої до найпізнішої:")
        for note in notes_copy:
            print(note)
# сортуємо список нотаток від найпізнішої до найновішої
    elif command == "latest":
        notes_copy = notes.copy()
        notes_copy.sort(reverse=True)
        print("Список нотаток від найпізнішої до найновішої:")
        for note in notes_copy:
            print(note)
# сортуємо список нотаток від найдовшої до найкоротшої
    elif command == "longest":
        notes_copy = notes.copy()
        notes_copy.sort(key=len, reverse=True)
        print("Список нотаток від найдовшої до найкоротшої:")
        for note in notes_copy:
            print(note)
# сортуємо список нотаток від найкоротшої до найдовшої
    elif command == "shortest":
        notes_copy = notes.copy()
        notes_copy.sort(key=len)
        print("Список нотаток від найкоротшої до найдовшої:")
        for note in notes_copy:
            print(note)
# зупиняємо цикл по команді
    elif command == "Exit":
        print("До побачення!")
        break
# обробляємо невідому команду
    else:
        print("Невідома команда. Спробуйте ще раз.")
