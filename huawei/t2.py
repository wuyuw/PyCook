import sys


def min_step(l):
    if l[0] >= len(l) - 1:
        return 1
    choices = []
    for i in range(1, l[0]+1):
        choices.append(min_step(l[i:]))
    return 1 + min(choices)


if __name__ == '__main__':
    # n = int(sys.stdin.readline().strip())
    # lst = []
    # for i in range(n):
    #     lst.append(int(sys.stdin.readline().strip()))
    lst = [2, 3, 2, 1, 2, 1, 5, 3]
    print(min_step(lst))
