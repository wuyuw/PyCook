
# callback


from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
import socket
import time

selector = DefaultSelector()
n_tasks = 0


def get(path):
    global n_tasks
    n_tasks += 1

    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect(('www.baidu.com', 80))
    except BlockingIOError:
        pass

    request = 'GET %s HTTP/1.1\r\n\r\n' % path

    selector.register(s.fileno(), EVENT_WRITE, data=lambda: connected(s, request))


def connected(s, request):
    selector.unregister(s.fileno())
    # s is writable
    s.send(request.encode())

    chunks = []
    selector.register(s.fileno(), EVENT_READ, data=lambda: readable(s, chunks))


def readable(s, chunks):
    global n_tasks

    # s is readable

    selector.unregister(s.fileno())

    chunk = s.recv(1000)
    if chunk:
        chunks.append(chunk)
        selector.register(s.fileno(), EVENT_READ, data=lambda: readable(s, chunks))
    else:
        body = (b''.join(chunks)).decode()
        print(body.split('\n')[0])
        n_tasks -= 1


if __name__ == '__main__':
    start = time.time()
    get('/s?wd=python')
    get('/s?wd=python')

    while n_tasks:
        events = selector.select()
        for event, mask in events:
            cb = event.data
            cb()

    print('took %.1f sec' % (time.time() - start))



