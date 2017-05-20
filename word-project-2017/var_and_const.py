# -*- coding: utf-8 -*-
from document_class import Documents

#both server and client vars and consts
options = ['import existing doc', 'disconnect', 'save doc', 'add new picture', 'add new table', 'write to table',
           'add new paragraph', 'add new heading', 'add new page break', 'email doc', 'return to last save', 'live docx']

#clients consts and vars
args_from_sql = ['first_arg', 'second_arg', 'third_arg', 'fourth_arg', 'fifth_arg', 'sixth_arg']
ARGUMENT_SPECIFIC_REQUEST = 'ENTER %s: '
ACTION_MENU = """PRESS THE NUMBER FOR THE DESIRED ACTION
0 for importing existing doc
1 for disconnecting
2 for saveing the document
3 for adding a picture
4 for adding a table
5 for writing to the table
6 for adding a paragraph
7 for adding a heading
8 for adding a new page break
9 for emailing the document
10 for returning to the last save
11 for seeing the document(only text)
action number: """
DOCX_SQL_FILE_NAME = 'docx_funcs.sql'


#server vars and consts
actions = {'save doc': Documents.save_doc,
    'add new picture': Documents.add_new_picture, 'add new table': Documents.add_new_table,
    'write to table': Documents.write_to_table, 'add new paragraph': Documents.add_new_paragraph,
    'add new heading': Documents.add_new_heading,
    'add new page break': Documents.add_new_page_break, 'email doc': Documents.email_doc,
    'import existing doc': Documents.import_existing_doc, 'return to last save': Documents.return_to_last_save
    , 'live docx': Documents.live_docx}

ARGUMENT_REQUST = 'please send the argument of the action'
DISCONNECT_MESSAGE = 'you have been seccefully disconnected'