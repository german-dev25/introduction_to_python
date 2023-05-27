from typing import Optional, List
from decorators import check_search, check_content
from interface import format_row
from config import COLUMNS


@check_content
def show_all_contacts(content: str) -> Optional[str]:
    content_list = content.split('\n')
    for row in content_list:
        formatted_row = format_row(row)
        print(formatted_row)
    return content


@check_content
def add_contact(content: str) -> str:
    data_list = [input(column + ': ') or 'Отсутствует' for column in COLUMNS]
    new_contact = ' | '.join(data_list) + '\n'
    return content + new_contact


@check_content
@check_search
def search_contact(content: str = None,
                   search: str = None) -> str:
    data = search_and_make_choice(content, search, 'отображения')
    if data is not None:
        _, matched_lines, line_index = data
        searched_line = matched_lines[line_index]
        print(format_row(searched_line))
    return content


@check_content
@check_search
def update_contact(content: str = None,
                   search: str = None) -> str:
    data = search_and_make_choice(content, search, 'изменения')
    if data is not None:
        lines, matched_lines, line_index = data
        new_row = input('Введите новое значение для строки: ')
        updated_lines = [new_row if line == matched_lines[line_index] else line
                         for line in lines]
        updated_data = '\n'.join(updated_lines)
        return updated_data
    return content


@check_content
@check_search
def delete_contact(content: str = None,
                   search: str = None) -> str:
    data = search_and_make_choice(content, search, 'удаления')
    if data is not None:
        lines, matched_lines, line_index = data
        deleted_line = matched_lines[line_index]
        updated_lines = [line for line in lines if line != deleted_line]
        deleted_data = '\n'.join(updated_lines)
        return deleted_data
    return content


def search_and_make_choice(content: str,
                           search_text: str,
                           operation: str) -> Optional[list]:
    all_lines = content.split('\n')
    matched_lines = [line for line in all_lines if search_text in line]
    print_matched_lines(matched_lines)

    selected_line = get_user_choice(len(matched_lines), operation)
    if selected_line is None:
        return None

    line_index = selected_line - 1
    if 0 <= line_index < len(matched_lines):
        return [all_lines, matched_lines, line_index]
    else:
        print('Некорректный номер строки.')
        return None


def get_user_choice(max_value: int,
                    operation: str) -> Optional[int]:
    choice = input(
        f'Введите номер строки (1-{max_value}) '
        f'для {operation} (или 0 для отмены): ')
    if choice == '0':
        return None
    elif choice.isnumeric():
        choice = int(choice)
        if 1 <= choice <= max_value:
            return choice
    print('Некорректный ввод.')
    return None


def print_matched_lines(matched_lines: List[str]) -> None:
    if not matched_lines:
        print('Нет совпадений.')
    else:
        for i, line in enumerate(matched_lines, start=1):
            print(f'{i}. {line}')
