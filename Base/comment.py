class Comment:
    def __init__(self):
        self.id = -1
        self.id_book = -1
        self.comm = ''
        self.aut = ''


def ask_comment():
    c = Comment()
    c.id_book = input('Id Book: ')
    c.aut = input('Author: ')
    c.comm = input('Text: ')
    return c
