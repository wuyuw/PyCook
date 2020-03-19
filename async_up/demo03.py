


def foo():
    while True:
        num = int(input())
        s = ''
        while num > 0:
            c = num % 27
            if c == 0:
                char = 'A'
            else:
                char = chr(ord('A') + c - 1)
            s = s + char
            num = num // 27
        print(s)


if __name__ == '__main__':
    foo()