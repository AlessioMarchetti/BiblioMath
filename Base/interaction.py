from data import *
from html_generator import *
from ftp_loader import *


def prompt(data):
    txt = input('BiblioMath>> ')
    manage(txt, data)


def ask(txt):
    print(txt + '/n')
    return prompt()


def get_text(name):
    with open('text/{}.txt'.format(name), 'r') as f:
        return f.read()


def manage(txt, data):
    txt += ' '
    tt = txt.split(' ')
    if tt[0] == 'help':
        t = get_text('help')
        print(t)

    elif tt[0] == 'ins':
        if tt[1] == 'comm':
            c = ask_comment()
            data.insert_comment(c)
        elif tt[1] == 'book':
            b = ask_book()
            data.insert_book(b)
        elif tt[1] == 'cat':
            c = ask_category()
            data.insert_category(c)
        elif tt[1] == 'aut':
            a = ask_author()
            data.insert_author(a)

    elif tt[0] == 'print':
        if tt[1] == 'comm':
            print('Not available now. Wait for next version :)')
        elif tt[1] == 'book':
            books = data.get_book_list()
            out = ''
            for b in books:
                out += b.to_string() + '\n\n'
            print(out)
        elif tt[1] == 'cat':
            cats = data.get_cat_list()
            out = ''
            for c in cats:
                out += c.to_string() + '\n\n'
            print(out)
        elif tt[1] == 'aut':
            auts = data.get_aut_list()
            out = ''
            for a in auts:
                out += a.to_string() + '\n\n'
            print(out)

    elif tt[0] == 'upload':
        load('out')
        load_db(data.db_name)

    elif tt[0] == 'gen':
        tot_gen(data)

    elif tt[0] == 'quit':
        quit()

    elif tt[0] == 'exec':
        data.exec_script(txt[5:])

    else:
        print('Command unknow')


def get_db():
    txt = input('BiblioMath>> ') + ' '
    tt = txt.split(' ')
    if tt[0] == 'create':
        name = tt[1]
        os.remove(name)
        d = Data(name)
        return d
    elif tt[0] == 'use':
        name = tt[1]
        d = Data(name)
        return d
    elif tt[0] == 'download':
        ftp_get_db()
        d = Data('db.db')
        return d
    elif tt[0] == 'help':
        t = get_text('help')
        print(t)
    else:
        print('NOT VALID. You need to get a DB first')
        return get_db()


def interact():
    print(get_text('intro'))
    d = get_db()
    while True:
        prompt(d)


interact()
