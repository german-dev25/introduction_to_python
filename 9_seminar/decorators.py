def check_content(func):
    def wrapper(self, *args, **kwargs):
        if self.phonebook.content is None:
            print('Необходимо открыть файл, прежде чем выполнить команду')
        else:
            return func(self, *args, **kwargs)
    return wrapper


def check_search(func):
    def wrapper(self, search=None, *args, **kwargs):
        if search is None or not search.strip():
            print('Необходимо ввести поисковый запрос')
        else:
            return func(self, search, *args, **kwargs)
    return wrapper