from collections import defaultdict
total = defaultdict(int)
#  搜索+记忆算法

def fib_test(k):
    assert k > 0
    if k in [1, 2]:
        return 1
    global total
    if k in total:
        result = total[k]
    else:
        result = fib_test(k-1) + fib_test(k-2)
        total[k] = result
    return result


if __name__ == "__main__":
    print(fib_test(6))
