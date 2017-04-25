# -*- coding: utf-8 -*-
import socket_class
from document_class import Documents

ARGUMENT_REQUST = 'please send the argument of the action'

options = ['import_existing_doc', 'save_doc', 'add_new_picture', 'add_new_table', 'write_to_table',
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
        self.server_socket__ = socket_class.Sockets()
        self.server_socket__.open_server(ip, port)
        print 'starting server'

    def action_activation(self, action, arguments):
        #doing the actions
        actions[action](self.document__, text, style, color)
        pass


    def get_arguments(self, client_socket):
        self.server_socket__.write_to_client(ARGUMENT_REQUST, client_socket)
        arguments = self.server_socket__.read_from_client(client_socket)
        return arguments

    def action_manager(self):
        client_socket, client_address = self.server_socket__.client_connection()
        action = self.server_socket__.read_from_client(client_socket)
        self.check_action(action, client_socket)

    def check_action(self, action, client_socket):
        arguments = ''
        if action in options:
            if action == options[0]:
                arguments = self.get_arguments(client_socket)
                self.import_docx_file(arguments)
            if action in options[4:]:
                arguments = self.get_arguments(client_socket)
            self.action_activation(action, arguments)



    def import_docx_file(self, path):
        self.document__ = Documents(path)

