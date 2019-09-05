# 面试题20：表示数值的字符串
# 题目：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100"、"5e2"、"-123"、"3.1416"、及"-1E-16"都表示
# 数值，但"12E"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

# # 读不懂题意，留下代码，暂时空着


def is_numeric(string):
    if not isinstance(string, str):
        return False

    index = 0
    result, index = scan_integer(string, index)
    if index < len(string) and string[index] == '.':
        index += 1
        has_float, index = scan_unsigned_integer(string, index)
        result = result or has_float

    if index < len(string) and string[index] in ('e', 'E'):
        index += 1
        has_exp, index = scan_integer(string, index)
        result = result and has_exp
    return result and index == len(string)


def scan_integer(string, index):
    if index < len(string) and string[index] in ('-', '+'):
        index += 1
    return scan_unsigned_integer(string, index)


def scan_unsigned_integer(string, index):
    old_index = index
    while index < len(string) and string[index] in '0123456789':
        index += 1
    return (old_index != index), index


if __name__ == "__main__":
    print(is_numeric("+100"))
    print(is_numeric("5e2"))
    print(is_numeric("-200"))
    print(is_numeric("3.1415926"))
    print(is_numeric("1.34e-2"))
    print(is_numeric("1.34e"))
