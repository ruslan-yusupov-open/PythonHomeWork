# Задание №3 (посложное)
# Написать декоратор check, который проверяет типы входных аргументов декорируемой функции и тип результата


def parametric_type_checking_decorator(check_args=None, check_kwargs=None, check_result=None):
    def type_checking_decorator(func):
        def inner(*args, **kwargs):
            if check_args:
                for check_tuple in enumerate(zip(check_args, args)):
                    if not isinstance(check_tuple[1][1], check_tuple[1][0]):
                        raise TypeError("wrong type of param number {}".format(check_tuple[0] + 1))

            if check_kwargs:
                for check_key in kwargs.keys():
                    if check_key in check_kwargs:
                        if not isinstance(kwargs[check_key], check_kwargs[check_key]):
                            raise TypeError("wrong type of param \"{}\"".format(check_key))

            result = func(*args, **kwargs)

            if check_result:
                if not isinstance(result, check_result):
                    raise TypeError("wrong type of result")

            return result

        return inner

    return type_checking_decorator


@parametric_type_checking_decorator(check_args=[int, int], check_kwargs={"param": int}, check_result=int)
def summ_and_mult(x, y, param):
    if param < 0:
        return "below zero"
    return (x + y) * param


print(summ_and_mult(2, 2, param=3))

try:
    print(summ_and_mult(2, "2", param=3))
except Exception as err:
    print("sum caught {} {}".format(type(err), err))

try:
    print(summ_and_mult(2, 2, param="3"))
except Exception as err:
    print("sum caught {} {}".format(type(err), err))

try:
    print(summ_and_mult(2, 2, param=-5))
except Exception as err:
    print("sum caught {} {}".format(type(err), err))


@parametric_type_checking_decorator(check_result=type(None))
def foo1():
    return 1


@parametric_type_checking_decorator(check_result=type(None))
def foo2():
    print("hi")


@parametric_type_checking_decorator()
def bar(x, y):
    return x + y + 123


try:
    foo1()
except Exception as err:
    print("foo1 caught {} {}".format(type(err), err))

foo2()
print(bar(1, 2))


# интересно что нельзя использовать @parametric_type_checking_decorator(check_args=[function)])
@parametric_type_checking_decorator(check_args=[type(foo1)])
def ex(func):
    func()


ex(foo2)

try:
    ex(1)
except Exception as err:
    print("ex caught {} {}".format(type(err), err))
