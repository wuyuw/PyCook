# -*- encoding:utf-8 -*-


def foo(a, *, b):
    return a, b


if __name__ == '__main__':
    foo(1, b=2)