# coding:utf-8
import collections
# 一摞Python风格的纸牌

Card = collections.namedtuple('Card', ['rank', 'suit'])  # namedtuple 具名元组 "Card"元组名 rank\suit 元素名


class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, postion):
        return self._cards[postion]


beer_card = Card("7", "diamonds")
print (beer_card)

deck = FrenchDeck()
print (len(deck))  # 因为我们写了__len__方法，所以才能直接调用len

print (deck[0])
print (deck[-1])
#  由于写了__getitem__方法，所以可以直接实现。因为实现了__getitem__方法，所以迭代也是可行的