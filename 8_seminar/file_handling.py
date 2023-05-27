from pathlib import Path
from typing import Optional
from config import FILENAME


def process_file(mode: str,
                 content: str = None,
                 filename: str = FILENAME) -> Optional[str]:
    path = Path(filename)
    try:
        with path.open(mode=mode) as file:
            if mode == 'r':
                content = file.read()
                print(f'Файл {filename} успешно прочтен.')
            elif mode == 'w':
                file.write(content)
                print(f'Файл {filename} успешно сохранен.')
        return content
    except IOError:
        print(f'Ошибка ввода-вывода файла {filename}.')
