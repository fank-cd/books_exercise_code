"""
我们需要将字符串拆分为不同的字段，但是分隔符（以及分隔符中间的空格）在整个字符串中不一致
应该怎么办？

split()方法只能处理非常简单的情况，而且不支持多个分隔符
这时候应该使用re.split()
"""
import re

line = "asdf jkjdf; jlkdas, qieu.          foo"

res = re.split(r"[;,.]\s*",line)
print(res)
# output 
# ['asdf jkjdf', 'jlkdas', 'qieu', 'foo']