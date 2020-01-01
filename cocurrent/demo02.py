from threading import Thread, Event
import time


def countdown(n, started_event):
    time.sleep(0.1)
    print('coundown starting')
    started_event.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)


if __name__ == '__main__':
    started_event = Event()
    print('launching countdown')
    t = Thread(target=countdown, args=(10, started_event))
    t.start()

    started_event.wait()
    print('countdown is running')

