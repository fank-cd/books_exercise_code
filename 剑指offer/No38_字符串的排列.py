# 题目：输入一个字符串，打印出该字符串中字符的所有排列。
# 例如，输入字符串abc，则打印出由字符a,b,c所能排列出来的
# 所有字符串
# 妈耶 看不懂

def permutaion(string):
    if not isinstance(string, str):
        return None

    permutaion_core(list(string), 0)


def permutaion_core(list_of_char, index):
    if not isinstance(list_of_char, list) or not isinstance(index, int) or index > len(list_of_char):
        return None

    if index == len(list_of_char):
        print("".join(list_of_char))

    for i in range(index, len(list_of_char)):
        list_of_char[i], list_of_char[index] = list_of_char[index], list_of_char[i]
        permutaion_core(list_of_char, index + 1)
        list_of_char[i], list_of_char[index] = list_of_char[index], list_of_char[i]


if __name__ == "__main__":
    permutaion("abc")
