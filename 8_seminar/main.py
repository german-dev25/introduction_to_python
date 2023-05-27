from typing import Optional

from config import COMMANDS, FILENAME
from file_handling import process_file
from content_handling import show_all_contacts, add_contact, search_contact, \
    update_contact, delete_contact
from interface import display_commands, exit_app


def main():
    phonebook_content: Optional[str] = None

    while True:
        display_commands(COMMANDS)
        command = int(input('Введите номер команды: '))
        if command == 1:
            phonebook_content = process_file(mode='r',
                                             filename=FILENAME)
        if command == 2:
            phonebook_content = process_file(mode='w',
                                             content=phonebook_content,
                                             filename=FILENAME)
        if command == 3:
            phonebook_content = show_all_contacts(content=phonebook_content)
        if command == 4:
            phonebook_content = add_contact(content=phonebook_content)
        if command == 5:
            search = input('Введите текст для поиска: ')
            phonebook_content = search_contact(content=phonebook_content,
                                               search=search)
        if command == 6:
            search = input('Введите текст для поиска и обновления: ')
            phonebook_content = update_contact(content=phonebook_content,
                                               search=search)
        if command == 7:
            search = input('Введите текст для поиска и удаления: ')
            phonebook_content = delete_contact(content=phonebook_content,
                                               search=search)
        if command == 8:
            exit_app()


main()
