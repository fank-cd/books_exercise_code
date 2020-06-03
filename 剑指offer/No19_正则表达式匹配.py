# 面试题19：正则表达式匹配
# 题目：请实现一个函数用来匹配包含"."和"*"的正则表达式。
# 模式中的字符 '.' 表示任意一个字符，而 '*'表示它前面的字符
# 可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符
# 匹配整个模式。例如字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与
# "aa.a"和"ab*a"均不匹配

def match(string,pattern):
    if string is None or pattern is None:
        return None
    return match_core(string,pattern)

def match_core(string,pattern):
      # 没有pattern了却还有字符串
    if len(pattern) == 0 and len(string) != 0:
        return False

    # 没有字符串了，看pattern剩下的是不是0个或者n个"'ch'*"
    if len(string) == 0:
        while len(pattern) >= 2 and pattern[1] == '*':
            pattern = pattern[2:]
        return len(pattern) == 0

        # 剩余pattern以"'ch'*"开头，
        # 直到string的第一个字符不是ch的时候再去掉pattern中的"'ch'*"
    if len(pattern) >= 2 and pattern[1] == '*':
        if string[0] == pattern[0]:
            return match_core(string[1:], pattern)

        return match_core(string, pattern[2:])

    if string[0] == pattern[0] or pattern[0] == '.':
        return match_core(string[1:], pattern[1:])

    return False

if __name__ == "__main__":
    print(match("aaaefwe", "aa*"))

# 更优雅的写法

def isMatch(text,pattern):
    if not pattern:
        return not text
    first_match = bool(text) and pattern[0] in {text[0],"."}

    if len(pattern) >= 2 and pattern[1] == "*":
        return (isMatch(text,pattern[2:])) or first_match and isMatch(text[1:],pattern)

    else:
        return first_match and isMatch(text[1:],pattern[1:])