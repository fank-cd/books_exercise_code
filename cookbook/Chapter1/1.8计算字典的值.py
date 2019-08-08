
prices = {
    "ACME":45.8,
    "AAPL":612.78,
    "IBM":205.55,
    "HPQ":37.20,
    "FB":10.75
}

"""
假如我们需要知道股票价格最低的键值对是什么，这个问题有点麻烦吧
可以用zip，但是不够优雅,
注意，value相同时，会比较key
"""

min_key = min(prices,key=lambda k: prices[k]) 

print(min_key)