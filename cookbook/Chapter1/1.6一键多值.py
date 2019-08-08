from collections import defaultdict

'''
比如你需要这的字典
d = {
    "a":[1,2,3],
    "b":[4,5]
    }
或者

e = {
    "a":{1,2,3},
    "b":{4,5},
}

构造起来其实是容易的，不过在初始化的时候可能会遇到一些麻烦，比如你需要这样初始化
d = {}
for key,value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

用defaultdict就方便很多
'''

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
