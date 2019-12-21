# -*- encoding: utf-8 -*-

"""
去重且保留顺序
"""


def dedupe(items):
    pool = set()
    for item in items:
        if item not in pool:
            yield item
            pool.add(item)


# 读文件去除重复行

with open('file', 'r') as f:
    for line in dedupe(f):
        pass

