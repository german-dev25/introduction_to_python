from pathlib import Path
from typing import Optional


class FileHandler:
    def __init__(self, phone_book, filename):
        self.filename = filename
        self.phone_book = phone_book

    def process_file(self, mode: str) -> Optional[str]:
        path = Path(self.filename)
        try:
            with path.open(mode=mode) as file:
                if mode == 'r':
                    self.phone_book.content = file.read()
                    print(f'Файл {self.filename} успешно прочтен.')
                elif mode == 'w':
                    file.write(self.phone_book.content)
                    print(f'Файл {self.filename} успешно сохранен.')
            return self.phone_book.content
        except IOError:
            print(f'Ошибка ввода-вывода файла {self.filename}.')
