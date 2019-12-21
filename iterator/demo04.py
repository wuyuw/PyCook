# -*- encoding: utf-8 -*-

import io
import sys
from functools import partial
import mmap

def test1():
    with open('../LICENSE', 'r') as f:
        for chunk in iter(lambda : f.read(10), ''):
            n = sys.stdout.write(chunk)


def test2():
    READ_SIZE = 32
    with open('../LICENSE', 'rt') as f:
        for chunk in iter(partial(f.read, READ_SIZE), ''):
            n = sys.stdout.write(chunk)


def test3():
    READ_SIZE = 32
    buf = bytearray(READ_SIZE)
    with open('../LICENSE', 'rb') as f:
        while True:
            n = f.readinto(buf)
            if n < READ_SIZE:
                break
    print(buf)
    m1 = memoryview(buf)
    print(m1)
    m2 = m1[-4:]
    print(m2)
    m2[:] = b'AAAA'
    print(buf)



if __name__ == '__main__':
    # test2()
    test3()