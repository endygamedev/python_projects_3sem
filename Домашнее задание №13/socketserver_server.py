"""
    Модифицировать приведенный выше код socketserver так, чтобы сервер возвращал отправленные сообщения длиной менее 10 символов в исходном виде,
    в ином случае от сообщения должны браться первые 10 символов сообщения, а после них ставиться многоточие.
"""


import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        data = self.data.decode()
        if len(data) >= 10:
            data = f'{data[:10]}...'
        self.data = str.encode(data)
        self.request.sendall(self.data)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
