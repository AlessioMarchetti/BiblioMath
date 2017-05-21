class Category:
    def __init__(self, name='', parent_id=0):
        self.id = -1
        self.name = name
        self.parent_id = parent_id

    def to_string(self):
        r = ''
        r += 'Id: {}'.format(self.id) + '\n'
        r += 'Name: ' + self.name
        return r


def ask_category():
    c = Category()
    c.name = input('Name: ')
    c.parent_id = input('Parent id (unique): ')
    return c
