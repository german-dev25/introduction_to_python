COMMANDS = {
    1: ['Открыть файл',
        'file.process_file(mode="r")'],
    2: ['Сохранить файл',
        'file.process_file(mode="w")'],
    3: ['Показать все контакты',
        'content.show_all_contacts()'],
    4: ['Добавить контакт',
        'content.add_contact()'],
    5: ['Найти контакт',
        'content.search_contact(search=input("Введите текст для поиска: "))'],
    6: ['Изменить контакт',
        'content.update_contact(search=input("Введите текст для поиска и обновления: "))'],
    7: ['Удалить контакт',
        'content.delete_contact(search=input("Введите текст для поиска и удаления: "))'],
    8: ['Выход',
        'phonebook.exit_app()']
}

FILENAME = 'phonebook.txt'
COLUMNS = ['Имя', 'Фамилия', 'Номер телефона', 'Комменатрий']
DELIMITER_COL = '|'
DELIMITER_ROW = '*'
