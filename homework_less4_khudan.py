notes = []

while True:
    command = input("Введіть команду (add/earliest/latest/longest/shortest/Exit): ")

    if command == "add":
        note = input("Введіть нотатку: ")
        notes.append(note)
        print("Нотатку додано")

    elif command == "earliest":
        notes_copy = notes.copy()
        notes_copy.sort()
        print("Список нотаток від найновішої до найпізнішої:")
        for note in notes_copy:
            print(note)

    elif command == "latest":
        notes_copy = notes.copy()
        notes_copy.sort(reverse=True)
        print("Список нотаток від найпізнішої до найновішої:")
        for note in notes_copy:
            print(note)

    elif command == "longest":
        notes_copy = notes.copy()
        notes_copy.sort(key=len, reverse=True)
        print("Список нотаток від найдовшої до найкоротшоЇ:")
        for note in notes_copy:
            print(note)

    elif command == "shortest":
        notes_copy = notes.copy()
        notes_copy.sort(key=len)
        print("Список нотаток від найкоротшої до найдовшої:")
        for note in notes_copy:
            print(note)

    elif command == "Exit":
        print("До побачення!")
        break

    else:
        print("Невідома команда. Спробуйте ще раз.")
