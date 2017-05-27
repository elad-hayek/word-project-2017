# -*- coding: utf-8 -*-
"""
Description      : The server part of the program

Author           : Elad Hayek
FileName         : client.py
Date             : 27.5.17
Version          : 1.0
"""

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
        """
        creates a new server

        :arg ip = the server's ip
        :type = string

        :arg port = the server's port
        :type port = string
        """
        self.__ip = ip
        self.__port = port
        self.__document = Documents()
        self.__client_socket = socket_class.Sockets()
        self.__server_socket = socket_class.Sockets()
        self.__server_socket.open_server(ip, port)
        print 'starting server'

    def action_activation(self, action, arguments):
        """
        activates the actions with the arguments from the document_class
        and returns the response of the action(if it succeeded or terminated)

        :arg action = the client's action request
        :type action = string

        :arg arguments = the arguments the client sent
        :type arguments = string
        """
        arguments = arguments.split(',')
        print arguments
        response = actions[action](self.__document, arguments)
        response = pickle.dumps(response)
        self.__server_socket.write_to_client(response, self.__client_socket)

    def get_arguments(self):
        """
        gets the client's arguments to the specific actions he chose
        """
        arguments = self.__server_socket.read_from_client(self.__client_socket)
        return arguments

    def connect_to_client(self):
        """
        connects to the client
        """
        client_socket, client_address = self.__server_socket.client_connection()
        self.__client_socket = client_socket
        self.__document = Documents()

    def disconnect_client(self):
        """
        disconnects the client from the server
        """
        print 'disconnecting client'
        response = pickle.dumps(DISCONNECT_MESSAGE)
        self.__server_socket.write_to_client(response, self.__client_socket)
        self.__client_socket.close()
        if os.path.exists('beta.docx'):
            os.remove('beta.docx')
        self.connect_to_client()
        self.action_menager()

    def action_menager(self):
        """
        receives the client's request and sends it to the check_action method
        """
        action = self.__server_socket.read_from_client(self.__client_socket)
        print action
        self.check_action(action)

    def check_action(self, action):
        """
        checks if the action is 8,10,11,1 because they need to be sent to
        other methods and if not it sends it to the action_activation method
        with the client arguments

        :arg action = the client's action request
        :arg action = string
        """
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