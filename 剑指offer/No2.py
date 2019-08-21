def func_wrap():
    def prt_func():
        return 'hello,world'
    return prt_func

hlowld = func_wrap()
print(hlowld)