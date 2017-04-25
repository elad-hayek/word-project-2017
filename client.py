import socket_class

ACTION_MENU = ''
options = ['save_doc', 'add_new_picture', 'add_new_table', 'write_to_table',
           'add_new_paragraph', 'add_new_word', 'add_new_heading', 'add_new_page_break', 'email_doc']


class Client:
    def __init__(self, ip, port):
        self.client_socket__ = socket_class.Sockets()
        self.client_socket__.connect_to_server(ip, port)


    def menu_options(self):
            action = raw_input()
            if action in options:
                for option in options:
                    if action == option:
                        self.client_socket__.write_to_socket(action)
            else:
                print 'write a real action'



