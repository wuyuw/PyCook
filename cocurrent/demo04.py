import threading


def worker(n, sema):
    sema.acquire()
    print('working', n)


sema = threading.Semaphore(3)

for n in range(10):
    t = threading.Thread(target=worker, args=(n, sema))
    t.start()

