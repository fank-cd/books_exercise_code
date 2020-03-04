#一般的情况，用str.replace()即可，但是一些特殊情况，可以用re模块

import re

text = "Tody is 11/27/2012. PyCon starts 3/13/2013."
res = re.sub(r"(\d+)/(\d+)/(\d+)",r"\3-\1-\2",text)
print(res)  #output Tody is 2012-11-27. PyCon starts 2013-3-13.
# \3的意思捕获组的位置