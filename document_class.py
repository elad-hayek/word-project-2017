# -*- coding: utf-8 -*-
from docx import Document


class Documents(Document):
    def __init__(self, path=''):
        self.document__ = super(Documents, self).__init__(path)


    def save_doc(self, path):
        self.document__save(path)

    def add_new_picture(self, width):
        pass

    def add_new_table(self, rows, lines):
        pass

    def write_to_table(self, line, text, style, color):
        pass

    def add_new_paragraph(self, text, style, color):
        pass

    def add_new_word(self, text, style, color):
        pass

    def add_new_heading(self, text, style, color):
        pass

    def add_new_page_break(self):
        pass

    def email_doc(self, from_email, to_email):
        pass
