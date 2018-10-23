# Задание №4 (посложное)
# Написать декоратор, который “пропускает” из функциии только один типа исключения (RightError),
# все остальные превращая в исключения другого типа(WrongError)


def process_error_parametric_decorator(right_error, wrong_error):
    def process_error_decorator(func):
        def inner(*args, **kwargs):
            raise_error = None

            try:
                func(*args, **kwargs)
            except right_error as e:
                print("right error passthrough")
                raise e
            except Exception as e:
                raise_error = e

            if raise_error:
                print("wrong error throw")
                raise wrong_error()

        return inner

    return process_error_decorator


@process_error_parametric_decorator(TypeError, ValueError)
def div(x, y):
    return x / y


try:
    div(1, "abc")
except Exception as err:
    print("caught {}".format(type(err)))

try:
    div(1, 0)
except Exception as err:
    print("caught {}".format(type(err)))
