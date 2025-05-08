import logging
from functools import wraps


handlers = [logging.FileHandler('log.log'),
            logging.StreamHandler()]
logging.basicConfig(handlers=handlers,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)-8s - %(message)s')


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f'Вызов функции: {func.__name__} '
                     f'с аргументами args: {args} и kwargs: {kwargs} '
                     f'и результатом {result}')
        func(*args, **kwargs)
    return wrapper


@log_decorator
def greeting(name):
    print(f"Hello, {name}!")


your_name = "Ilya"
greeting(your_name)


