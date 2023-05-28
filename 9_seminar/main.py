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

        if command == 1:
            phonebook.content = file.process_file(mode='r')
        if command == 2:
            phonebook.content = file.process_file(mode='w')
        if command == 3:
            phonebook.content = content.show_all_contacts()
        if command == 4:
            phonebook.content = content.add_contact()
        if command == 5:
            phonebook.content = content.search_contact(
                search=input('Введите текст для поиска: '))
        if command == 6:
            phonebook.content = content.update_contact(
                search=input('Введите текст для поиска и обновления: '))
        if command == 7:
            phonebook.content = content.delete_contact(
                search=input('Введите текст для поиска и удаления: '))
        if command == 8:
            phonebook.exit_app()


if __name__ == "__main__":
    main()
