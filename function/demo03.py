# -*- encoding:utf-8 -*-

from queue import Queue
from functools import wraps

def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper


def add(x, y):
    return x + y

# @inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')


def func():
    x = 1
    while True:
        y = (yield x)
        x += y


if __name__ == '__main__':
    geniter = func()
    print(geniter.send(None))  # 1
    print(geniter.send(3)) # 4
    print(geniter.send(10))# 14
