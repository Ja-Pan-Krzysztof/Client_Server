from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] [%(name)s] - %(message)s')


class Server:
    HOST = '192.168.0.101'
    PORT = 9999
    FORMAT = 'utf8'
    HEADER = 8

    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((self.HOST, self.PORT))

        self.sock.listen()

        print('Server is running...')

    def handle_client_connection(self, client):
        while True:
            try:
                head_message = client.recv(self.HEADER).decode(self.FORMAT)
                message = client.recv(int(head_message)).decode(self.FORMAT)

                if message == '!stop':
                    logging.info('User was disconected')
                    break

                else:
                    print(message)

            except ValueError:
                break

    def receive(self):
        while True:
            client, address = self.sock.accept()

            logging.info(f'Connected with {address[0]}:{[address[1]]}')

            client.send('26'.encode(self.FORMAT))
            client.send('Welcome to the my server !'.encode(self.FORMAT))

            tasks = Thread(target=self.handle_client_connection, args=(client, ))
            tasks.start()

    def __del__(self):
        self.sock.close()


server = Server()
server.receive()
