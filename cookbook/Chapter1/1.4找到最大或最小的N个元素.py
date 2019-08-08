# 找到最大或最小的N个元素

# 在某个集合中找出最大或者最小的N元素
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3,nums))  # [42, 37, 23]

print(heapq.nsmallest(3,nums))  # [-4, 1, 2]



portfolio = [
    {'name': "IBM", "share": 100, "price": 91},
    {'name': "AAPL", "share": 50, "price": 543.22},
    {'name': "IBM", "share": 200, "price": 21.09},
    {'name': "IBM", "share": 35, "price": 31.57},
    {'name': "IBM", "share": 45, "price": 16.35}

]

cheap = heapq.nsmallest(3,portfolio,key=lambda s:s["price"])
print(cheap)
