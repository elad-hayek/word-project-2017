import socket_class

ACTION_MENU = ''
options = []


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



