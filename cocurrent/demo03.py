from threading import Condition, Thread
import time


class PeriodicTimer:

    def __init__(self, interval):
        self.interval = interval
        self._cv = Condition()
        self._flag = 0

    def run(self):
        while True:
            time.sleep(self.interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        t.start()

    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()


def countdown(nticks, ptimer):
    while nticks > 0:
        ptimer. wait_for_tick()
        print('T-minus', nticks)
        nticks -= 1


def countup(nticks, ptimer):
    n = 0
    while n < nticks:
        ptimer.wait_for_tick()
        print('counting', n)
        n += 1


if __name__ == '__main__':
    ptimer = PeriodicTimer(3)
    Thread(target=countdown, args=(10, ptimer)).start()
    Thread(target=countup, args=(5, ptimer)).start()
    ptimer.start()
