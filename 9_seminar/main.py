from config import COMMANDS, FILENAME, COLUMNS
from file_handling import FileHandler
from content_handling import ContentHandler
from phonebook import Phonebook


def main():
    phonebook = Phonebook()
    content = ContentHandler(phonebook)
    file = FileHandler(phonebook, filename=FILENAME)

    while True:
        phonebook.display_commands(COLUMNS)
        command = input('Введите номер команды: ')

        if not command.isdigit() or int(command) not in COMMANDS:
            print('Некорректный ввод. Введите число от 1 до 8.')
            continue
        command = int(command)

        phonebook.content = eval(COMMANDS[command][1])


if __name__ == "__main__":
    main()
