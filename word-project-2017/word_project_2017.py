# -*- coding: utf-8 -*-
import sqlite3

DOCX_SQL_FILE_NAME = 'docx_funcs.sql'
CREATE_TABLE = '''CREATE TABLE DOCX_METHODS
(NAME TEXT PRIMARY KEY    NOT NULL,
ARGS_NUMBER INT     NOT NULL,
FIRST_ARG TEXT, SECOND_ARG TEXT, THIRD_ARG TEXT, FOURTH_ARG TEXT, FIFTH_ARG TEXT, SIXTH_ARG TEXT)'''

docx_methods_sql_values = [
    "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('write to table', 6,'what_table(starts for 0)', 'row', 'column', 'text', null, null )",
     "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('save doc', 2, 'path', 'name', null, null, null, null )",
      "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('add new picture',2,'path', 'width(in inches)',null, null, null, null )",
       "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('add new table' ,2,'rows', 'lines', null, null, null, null )",
        "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('add new paragraph', 5, 'text', 'style(bold, italic or none)', 'color(black, blue, green or red)', 'size', 'font_name', null )",
          "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('add new heading' ,1 , 'text', null, null, null, null, null )",
           "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('add new page break', 0, null, null, null, null, null, null )",
            "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('email doc', 2, 'from_email', 'to_email', null, null, null, null )",
             "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('import existing_doc', 1, 'path', null, null, null, null, null )",
              "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('return to last save', 0, null, null, null, null, null, null )",
               "INSERT INTO DOCX_METHODS (NAME,ARGS_NUMBER,FIRST_ARG,SECOND_ARG,THIRD_ARG, FOURTH_ARG, FIFTH_ARG, SIXTH_ARG) \
      VALUES ('live docx', 0, null, null, null, null, null, null )"]

def main():
    conn = sqlite3.connect(DOCX_SQL_FILE_NAME)
    conn.execute(CREATE_TABLE)
    for new_insert in docx_methods_sql_values:
        conn.execute(new_insert)
    conn.commit()
    cursor = conn.execute("SELECT name, args_number, first_arg, second_arg, third_arg, fourth_arg, fifth_arg, sixth_arg from DOCX_METHODS ")
    for row in cursor:
        print "NAME = ", row[0]
        print "ARGS_NUMBER = ", row[1]
        print "FIRST_ARG = ", row[2]
        print "SECOND_ARG = ", row[3]
        print "THIRD_ARG = ", row[4]
        print "FOURTH_ARG = ", row[5]
        print "FIFTH_ARG = ", row[6]
        print "SIXTH_ARG = ", row[7], "\n"
    cursor = conn.execute("SELECT args_number FROM DOCX_METHODS WHERE name = 'add_new_page_break' or name = 'email_doc' ")
    for raw in cursor:
        print raw[0]

    conn.close()

if __name__ == '__main__':
    main()