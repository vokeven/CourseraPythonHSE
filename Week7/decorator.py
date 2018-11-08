# Тестовый декоратор

from datetime import datetime
import functools

def my_timer(func, file):
    def wrapper(*args, **kwargs):
        print('Вызов функции: ', func.__name__)
        print(args)
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now() - start
        print('Время выполнения: ', end)
        return
    return wrapper


def memoized(func):
    cache={}
    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = args, tuple(sorted(kwargs.items()))
        if key not in cache:
            print('Вход в кэш')
            print('key: ', key)
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return inner


@memoized
def sum_range(n, *args, **kwargs):
    l = []
    for i in range(n):
        if i % 2 != 0:
            l.append(i)
    return l


sum_range(9**4, **{'a':2, 'b':7})



def square(func):
    return lambda x: func(x * x)


def addsome(func):
    return lambda x: func(x + 42)

@square
@addsome
def identity(x):
    return x+1


print(identity(2))
