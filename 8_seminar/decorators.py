def check_content(func):
    def wrapper(content, *args, **kwargs) -> None:
        if content is None:
            print('Необходимо открыть файл, прежде чем выполнить команду')
        else:
            return func(content, *args, **kwargs)

    return wrapper


def check_search(func):
    def wrapper(content, search=None, *args, **kwargs) -> None:
        if search is None or not search.strip():
            print('Необходимо ввести поисковый запрос')
        else:
            return func(content, search, *args, **kwargs)

    return wrapper
