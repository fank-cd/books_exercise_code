from urllib.request import urlopen


class UrlTemplate(object):
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))
    
# Demo
yahoo = UrlTemplate("https://finace.yahoo.com/d/quotes?={names}&f={fields}")
for line in yahoo.open(names="IBM",fields="sl1c1v"):
    print(line)

# 以上这个类可以用闭包函数来代替

def urltemplate(template):
    def opener(**kwargs):
        return urlopen(self.template.format_map(kwargs))
    return opener

# 闭包的核心特性就是它可以记住闭包时的环境
# 无论何时，当在编写代码中遇到需要附加额外的状态给函数时，请考虑使用闭包