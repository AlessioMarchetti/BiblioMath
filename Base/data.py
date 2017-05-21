import os
import sqlite3
from author import *
from book import *
from category import *
from comment import *


class Data:
    def __init__(self, db_name):
        self.db_name = db_name
        not_exists = not os.path.exists(db_name)
        self.conn = sqlite3.connect(db_name)
        if not_exists:
            self.conn.executescript(get_script('create'))

    def insert_author(self, author):
        sch = get_script('insert_author').format(author.name)
        self.conn.executescript(sch)
        cu = self.conn.cursor()
        cu.execute(get_script('get_aut_ids'))
        idm = cu.fetchall()[0][0]
        print('Created with id {}'.format(idm))

    def insert_category(self, category):
        sch = get_script('insert_category').format(category.name, category.parent_id)
        self.conn.executescript(sch)

    def insert_book(self, book):
        cu = self.conn.cursor()
        cu.execute(get_script('get_max_book_id'))
        try:
            book_id = int(cu.fetchall()[0][0])+1
        except:
            book_id = 1
        print('creating with id {}'.format(book_id))
        sch = get_script('insert_book').format(id=book_id, title=book.title)
        self.conn.executescript(sch)
        for id_aut in book.id_aut:
            sch = get_script('insert_aut_ref').format(id_book=book_id, id_aut=id_aut)
            self.conn.executescript(sch)
        for id_cat in book.id_cat:
            sch = get_script('insert_cat_ref').format(id_book=book_id, id_cat=id_cat)
            self.conn.executescript(sch)

    def insert_comment(self, comment):
        sch = get_script('insert_comment').format(id_book=comment.id_book, aut=comment.aut, comm=comment.comm)
        self.conn.executescript(sch)

    def exec_script(self, script):
        self.conn.executescript(script)

    def get_aut_list(self):
        sch = get_script('aut_list')
        cu = self.conn.cursor()
        cu.execute(sch)
        raw = cu.fetchall()
        res = []
        for el in raw:
            a = Author(el[1])
            a.id = el[0]
            res.append(a)
        return res

    def get_cat_list(self):
        sch = get_script('cat_list')
        cu = self.conn.cursor()
        cu.execute(sch)
        raw = cu.fetchall()
        res = []
        for el in raw:
            c = Category(el[1], el[2])
            c.id = el[0]
            res.append(c)
        return res

    def get_book_list(self):
        res = []
        cu = self.conn.cursor()
        sch = get_script('book_list')
        cu.execute(sch)
        for rw in cu.fetchall():
            id = rw[0]
            title = rw[1]
            b = Book()
            b.id = id
            b.title = title

            # find and insert authors
            sch = get_script('aut_from_book_id').format(id_book=id)
            cu.execute(sch)
            for aa in cu.fetchall():
                a = Author()
                a.name = aa[1]
                a.id = aa[0]
                b.aut.append(a)

            # find and insert categories
            sch = get_script('cat_from_book_id').format(id_book=id)
            cu.execute(sch)
            for cc in cu.fetchall():
                c = Category()
                c.id = cc[0]
                c.name = cc[1]
                c.parent_id = cc[2]
                b.cat.append(c)

            # find and insert comments
            sch = get_script('comm_from_book_id').format(id_book=id)
            cu.execute(sch)
            for cc in cu.fetchall():
                c = Comment()
                c.id = cc[0]
                c.comm = cc[1]
                c.aut = cc[2]
                b.comm.append(c)

            #add the book to the list
            res.append(b)
        return res

    def get_parent_category(self, id_category):
        cu = self.conn.cursor()
        sch = get_script('get_parent_category').format(id_category=id_category)
        cu.execute(sch)
        pp = cu.fetchall()[0]
        c = Category()
        c.id = pp[0]
        c.name = pp[1]
        c.parent_id = pp[2]
        return c


def get_script(name):
    with open('sqlite/{}.sql'.format(name), 'r') as f:
        return f.read()
