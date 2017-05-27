# -*- coding: utf-8 -*-
import socket_class
from document_class import Documents
import os
from colorama import init, Fore
import pickle


GREEN = Fore.LIGHTGREEN_EX
DISCONNECT_MESSAGE = GREEN, 'you have been seccefully disconnected'

options = ['import existing doc', 'disconnect', 'save doc', 'add new picture', 'add new table', 'write to table',
           'add new paragraph', 'add new heading', 'add new page break', 'email doc', 'return to last save', 'live docx']
actions = {'save doc': Documents.save_doc,
    'add new picture': Documents.add_new_picture, 'add new table': Documents.add_new_table,
    'write to table': Documents.write_to_table, 'add new paragraph': Documents.add_new_paragraph,
    'add new heading': Documents.add_new_heading,
    'add new page break': Documents.add_new_page_break, 'email doc': Documents.email_doc,
    'import existing doc': Documents.import_existing_doc, 'return to last save': Documents.return_to_last_save
    , 'live docx': Documents.live_docx}


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
        arguments = arguments.split(',')
        print arguments
        response = actions[action](self.document__, arguments)
        response = pickle.dumps(response)
        self.server_socket__.write_to_client(response, self.__client_socket)

    def get_arguments(self):
        #print 'getting arguments'
        arguments = self.server_socket__.read_from_client(self.__client_socket)
        return arguments

    def connect_to_client(self):
        client_socket, client_address = self.server_socket__.client_connection()
        self.__client_socket = client_socket
        self.document__ = Documents()

    def disconnect_client(self):
        print 'disconnecting client'
        response = pickle.dumps(DISCONNECT_MESSAGE)
        self.server_socket__.write_to_client(response, self.__client_socket)
        self.__client_socket.close()
        if os.path.exists('beta.docx'):
            os.remove('beta.docx')
        self.connect_to_client()
        self.action_menager()

    def action_menager(self):
        action = self.server_socket__.read_from_client(self.__client_socket)
        print action
        self.check_action(action)

    def check_action(self, action):
        if action == options[8]:
            self.action_activation(action, '')
        elif action == options[10]:
            self.action_activation(action, '')
        elif action == options[11]:
            self.action_activation(action, '')
        elif action == options[1]:
            self.disconnect_client()
        else:
            arguments = self.get_arguments()
            self.action_activation(action, arguments)


def main():
    try:
        my_server = Server('0.0.0.0', 8820)
        my_server.connect_to_client()
        while True:
            my_server.action_menager()
    except Exception, ex:
        print 'EXCEPTION: %s' % (ex, )

if __name__ == main():
    init(autoreset=True)
    main()