

def log_errors(f):
    """
    Простой логгер для вывода исключений в консоль
    :param f:
    :return:
    """
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка {e}'
            print(error_message)
            raise e
    return inner
