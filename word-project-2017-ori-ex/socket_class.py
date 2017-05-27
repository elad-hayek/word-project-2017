# -*- coding: utf-8 -*-
from socket import socket
import pickle

class Sockets(socket):
    def __init__(self):
        super(Sockets, self).__init__()

    def connect_to_server(self, ip, port):
        self.connect((ip, port))

    def write_to_server(self, data):
        self.send(data)

    def write_to_client(self, data,  client_socket):
        client_socket.send(data)

    def read_from_server(self):
        data = self.recv(1024)
        data = pickle.loads(data)
        return data

    def read_from_client(self, client_socket):
        data = client_socket.recv(1024)
        return data

    def open_server(self, ip, port):
        self.bind((ip, port))

    def client_connection(self):
        self.listen(1)
        (client_socket, client_address) = self.accept()
        return client_socket, client_address

    def close_socket(self):
        self.close()
