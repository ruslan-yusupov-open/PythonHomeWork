# Задание №2
# 1. Написать менеджер контекста, который замеряет время исполнения кода
# 2. Написать менеджер контекста, который “съедает” все исключения в коде
import time
from contextlib import contextmanager


@contextmanager
def error_handler():
    # noinspection PyBroadException
    try:
        yield
    except Exception:
        pass


with error_handler():
    print(2 / 0)

print("Hi!")


class MeasureTime(object):
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, *args):
        print("execution took {}".format(time.time() - self.start_time))


with MeasureTime():
    print('Some work here!')
    time.sleep(1)
