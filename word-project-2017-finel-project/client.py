"""
Description      : The client part of the program

Author           : Elad Hayek
FileName         : client.py
Date             : 27.5.17
Version          : 1.0
"""

import socket_class
import sqlite3
from colorama import init, Fore
import re

IP_REGEX_SEARCH = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
CYAN = Fore.LIGHTCYAN_EX
ARGUMENT_SPECIFIC_REQUEST = 'ENTER %s: '
ACTION_MENU = """PRESS THE NUMBER FOR THE DESIRED ACTION AND PRESS ENTER
0 for importing and editing existing doc
1 for disconnecting
2 for saving the document
3 for adding a picture
4 for adding a table
5 for writing text into a table (only the last table could be edited)
6 for adding a paragraph
7 for adding a heading
8 for adding a new page break
9 for emailing the document (only works with gmail)
10 for going back to last save
11 for viewing the document(only text)
action number: """
MENU_VIEW_QUESTION = 'FOR VIEWING THE MENU PRESS M \ ENTER THE ' \
                     'ACTION NUMBER: '
DOCX_SQL_FILE_NAME = 'docx_funcs.sql'
INPUT_ERROR_MESSAGE = 'ERROR: enter a valid input'
IP_INPUT_ERROR_MESSAGE = 'ERROR: enter a valid ip address'
IP_INPUT_REQUEST = 'Enter the server ip address: '
NUMBER_REGEX = '^\d+$'
CELL_INDEX_REGEX = '^\d+,\d+$'
EMAIL_REGEX = '^\w+\@gmail\.com$'
IMPORT_REGEX = '^.+\.docx$'
PICTURE_SIZE_REGEX = '^\d(\.\d){0,1}$'
IMPORT_ERROR = 'ERROR : enter a valid path'
LIVE_DOCX_REQUEST = 'close the Word application to continue'
SQL_ACTION_SELECTION = "SELECT args_number FROM DOCX_METHODS " \
                       "WHERE name =  '%s'"
SQL_ARGUMENT_SELECTION = "SELECT %s FROM DOCX_METHODS WHERE name = '%s'"

options = ['import existing doc', 'disconnect', 'save doc',
           'add new picture', 'add new table', 'write to table',
           'add new paragraph', 'add new heading', 'add new page break',
           'email doc', 'return to last save', 'live docx']

args_from_sql = ['first_arg', 'second_arg', 'third_arg', 'fourth_arg',
                 'fifth_arg', 'sixth_arg']

action_numbers = map(str, range(12))

actions_input = {'add new picture': {
    'width(in inches)(note that 1 inch = 25.4mm)': PICTURE_SIZE_REGEX},
    'add new table': {'number of rows': NUMBER_REGEX,
                      'number of columns': NUMBER_REGEX},
    'write to table': {'cell index(row,column)': CELL_INDEX_REGEX},
    'add new paragraph': {'font size(from 1 to 1638)': NUMBER_REGEX},
    'email doc': {'your email': EMAIL_REGEX},
    'import existing doc': {'document path': IMPORT_REGEX}}


class Client:
    def __init__(self, ip, port):
        """
        creates a new client

        :arg ip = the server's ip
        :type = string

        :arg port = the server's port
        :type port = string
        """
        self.__client_socket = socket_class.Sockets()
        self.__client_socket.connect_to_server(ip, port)
        self.__first_time = True

    def menu_options(self):
        """
        presents the client with the options and chooses what to do
         accordingly
        it also presents the client with the option arguments and sends them
        to the server
        """
        while True:
            print '\n'
            response, action = self.action_choose()
            if response:
                self.__client_socket.write_to_server(options[int(action)])
                if int(action) == 8 or int(action) == 10 or int(action) == 11:
                    if int(action) == 11:
                        print CYAN + LIVE_DOCX_REQUEST
                    color, response_from_server =\
                        self.__client_socket.read_from_server()
                    print color + response_from_server
                    continue

                if int(action) == 1:
                    color, response_from_server =\
                        self.__client_socket.read_from_server()
                    print color + response_from_server
                    self.__client_socket.close()
                    break

                conn = sqlite3.connect(DOCX_SQL_FILE_NAME)
                arg_len_cursor =\
                    conn.execute(SQL_ACTION_SELECTION % options[int(action)])

                args_for_client = ''
                for raw in arg_len_cursor:
                    for i in range(raw[0]):
                        arg_name_cursor = \
                            conn.execute(
                                SQL_ARGUMENT_SELECTION % (
                                    args_from_sql[i], options[int(action)]))
                        for inside_raw in arg_name_cursor:
                            arg = raw_input(
                                ARGUMENT_SPECIFIC_REQUEST % inside_raw[0])
                            if options[int(action)] in\
                                    actions_input and inside_raw[0] in\
                                    actions_input[options[int(action)]]:
                                arg = self.check_argument_input(
                                    arg, options[int(action)], inside_raw[0])
                            args_for_client += arg+','
                self.__client_socket.write_to_server(args_for_client)
                color, response_from_server =\
                    self.__client_socket.read_from_server()
                print color + response_from_server
            else:
                continue

    def check_argument_input(self, arg, func_name, arg_name):
        """
        checks if the client's input was according to a specific argument in
         an action

         :arg arg = the client's input
         :type arg = string

         :arg func_name = the action the client chose
         :type func_name = string

         :arg arg_name = the specific argument in the action the client chose
         :type arg_name = string
        """
        match = re.match(actions_input[func_name][arg_name], arg)
        while not match:
            if func_name == options[0]:
                print RED + IMPORT_ERROR
            else:
                print RED + INPUT_ERROR_MESSAGE
            arg = raw_input(ARGUMENT_SPECIFIC_REQUEST % arg_name)
            match = re.match(actions_input[func_name][arg_name], arg)
        return arg

    def action_choose(self):
        """
        checks if the input of the client to choose the action is a number
        between 0-11 or M
        """
        if self.__first_time:
            action = raw_input(ACTION_MENU)
            self.__first_time = False
        else:
            action = raw_input(MENU_VIEW_QUESTION)
            if action == 'M':
                action = raw_input(ACTION_MENU)
                if self.input_check(action):
                    return True, action
                else:
                    print INPUT_ERROR_MESSAGE
                    return False, None
            elif self.input_check(action):
                return True, action
            else:
                print RED + INPUT_ERROR_MESSAGE
                return False, None
        if self.input_check(action):
            return True, action
        else:
            print RED + INPUT_ERROR_MESSAGE
            return False, None

    def input_check(self, action):
        """
        checks if the number that the client chose is between 0-11

        :arg action = the number of action the client chose
        :type action = string
        """
        if action in action_numbers:
            return True
        else:
            return False


def connect_to_server():
    """
    asks the client to enter the ip address of the server and checks if valid
    """
    ip = raw_input(IP_INPUT_REQUEST)
    match = re.match(IP_REGEX_SEARCH, ip)
    while not match:
        print RED + IP_INPUT_ERROR_MESSAGE
        ip = raw_input(IP_INPUT_REQUEST)
        match = re.match(IP_REGEX_SEARCH, ip)
    return ip


def run_client():
    """
    connects to the server and runs the client
    """
    my_client = Client(connect_to_server(), 8820)
    my_client.menu_options()


def main():
    try:
        run_client()
    except Exception, ex:
        print 'EXCEPTION: %s' % (ex, )

if __name__ == '__main__':
    init(autoreset=True)
    main()
