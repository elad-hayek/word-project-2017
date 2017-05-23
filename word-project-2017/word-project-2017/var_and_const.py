# -*- coding: utf-8 -*-
from document_class import Documents
from colorama import Fore

#both server and client vars and consts
options = ['import existing doc', 'disconnect', 'save doc', 'add new picture', 'add new table', 'write to table',
           'add new paragraph', 'add new heading', 'add new page break', 'email doc', 'return to last save', 'live docx']

RED = Fore.LIGHTRED_EX

#clients consts and vars
args_from_sql = ['first_arg', 'second_arg', 'third_arg', 'fourth_arg', 'fifth_arg', 'sixth_arg']
action = ''
first_time = True
action_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
# action_numbers = map(str, range(12))

ARGUMENT_SPECIFIC_REQUEST = 'ENTER %s: '
ACTION_MENU = """PRESS THE NUMBER FOR THE DESIRED ACTION AND PRESS ENTER
0 for importing and editing existing doc
1 for disconnecting
2 for saving the document
3 for adding a picture
4 for adding a table
5 for writing text into a table *only the last table could be edited
6 for adding a paragraph
7 for adding a heading
8 for adding a new page break
9 for emailing the document *only with gmail
10 for going back to last save
11 for viewing the document(only text)
action number: """
MENU_VIEW_QUESTION = 'FOR VIEWING THE MENU PRESS M \ ENTER THE ACTION NUMBER: '
DOCX_SQL_FILE_NAME = 'docx_funcs.sql'
INPUT_ERROR_MESSAGE = RED + 'ERROR: enter a valid input'


#server vars and consts
actions = {'save doc': Documents.save_doc,
    'add new picture': Documents.add_new_picture, 'add new table': Documents.add_new_table,
    'write to table': Documents.write_to_table, 'add new paragraph': Documents.add_new_paragraph,
    'add new heading': Documents.add_new_heading,
    'add new page break': Documents.add_new_page_break, 'email doc': Documents.email_doc,
    'import existing doc': Documents.import_existing_doc, 'return to last save': Documents.return_to_last_save
    , 'live docx': Documents.live_docx}

GREEN = '\033[92m'

DISCONNECT_MESSAGE = GREEN + 'you have been seccefully disconnected' + END