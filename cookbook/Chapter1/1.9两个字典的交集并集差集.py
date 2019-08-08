
a = {
    "x" : 1,
    "y" : 2,
    "z" : 3,
}

b = {
    "w" : 10,
    "x": 11,
    "y": 2
}

# 交集
common = a.keys() & b.keys()

# a有b无
diff = a.keys() - b.keys()

# find key,value pairs in common
common_pairs =  a.items() & b.items()

print(common,diff,common_pairs)
"""
可以通过这个来过滤一些特有的key
"""