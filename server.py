# -*- coding: utf-8 -*-
import socket_class
from document_class import Documents

ARGUMENT_REQUST = 'please send the argument of the action'
DISCONNECT_MESSAGE = 'you have been seccefully disconnected'

options = ['import_existing_doc', 'disconnect', 'save_doc', 'add_new_picture', 'add_new_table', 'write_to_table',
           'add_new_paragraph', 'add_new_word', 'add_new_heading', 'add_new_page_break', 'email_doc']
actions = {
    'AddNewWord': Documents.add_new_word, 'save_doc': Documents.save_doc,
    'add_new_picture': Documents.add_new_picture, 'add_new_table': Documents.add_new_table,
    'write_to_table': Documents.write_to_table, 'add_new_paragraph': Documents.add_new_paragraph,
    'add_new_word': Documents.add_new_word, 'add_new_heading': Documents.add_new_heading,
    'add_new_page_break': Documents.add_new_page_break, 'email_doc': Documents.email_doc
}

class Server:

    def __init__(self, ip, port):
        self.ip__ = ip
        self.port__ = port
        self.document__ = Documents()
        self.__client_socket = socket_class.Sockets()
        self.server_socket__ = socket_class.Sockets()
        self.server_socket__.open_server(ip, port)
        print 'starting server'

    def action_activation(self, action, arguments):
        arguments = arguments[1:].split(',')
        print actions[action](self.document__, arguments)



    def get_arguments(self):
        self.server_socket__.write_to_client(ARGUMENT_REQUST, self.__client_socket)
        arguments = self.server_socket__.read_from_client(self.__client_socket)
        return arguments

    def connect_to_client(self):
        client_socket, client_address = self.server_socket__.client_connection()
        self.__client_socket = client_socket
        self.document__ = Documents()

    def disconnect_client(self):
        print 'disconnecting client'
        self.server_socket__.write_to_client(DISCONNECT_MESSAGE, self.__client_socket)
        self.__client_socket.close()
        self.connect_to_client()
        self.action_menager()

    def action_menager(self):
        action = self.server_socket__.read_from_client(self.__client_socket)
        self.check_action(action)

    def check_action(self, action):
        print action
        print options[1]
        if action == options[0]:
            arguments = self.get_arguments()
            self.import_docx_file(arguments)
        if action == options[1]:
            self.disconnect_client()
        else:
            arguments = self.get_arguments()
            self.action_activation(action, arguments)



    def import_docx_file(self, path):
        self.document__ = Documents(path)


def main():
    my_server = Server('0.0.0.0', 8820)
    my_server.connect_to_client()
    while True:
        my_server.action_menager()

if __name__ == main():
    main()