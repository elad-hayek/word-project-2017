# -*- coding: utf-8 -*-
"""
Description      : Creates the sql table for the actions

Author           : Elad Hayek
FileName         : client.py
Date             : 27.5.17
Version          : 1.0
"""

import sqlite3

DOCX_SQL_FILE_NAME = 'docx_funcs.sql'
CREATE_TABLE = '''CREATE TABLE DOCX_METHODS
(NAME TEXT PRIMARY KEY    NOT NULL,
ARGS_NUMBER INT     NOT NULL,
FIRST_ARG TEXT, SECOND_ARG TEXT, THIRD_ARG TEXT, FOURTH_ARG TEXT,
 FIFTH_ARG TEXT, SIXTH_ARG TEXT)'''

docx_methods_sql_values = [
    "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,"
    "THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('write to table', 2,'cell index(row,column)',"
    "'cell text', null, null, null, null )",
    "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,"
    "THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('save doc', 2, 'saving path', 'document name', null,"
    " null, null, null )",
    "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,"
    "THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('add new picture',2,'the path of the picture', 'width"
    "(in inches)(note that 1 inch = 25.4mm)',null, null, null, null )",
    "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,"
    "THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('add new table' ,2,'number of rows', 'number of columns',"
    " null, null, null, null )",
    "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,"
    "THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('add new paragraph', 5, 'paragraph text', "
    "'font style(N=none, B=bold, I=italic)', "
    "'font color(B=black, b=blue, G=green, R=red)', "
    "'font size(from 1 to 72)', 'Word font name \ "
    "your own font name', null )",
    "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,"
    "THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('add new heading' ,1 , 'heading text', null, null,"
    " null, null, null )",
    "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,"
    "THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('add new page break', 0, null, null, null, null, null, null )",
    "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,"
    "THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('email doc', 1, 'your email', null, null, null, null, null )",
    "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,"
    "THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('import existing doc', 1, 'document path', null, null,"
    " null, null, null )",
    "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,"
    "THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('return to last save', 0, null, null, null, null, null, null )",
    "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,"
    "THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('live docx', 0, null, null, null, null, null, null )"]


def main():
    """
    creates a new sql table for the actions of the document_class
    and prints it
    """
    conn = sqlite3.connect(DOCX_SQL_FILE_NAME)
    conn.execute(CREATE_TABLE)
    for new_insert in docx_methods_sql_values:
        conn.execute(new_insert)
    conn.commit()
    cursor = conn.execute(
        "SELECT name, args_number, first_arg, second_arg, third_arg,"
        " fourth_arg, fifth_arg, sixth_arg from DOCX_METHODS ")
    for row in cursor:
        print "NAME = ", row[0]
        print "ARGS_NUMBER = ", row[1]
        print "FIRST_ARG = ", row[2]
        print "SECOND_ARG = ", row[3]
        print "THIRD_ARG = ", row[4]
        print "FOURTH_ARG = ", row[5]
        print "FIFTH_ARG = ", row[6]
        print "SIXTH_ARG = ", row[7], "\n"
    conn.close()

if __name__ == '__main__':
    main()
