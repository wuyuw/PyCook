"""
题目：给定一个csv格式文件，给出坐标（a, b）,返回第a列第b行的数据
"""


def get_value(a, b):
    """
    :param a: 第 a 列
    :param b: 第 b 行
    :return:
    """
    path = 'test.csv'
    l = []
    with open(path, 'r') as f:
        for i in f:
            l.append(i.strip().split(','))
    res = ''
    for j in l[:b]:
        if j[a-1] != '':
            res = j[a-1]
    return res


if __name__ == '__main__':
    print(get_value(2, 1))
