import socket_class
import sqlite3

ACTION_MENU = ''
DOCX_SQL_FILE_NAME = 'docx_funcs.sql'

options = ['import_existing_doc', 'disconnect', 'save_doc', 'add_new_picture', 'add_new_table', 'write_to_table',
           'add_new_paragraph', 'add_new_word', 'add_new_heading', 'add_new_page_break', 'email_doc']
args_from_sql = ['first_arg', 'second_arg', 'third_arg', 'fourth_arg', 'fifth_arg', 'sixth_arg']
# args_for_client = ''
ARGUMENT_SPECIFIC_REQUEST = 'ENTER %s: '


class Client:
    def __init__(self, ip, port):
        self.client_socket__ = socket_class.Sockets()
        self.client_socket__.connect_to_server(ip, port)


    def menu_options(self):
        while True:
            action = raw_input('enter action: ')
            if action in options:
                self.client_socket__.write_to_server(action)
                if action == options[9]:
                    continue
                print self.client_socket__.read_from_server()   #argument requst
                if action == options[1]:
                    self.client_socket__.close()
                    break

                conn = sqlite3.connect(DOCX_SQL_FILE_NAME)
                arg_len_cursor = conn.execute("SELECT args_number FROM DOCX_METHODS WHERE name =  '%s'" % action)

                args_for_client = ''
                for raw in arg_len_cursor:
                    for i in range(raw[0]):
                        arg_name_cursor = conn.execute("SELECT %s FROM DOCX_METHODS WHERE name = '%s'" % (args_from_sql[i], action))
                        for inside_raw in arg_name_cursor:
                            arg = raw_input(ARGUMENT_SPECIFIC_REQUEST %inside_raw[0])
                            args_for_client += arg+','
                print args_for_client
                self.client_socket__.write_to_server(args_for_client)

            else:
                print 'write a real action'

def main():
    my_client = Client('127.0.0.1', 8820)
    my_client.menu_options()

if __name__== main():
    main()

