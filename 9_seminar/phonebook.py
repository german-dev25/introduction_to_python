from typing import Optional
from config import COMMANDS, DELIMITER_COL, DELIMITER_ROW


class Phonebook:
    def __init__(self):
        self.content: Optional[str] = None
        self.commands: dict = COMMANDS

    def display_commands(self, columns: list) -> None:
        self.print_separator(columns)
        print('Список команд:')
        for key, value in self.commands.items():
            print(f'{key}. {value}')
        self.print_separator(columns)

    @staticmethod
    def format_row(row: str) -> str:
        columns = row.split(DELIMITER_COL)
        formatted_columns = [column.strip().center(15) for column in columns]
        separator = DELIMITER_ROW * (
                15 * len(columns) + (len(columns) - 1) * 3)
        return f' {DELIMITER_COL} '.join(formatted_columns) + '\n' + separator

    @staticmethod
    def print_separator(columns: list) -> None:
        separator = '-' * (15 * len(columns) + (len(columns) - 1) * 3)
        print(separator)

    @staticmethod
    def exit_app():
        print('Выход из программы.')
        exit()
