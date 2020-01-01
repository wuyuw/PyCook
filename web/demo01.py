from socketserver import BaseRequestHandler, TCPServer


class EchoHandler(BaseRequestHandler):

    def handle(self):
        print('got connection from ', self.client_address)
        while True:
            msg = self.request.recv(1024)
            if not msg:
                break
            self.request.send(msg)


if __name__ == '__main__':
    server = TCPServer(('localhost', 20000), EchoHandler)
    server.serve_forever()