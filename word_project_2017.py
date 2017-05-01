# -*- coding: utf-8 -*-
import sqlite3

DOCX_SQL_FILE_NAME = 'docx_funcs.sql'
CREATE_TABLE = '''CREATE TABLE DOCX_METHODS
(NAME TEXT PRIMARY KEY    NOT NULL,
ARGS_NUMBER INT     NOT NULL,
FIRST_ARG TEXT, SECOND_ARG TEXT, THIRD_ARG TEXT, FOURTH_ARG TEXT, FIFTH_ARG TEXT)'''

docx_methods_sql_values = [
    "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG) \
      VALUES ('write_to_table', 5,'row', 'column', 'text', 'style', 'color' )",
     "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG) \
      VALUES ('save_doc', 1, 'path', null, null, null, null )",
      "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG) \
      VALUES ('add_new_picture',1, 'width', null, null, null, null )",
       "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG) \
      VALUES ('add_new_table' ,2,'rows', 'lines', null, null, null )",
        "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG) \
      VALUES ('add_new_paragraph', 3, 'text', 'style', 'color', null, null )",
         "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG) \
      VALUES ('add_new_word' ,3 ,'text', 'style', 'color', null, null )",
          "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG) \
      VALUES ('add_new_heading' ,3 , 'text', 'style', 'color', null, null )",
           "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG) \
      VALUES ('add_new_page_break', 0, null, null, null, null, null )",
            "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG) \
      VALUES ('email_doc', 2, 'from_email', 'to_email', null, null, null )"]

def main():
    conn = sqlite3.connect(DOCX_SQL_FILE_NAME)
    # conn.execute(CREATE_TABLE)
    # for new_insert in docx_methods_sql_values:
    #     conn.execute(new_insert)
    # conn.commit()
    cursor = conn.execute("SELECT name, args_number, first_arg, second_arg, third_arg, fourth_arg, fifth_arg from DOCX_METHODS ")
    for row in cursor:
        print "NAME = ", row[0]
        print "ARGS_NUMBER = ", row[1]
        print "FIRST_ARG = ", row[2]
        print "SECOND_ARG = ", row[3]
        print "THIRD_ARG = ", row[4]
        print "FOURTH_ARG = ", row[5]
        print "FIFTH_ARG = ", row[6], "\n"
    cursor = conn.execute("SELECT args_number FROM DOCX_METHODS WHERE name = 'add_new_page_break' or name = 'email_doc' ")
    for raw in cursor:
        print raw[0]

    conn.close()

if __name__ == '__main__':
    main()