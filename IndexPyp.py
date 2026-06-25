FILENAME = "notes.txt"

def add_note():
    note = input("Введите заметку: ")
    if(note is None == True):
        print("Вы ничего не ввели, поэтому действие отменено)")
    else:
        with open(FILENAME, "a", encoding="utf-8") as file:
            file.write(note + "\n")
        print("Заметка сохранена!\n")


def show_notes():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            notes = file.readlines()
            if notes:
                print("\nВаши заметки:")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note.strip()}")
            else:
                print("Заметок пока нет.")
    except FileNotFoundError:
        print("Файл с заметками ещё не создан.\n")
        
def delete_notes():
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            file.writelines("");
            print("Все заметки удалены!\n")
    except FileNotFoundError:
        print("Файл с заметками ещё не создан.\n")


def main():
    while True:
        print("\n1 — Добавить заметку")
        print("2 — Показать заметки")
        print("3 — Удалить все заметки")
        print("0 — Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()