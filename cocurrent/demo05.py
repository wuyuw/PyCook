from queue import Queue
from threading import Thread, Event
import time


class ActorExit(Exception):
    pass


class Actor:

    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        self._mailbox.put(ActorExit)

    def join(self):
        self._terminated.wait()

    def start(self):
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def run(self):
        while True:
            msg = self.recv()
            print(msg)
            time.sleep(2)


if __name__ == '__main__':
    p = Actor()
    p.start()
    p.send('hello')
    p.send('world')
    p.close()
    p.join()
