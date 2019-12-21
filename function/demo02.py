

def make_handler():
    sequence = 0
    while True:
        result = yield 
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


if __name__ == '__main__':
    handler = make_handler()
    print(handler)
    print(next(handler))
    print(next(handler))
    print(next(handler))
    print(next(handler))
    