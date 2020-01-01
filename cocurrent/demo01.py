import time

d = {'A': 1}
def countdown(n, c):
    while n > 0:
        print('t-minus', n)
        n -= 1
        time.sleep(5)


if __name__ == '__main__':
    from threading import Thread

    t = Thread(target=countdown, args=(10, d), daemon=True)
    t.daemon = True
    t.start()


