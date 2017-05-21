# -*- coding: utf-8 -*-
from document_class import Documents

#both server and client vars and consts
options = ['import existing doc', 'disconnect', 'save doc', 'add new picture', 'add new table', 'write to table',
           'add new paragraph', 'add new heading', 'add new page break', 'email doc', 'return to last save', 'live docx']

#clients consts and vars
args_from_sql = ['first_arg', 'second_arg', 'third_arg', 'fourth_arg', 'fifth_arg', 'sixth_arg']
action = ''
first_time = True
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
9 for emailing the document
10 for going back to last save
11 for viewing the document(only text)
action number: """
MENU_VIEW_QUESTION = 'FOR VIEWING THE MENU PRESS M \ ENTER THE ACTION NUMBER: '
DOCX_SQL_FILE_NAME = 'docx_funcs.sql'


#server vars and consts
actions = {'save doc': Documents.save_doc,
    'add new picture': Documents.add_new_picture, 'add new table': Documents.add_new_table,
    'write to table': Documents.write_to_table, 'add new paragraph': Documents.add_new_paragraph,
    'add new heading': Documents.add_new_heading,
    'add new page break': Documents.add_new_page_break, 'email doc': Documents.email_doc,
    'import existing doc': Documents.import_existing_doc, 'return to last save': Documents.return_to_last_save
    , 'live docx': Documents.live_docx}

CRED = '\033[91m'
CEND = '\033[0m'

error_messages = {
    'save doc': (CRED + 'ERROR: path does not exist, action terminated' + CEND),
    'add new picture': (CRED + 'ERROR: path does not exist, action terminated' + CEND),
    'write to table': ((CRED + 'ERROR: there is no such row number, action terminated' + CEND),
                      (CRED + 'ERROR: there is no such column number, action terminated' + CEND)),
    'add new paragraph': ((CRED + 'ERROR: there is no such color, action terminated' + CEND),
                          (CRED + 'ERROR: there is not such style, action terminated' + CEND)),
    'email doc': Documents.email_doc,
    'import existing doc': (CRED + 'ERROR: path does not exist, action terminated' + CEND),
    'return to last save': (CRED + 'WARNING: your document was not previously saved, action terminated' + CEND)}

colors = {'R': (0xff, 0x0, 0x0), 'G': (0x0, 0xff, 0x0), 'b': (0x0, 0x0, 0xff), 'B': (0x0, 0x0, 0x0)} #red, green, blue, black


TABLE_STYLE = 'Table Grid'
ARGUMENT_REQUST = 'please send the argument of the action'
DISCONNECT_MESSAGE = 'you have been seccefully disconnected'