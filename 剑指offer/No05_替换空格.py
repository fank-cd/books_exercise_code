"""
题目：请实现一个函数，把字符串中的每个空格替换成'%20'。例如,输入
“We are happy.”，则输出"We%20are%20happy."

这一道题在python里面写，比较扯淡。当然python的replace是新开的空间
这一道题目是在C++里面更有意义。简单来说就是通过快慢指针从后遍历。
"""

def replace_space(string):
    """
    O(n)
    """
    if not isinstance(string, str) or len(string) == 0:
        return None

    string = list(string)
    p1 = len(string) - 1
    for ch in string:
        if ch == " ":
            string.append(None)
            string.append(None)

    p2 = len(string) - 1
    while p1 != p2:
        if string[p1] != " ":
            string[p2] = string[p1]
            p2 -= 1
        else:
            string[p2 - 2:p2 + 1] = ["%", "2", "0"]
            p2 -= 3
        p1 -= 1
    return "".join(string)


if __name__ == "__main__":
    print(replace_space("we are friend"))


