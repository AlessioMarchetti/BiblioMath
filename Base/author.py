class Author:
    def __init__(self, name=''):
        self.id = -1
        self.name = name

    def to_string(self):
        str = ''
        str += 'Id: {}'.format(self.id) + '\n'
        str += 'Name: ' + self.name
        return str


def ask_author():
    a = Author()
    a.name = input('Name: ')
    return a
