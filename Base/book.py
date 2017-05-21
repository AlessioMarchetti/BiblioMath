class Book:
    def __init__(self):
        self.id = -1
        self.title = ''
        self.aut = []
        self.cat = []
        self.id_aut = []
        self.id_cat = []
        self.comm = []

    def to_string(self):
        str = ''
        str += 'Id: {}'.format(self.id) + '\n'
        str += 'Title: ' + self.title
        return str


def ask_book():
    b = Book()
    b.title = input('Title: ')
    b.id_aut = input('Authors: ').split(',')
    b.id_cat = input('Categories: ').split(',')
    return b
