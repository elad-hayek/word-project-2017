import socket_class
import sqlite3
import var_and_const
from colorama import init

class Client:
    def __init__(self, ip, port):
        self.client_socket__ = socket_class.Sockets()
        self.client_socket__.connect_to_server(ip, port)


    def menu_options(self):
        while True:
            print '\n'
            response, action = self.action_choose()
            if response:
                self.client_socket__.write_to_server(var_and_const.options[int(action)])
                if int(action) == 8 or int(action) == 10 or int(action) == 11:
                    response_from_server = self.client_socket__.read_from_server()
                    print response_from_server
                    continue

                if int(action) == 1:
                    print self.client_socket__.read_from_server()
                    self.client_socket__.close()
                    break

                conn = sqlite3.connect(var_and_const.DOCX_SQL_FILE_NAME)
                arg_len_cursor = conn.execute("SELECT args_number FROM DOCX_METHODS WHERE name =  '%s'" % var_and_const.options[int(action)])

                args_for_client = ''
                for raw in arg_len_cursor:
                    for i in range(raw[0]):
                        arg_name_cursor = conn.execute("SELECT %s FROM DOCX_METHODS WHERE name = '%s'" % (var_and_const.args_from_sql[i], var_and_const.options[int(action)]))
                        for inside_raw in arg_name_cursor:
                            arg = raw_input(var_and_const.ARGUMENT_SPECIFIC_REQUEST %inside_raw[0])
                            args_for_client += arg+','
                self.client_socket__.write_to_server(args_for_client)
                color, response_from_server = self.client_socket__.read_from_server()
                print color + response_from_server
            else:
                continue

    def action_choose(self):
        if var_and_const.first_time:
            action = raw_input(var_and_const.ACTION_MENU)
            var_and_const.first_time = False
        else:
            action = raw_input(var_and_const.MENU_VIEW_QUESTION)
            if action == 'M':
                action = raw_input(var_and_const.ACTION_MENU)
                if self.input_check(action):
                    return True, action
                else:
                    print var_and_const.INPUT_ERROR_MESSAGE
                    return False, None
            elif self.input_check(action):
                return True, action
            else:
                print var_and_const.INPUT_ERROR_MESSAGE
                return False, None
        if self.input_check(action):
            return True, action
        else:
            print var_and_const.INPUT_ERROR_MESSAGE
            return False, None


    def input_check(self, action):
        if action in var_and_const.action_numbers:
            return True
        else:
            return False




def run_client():
    my_client = Client('127.0.0.1', 8820)
    my_client.menu_options()

def main():
    try:
        run_client()
    except Exception, ex:
        print 'EXCEPTION: %s' % (ex, )

if __name__ == '__main__':
    init(autoreset=True)
    main()

