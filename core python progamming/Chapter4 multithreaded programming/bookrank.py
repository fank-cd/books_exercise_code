# coding:utf-8
from atexit import register
from re import compile
from threading import Thread
from time import  ctime
from urllib2 import urlopen as uopen

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}


def getRanking(isbn):
    page = uopen('%s%s' % (AMZN, isbn))
    data = page.read()
    print data
    page.close()
    return REGEX.findall(data)[0]


def showRanking(isbn):
    print("- %r ranked %s" % (ISBNs[isbn], getRanking(isbn)))


def main():
    print("AT", ctime(), "on Amazon...")
    for isbn in ISBNs:
        showRanking(isbn)

@register
def atexit():
    print("All Done at", ctime())

if __name__ == '__main__':
    main()

