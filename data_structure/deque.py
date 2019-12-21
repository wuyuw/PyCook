# -*- encoding: utf-8 -*-

"""
collections.deque
使用deque保留最后N个元素

"""
import os
from collections import deque


def search(f, pattern, history=5):
    previous_line = deque(maxlen=history)
    for line in f:
        if pattern in line:
            yield line, previous_line
            previous_line.append(line)


def test_tail(file):
    with open(file, 'r') as f:
        for line, prelines in search(f, '='):
            for pline in prelines:
                print(pline, end='')


if __name__ == '__main__':
    test_tail('../Pipfile')
