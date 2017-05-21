from ftplib import FTP
import os.path


def clear_ftp(ftp, path):
    ftp.cwd(path)
    for f in ftp.nlst():
        if f == 'save_this':
            continue
        try:
            ftp.delete(f)
        except Exception:
            clear_ftp(ftp, f)
            ftp.rmd(f)
    ftp.cwd('..')


def upload_this(path, myFTP):
    files = os.listdir(path)
    os.chdir(path)
    for f in files:
        if os.path.isfile(f):
            fh = open(f, 'rb')
            myFTP.storbinary('STOR {}'.format(f), fh)
            fh.close()
        elif os.path.isdir(f):
            myFTP.mkd(f)
            myFTP.cwd(f)
            upload_this(f, myFTP)
    myFTP.cwd('..')
    os.chdir('..')


def load(path):
    ftp = FTP('ftp.bibliomath.altervista.org')
    passwd = 'lageologianone\'unaverascienza'
    ftp.login(user='bibliomath', passwd=passwd)
    clear_ftp(ftp, '.')
    upload_this(path, ftp)
    ftp.close()


def load_db(path):
    ftp = FTP('ftp.bibliomath.altervista.org')
    passwd = 'lageologianone\'unaverascienza'
    ftp.login(user='bibliomath', passwd=passwd)
    f = open(path, 'rb')
    ftp.storbinary('STOR db.db', f)
    f.close()
    ftp.close()


def ftp_get_db():
    ftp = FTP('ftp.bibliomath.altervista.org')
    passwd = 'lageologianone\'unaverascienza'
    ftp.login(user='bibliomath', passwd=passwd)
    file = open('db.db', 'wb')
    ftp.retrbinary('RETR db.db', file.write)
    file.close()
