"""
题目1：给定一个整数，返回该整数表示的excel的列名
"""


def get_column_by_num(num, col=''):
    if num > 26:
        mod = num % 26
        rel = num // 26
        if mod == 0:
            mod = 26
            rel -= 1
        return get_column_by_num(rel, chr(mod+64) + col)
    else:
        return chr(num + 64) + col


def get_column_by_num_v2(num):
    col = ''
    while num > 26:
        mod = num % 26
        num = num // 26
        if mod == 0:
            mod = 26
            num -= 1
        col = chr(mod + ord('A') - 1) + col
    col = chr(num + ord('A') - 1) + col
    return col


if __name__ == '__main__':
    print(get_column_by_num(1657))
    print(get_column_by_num_v2(1657))
