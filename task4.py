contacts = {}


def parse_input(user_input):
    tokens = user_input.strip().split(" ")
    command = tokens[0].lower()
    arguments = tokens[1:]
    return command, arguments


def add_contact(username, phone):
    contacts[username] = phone
    return f"Контакт {username} з номером {phone} додано."


def change_contact(username, new_phone):
    if username in contacts:
        contacts[username] = new_phone
        return f"Номер телефону для контакту {username} змінено на {new_phone}."
    else:
        return f"Контакт {username} не знайдено."


def show_phone(username):
    if username in contacts:
        return f"Номер телефону для контакту {username}: {contacts[username]}."
    else:
        return f"Контакт {username} не знайдено."


def show_all_contacts():
    if contacts:
        result = "Список контактів:\n"
        for username, phone in contacts.items():
            result += f"{username}: {phone}\n"
        return result
    else:
        return "У вас ще немає збережених контактів."


def main():
    print("Вітаю! Це ваш консольний бот-помічник.")
    print("Доступні команди: hello, add, change, phone, all, exit")

    while True:
        user_input = input("Введіть команду: ")
        command, arguments = parse_input(user_input)

        if command == "exit" or command == "close":
            print("До зустрічі!")
            break
        elif command == "hello":
            print("Як я можу допомогти?")
        elif command == "add":
            if len(arguments) == 2:
                result = add_contact(arguments[0], arguments[1])
                print(result)
            else:
                print(
                    "Неправильне використання команди add. Введіть ім'я та номер телефону."
                )
        elif command == "change":
            if len(arguments) == 2:
                result = change_contact(arguments[0], arguments[1])
                print(result)
            else:
                print(
                    "Неправильне використання команди change. Введіть ім'я та новий номер телефону."
                )
        elif command == "phone":
            if len(arguments) == 1:
                result = show_phone(arguments[0])
                print(result)
            else:
                print("Неправильне використання команди phone. Введіть ім'я контакту.")
        elif command == "all":
            result = show_all_contacts()
            print(result)
        else:
            print("Невідома команда. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
