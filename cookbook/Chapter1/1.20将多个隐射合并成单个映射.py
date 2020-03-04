from collections import ChainMap

if __name__ == "__main__":
    a = {"x":1,"z":3}
    b = {"y":2,"z":4}
    c = ChainMap(a,b)

    print(c)
    print(c['x'],c['y'])
    """
    这样比直接update更好更优雅，而且原始数据改变之后，ChainMap也会跟着变
    另外如果改变C的值，总是会作用在列出的第一个映射结构上
    """