# coding:utf-8
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 import urlopen as uopen

# 这段代码一直503错误，应该是亚马逊做了其他反爬策略，这里就学习代码好了

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


def _main():
    print("AT", ctime(), "on Amazon...")
    for isbn in ISBNs:
        showRanking(isbn)

@register
def atexit():
    print("All Done at", ctime())

if __name__ == '__main__':
    main()

