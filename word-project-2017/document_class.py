# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Pt
from docx.shared import RGBColor
from docx.shared import Inches
import os
import subprocess
import docx2txt

TABLE_STYLE = 'Table Grid'

colors = {'red': (0xff, 0x0, 0x0), 'green': (0x0, 0xff, 0x0), 'blue': (0x0, 0x0, 0xff), 'black': (0x0, 0x0, 0x0)}
class Documents():
    def __init__(self):
        self.__path = ''
        self.__document = Document()
        self.__document.save('beta.docx')
        self.__table = []


    def save_doc(self, args_list):
        path = args_list[0]
        name = args_list[1]
        if not os.path.exists(path):
            return 'the path does not exists'
        self.__path = path + '\\' + name + '.docx'
        print 'saving document'
        print path
        self.__document.save(path + '\\' + name + '.docx')
        os.remove('beta.docx')
        return 'document saved successfully'


    def add_new_picture(self, args_list):
        path = args_list[0]
        width = args_list[1]
        if not os.path.exists(path):
            return 'the path does not exists'
        self.__document.add_picture(path, width=Inches(float(width)))
        return 'picture added successfully'

    def add_new_table(self, args_list):
        rows = args_list[0]
        lines = args_list[1]
        table = self.__document.add_table(rows=int(rows), cols=int(lines))
        table.style = TABLE_STYLE
        self.__table.append(table)
        return 'table added successfully'



    def write_to_table(self, args_list):
        what_table = args_list[0]
        if int(what_table) > len(self.__table):
            return 'there is no such table'
        row = args_list[1]
        if len(self.__table[int(what_table)].rows) < int(row):
            return 'there is no such row number'
        column = args_list[2]
        if len(self.__table[int(what_table)].columns) < int(column):
            return 'there is no such column number'
        text = args_list[3]
        cell = self.__table[int(what_table)].cell(int(row), int(column))
        cell.text = text
        return 'successfully writen to table'

    def add_new_paragraph(self, args_list):
        text = args_list[0]
        style = args_list[1]
        color = args_list[2]
        if color not in colors:
            return 'there is no such color'
        size = args_list[3]
        font_name = args_list[4]
        run = self.__document.add_paragraph().add_run(text)
        font = run.font
        font.name = font_name
        font.color.rgb = RGBColor(colors[color][0], colors[color][1], colors[color][2])
        font.size = Pt(int(size))
        if style == 'bold':
            font.bold = True
        elif style == 'italic':
            font.italic = True
        elif style == 'none':
            pass
        else:
            return 'there is not such style'
        return 'paragraph added successfully'



    def import_existing_doc(self, args_list):
        path = args_list[0]
        if not os.path.exists(path):
            return 'the path does not exists'
        self.__document = Document(path)
        return 'successfully imported a document'

    def add_new_heading(self, args_list):
        text = args_list[0]
        self.__document.add_heading(text, level=0)
        return 'heading added successfully'

    def add_new_page_break(self, args_list):
        print 'adding new page break'
        self.__document.add_page_break()
        return 'added new page break successfully'

    def return_to_last_save(self, args_list):
        if os.path.exists('beta.docx'):
             return 'there is no last save'
        self.__document = Document(self.__path)
        return 'returned to the last save'

    def live_docx(self, args_list):
        if os.path.exists('beta.docx'):
            self.__document.save('beta.docx')
            live_view = docx2txt.process('beta.docx')
        else:
            live_view = docx2txt.process(self.__path)
        return '\n'+str(live_view)+'\n'


    def email_doc(self, args_list):
        from_email = args_list[0]
        to_email = args_list[1]
        pass



