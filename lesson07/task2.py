# Написать декоратор, который кеширует результат исполнения функции.
# При повторном вызове с теми же аргументами функция не вызывается, а результат выдается из кэша.

# Работает если аргументы и результат - простые типы данных, также для аргументов допустимы списки и кортежи
from functools import reduce

cache = {}


def cache_decorator(func):
    def inner(*args, **kwargs):
        params_str = str({"args": args, "kwargs": kwargs})

        if params_str in cache:
            print("cached")
            return cache[params_str]
        else:
            the_result = func(*args, **kwargs)
            cache[params_str] = the_result
            return the_result

    return inner


@cache_decorator
def summa1(x, y):
    print("function is called")
    return x + y


@cache_decorator
def summa2(xarr):
    print("function is called")
    return reduce(lambda x, y: x + y, xarr)


print(summa1(1, 2))
print(summa1(1, 2))

print(summa2([1, 2, 3, 4]))
print(summa2([1, 2, 3, 4]))
