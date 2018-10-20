# На map, filter, reduce написать программу, которая проверяет, является ли строка палиндромом
import time
from functools import reduce

ex = "was it a car or a cat i saw"

# убрать пробелы
ex = list(filter(lambda x: x != ' ', ex))

part1 = ex[0:int(len(ex) / 2)]
part2 = ex[len(ex):int((len(ex) - 1) / 2):-1]

# noinspection PyTypeChecker
arr_2 = [True] + list(zip(part1, part2))

result = reduce(lambda x, y: x and y[0] == y[1], arr_2)

print(result)


# Написать декоратор, который замеряет время работы функции и выводит его
def measure_time_decorator(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        the_result = func(*args, **kwargs)
        print("execution took {}".format(time.time() - start_time))
        return the_result

    return inner


@measure_time_decorator
def long_exec():
    time.sleep(1)
    print("finished")


long_exec()


# Переписать декоратор так, чтобы его можно было включать и выключать

def measure_time_decorator_with_switch(enabled=True):
    def new_measure_time_decorator(func):
        def inner(*args, **kwargs):
            start_time = time.time()
            the_result = func(*args, **kwargs)
            print("execution took {}".format(time.time() - start_time))
            return the_result

        return inner if enabled else func

    return new_measure_time_decorator


@measure_time_decorator_with_switch(enabled=True)
def long_exec_3():
    time.sleep(1)
    print("finished1")


@measure_time_decorator_with_switch(enabled=False)
def long_exec_4():
    time.sleep(1)
    print("finished2")


long_exec_3()
long_exec_4()


# Написать три декоратора, каждый декоратор выводит свое имя, так, чтобы можно было написать их один над другим:

def first_decorator(func):
    def inner(*args, **kwargs):
        print("I'm first")
        the_result = func(*args, **kwargs)
        return the_result

    return inner


def second_decorator(func):
    def inner(*args, **kwargs):
        print("I'm second")
        the_result = func(*args, **kwargs)
        return the_result

    return inner


def third_decorator(func):
    def inner(*args, **kwargs):
        print("I'm third")
        the_result = func(*args, **kwargs)
        return the_result

    return inner


@first_decorator
@second_decorator
@third_decorator
def ex_func():
    print("Hello!")


ex_func()
