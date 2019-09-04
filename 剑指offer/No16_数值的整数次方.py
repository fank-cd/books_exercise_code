# 面试题16：数值的整数次方
# 题目：实现函数double Power(base,exponent),求base的exponent次方
# 不得使用库函数，同事不需要考虑大数问题
# 考虑指数为负数的情况，和指数为负数且底数为零的情况

def power(base, exponent):
    if base == 0 and exponent == 0:
        return None

    unsigned_exponent = exponent if exponent >= 0 else abs(exponent)
    result = unsigned_power(base, unsigned_exponent)
    if exponent < 0:
        return 1.0 / result
    return result

def unsigned_power(base, unsigned_exponent):
    """
    二分法计算a的b次方
    """
    if unsigned_exponent == 0:
        return 1

    if unsigned_exponent == 1:
        return base

    result = unsigned_power(base, unsigned_exponent >> 1)  
    # 右移运算符代替除以2，效率高
    result *= result
    if unsigned_exponent & 1 == 1: # 用位与运算符来代替求余运算符
        result *= base
    return result


if __name__ == "__main__":
    print(power(2, -4))
