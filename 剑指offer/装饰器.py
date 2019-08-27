# def use_logging(func):
#     def wrapper():
#         print(f"{func.__name__} is running ")
#         return func()
#     return wrapper

# def bar():
#     print("i am bar")
# bar = use_logging(bar)
# bar()

# @use_logging
# def foo():
#     print("i am foo")

# foo()

# 带参数的装饰器

# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == "warn":
#                 print(f"{func.__name__} is running ")
#             return func()
#         return wrapper
#     return decorator

# @use_logging(level="warn")
# def foo(name="foo"):
#     print(f"i am {name}")

# foo()

