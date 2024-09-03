import time


def get_time(func):
    def wrapper(*args, **kwargs):
        first_time = time.time()
        res = func(*args, **kwargs)
        second_time = time.time()
        execution_time = second_time - first_time
        print(f"Время выполнения: {execution_time} секунд, сумма: {res}")
        return res

    return wrapper


@get_time
def summ(x, y):
    return x + y


summ(1, 2)
