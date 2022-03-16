import socket


class Client:
    HOST = '192.168.0.101'
    PORT = 9999
    FORMAT = 'utf8'
    HEADER = 64
    DISCONNECTED = False

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = self.sock.connect((self.HOST, self.PORT))

    def write(self):
        message = str(input('>>> ')).encode(self.FORMAT)
        head_message = str(len(message)).encode(self.FORMAT)

        if message == '!stop'.encode(self.FORMAT):
            self.DISCONNECTED = True

            head_message = str(20).encode(self.FORMAT)
            message = 'User was disconected'.encode(self.FORMAT)

            self.sock.send(head_message)
            self.sock.send(message)

        else:
            self.sock.send(head_message)
            self.sock.send(message)

    def stop(self):
        self.sock.close()

    def receive(self):
        while not self.DISCONNECTED:
            try:
                message = self.sock.recv(self.HEADER).decode(self.FORMAT)
                print(message)
                self.write()

            except ConnectionAbortedError:
                break

            except ValueError:
                print('Error...')
                self.sock.close()


client = Client()
client.receive()