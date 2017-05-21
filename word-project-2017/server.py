# -*- coding: utf-8 -*-
import socket_class
from document_class import Documents
import var_and_const
import os



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
        response = var_and_const.actions[action](self.document__, arguments)
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
        self.server_socket__.write_to_client(var_and_const.DISCONNECT_MESSAGE, self.__client_socket)
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
        if action == var_and_const.options[8]:
            self.action_activation(action, '')
        elif action == var_and_const.options[9]:
            self.action_activation(action, '')
        elif action == var_and_const.options[10]:
            self.action_activation(action, '')
        elif action == var_and_const.options[11]:
            self.action_activation(action, '')
        elif action == var_and_const.options[1]:
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
    main()