import os


def gen_books(books):
    txt = get_html('list')
    records = ''
    for b in books:     # todo: Mabye we could use another template here?
        t = '\t<tr><td><a href="books/{}.html">'.format(b.id)
        t += str(b.id)
        t += '</a></td><td>'
        t += b.title
        t += '</td><td>'
        for a in b.aut:
            t += a.name + ', '
        t = t[:-2]
        t += '</td><td>'
        for c in b.cat:
            t += c.name + ', '
        t = t[:-2]
        t += '</td></tr>\n'
        records += t
    txt = txt.format(what='books', record=records)
    return txt


def gen_book(book):
    txt = get_html('detail')
    dict = {}
    dict['id'] = book.id
    dict['title'] = book.title
    authors = ''
    for a in book.aut:
        authors += a.name
        authors += '<br>'
    dict['authors'] = authors
    cate = ''
    for c in book.cat:
        cate += c.name
        cate += '<br>'
    dict['categories'] = cate
    coms = ''
    for c in book.comm:
        coms += 'Comment by {aut}<br><p>{com}</p>'
        coms = coms.format(aut=c.aut, com=c.comm)
    dict['comments'] = coms
    txt = txt.format(**dict)
    return txt


def tot_gen(data):
    os.makedirs('out', exist_ok=True)
    os.makedirs('out/books', exist_ok=True)
    fl = open('out/index.html', 'w')
    book_list = data.get_book_list()
    fl.write(gen_books(book_list))
    fl.close()
    for b in book_list:
        name = 'out/books/{}.html'.format('{}'.format(b.id))
        fl = open(name, 'w')
        fl.write(gen_book(b))
        fl.close()


def get_html(name):
    with open('html/{}.html'.format(name), 'r') as f:
        return f.read()
