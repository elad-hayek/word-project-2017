# -*- coding: utf-8 -*-
import socket_class
import document_class
ARGUMENT_REQUST = 'please send the argument of the action'

options = []
actions = {}

class Server:

    def __init__(self, ip, port):
        self.ip__ = ip
        self.port__ = port
        self.document__ = document_class.Document()
        self.server_socket__ = socket_class.Sockets()
        self.server_socket__.open_server(ip, port)
        print 'starting server'

    def action_activation(self, action):
        #doing the actions
        pass



    def override_request(self, ip, port):
        pass


    def action_manager(self):
        client_socket, client_address = self.server_socket__.client_connection()
        action = self.server_socket__.read_from_client(client_socket)
        self.get_order_arguments(action, client_socket)

    def get_order_arguments(self, action, client_socket):
        arguments = ''
        if action in options:
            if action in options[4:]:
                self.server_socket__.write_to_client(ARGUMENT_REQUST, client_socket)
                arguments = self.server_socket__.read_from_client(client_socket)
            self.action_activation((action, arguments))



    def import_docx_file(self, path):
        self.document__ = document_class.Document(path)

