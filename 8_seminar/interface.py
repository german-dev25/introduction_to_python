def format_row(row: str) -> str:
    columns = row.split('|')
    formatted_columns = [column.strip().center(15) for column in columns]
    return ' | '.join(formatted_columns)


def display_commands(commands: dict) -> None:
    print('Список команд:')
    for key, value in commands.items():
        print(f'{key}. {value}')


def exit_app():
    print('Выход из программы.')
    exit()
