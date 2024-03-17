# # # # Making a nested function
def main_func(f_str):
    def nest_fun():
        new_str = f_str.swapcase()
        return new_str
    return nest_fun()
# # #
rs = main_func('Anup')
print(rs)
# # # #
# # # # Making an alias of a function
mf = main_func
print(id(mf))
print(id(main_func))
hx = hex(id(mf))
print(hx)
print(main_func, type(main_func))
print(mf, type(mf))
res = mf('Skyscend')
print(res)


# Passing function as argument
def mul_2(f_str):
    return f_str * 2

def mul_3(x):
    return x * 3
#
# #
def main_func(func):
    print(func)
    f_str = 'Hello'
    return func(f_str)
# # #
# # # #
res = main_func(mul_2)
print(res)
#
res = main_func(mul_3)
print(res)


# # # Returning a function
# def main_func(f_str):
#     def nest_fun():
#         new_str = f_str.swapcase()
#         return new_str
#     return nest_fun
# # # #
# # # #
# rs = main_func('Hello')
# print(rs, type(rs))
# print(rs())


# # # Creating a decorator
# def dec_func(func):
#     def inner_func():
#         # print(globals())
#         # print(locals())
#         fn = func()
#         return fn.swapcase()
#     return inner_func
# # # #
# def mul_2():
#     return 'Hello' * 2
# # #
# dec = dec_func(mul_2)
# print(dec)
# res = dec()
# print(res)

# # # # Actual Decorator usage
# def dec_func(func):
#     print("Decorator Function", func)
#     def inner_func():
#         print("Inner Function", func)
#         fn = func()
#         return fn.swapcase()
#     return inner_func
# # # # # #
# @dec_func
# def mul_2():
#     print("Mul")
#     return 'Hello' * 2
# # # #
# @dec_func
# def add():
#     print("Add")
#     return "Hello" + " Skyscend"
# # # #
# print(mul_2)
# z = mul_2()
# print(z)
# # # #
# z = add()
# print(z)

# # # # Applying Multiple Decorators
# def dec_func(func):
#     print("Dec1",func)
#     def inner_func():
#         print("INNER 1", func)
#         fn = func()
#         print("FN1",fn)
#         return fn.swapcase()
#     return inner_func
# #
# #
# def dec_func2(func):
#     print("Dec2",func)
#     print("Decorator 2")
#     def inner_func2():
#         print("INNER 2", func)
#         fn = func()
#         print("FN2", fn)
#         print("Decorator Inner 2")
#         return fn.replace('ello', 'i')
#     return inner_func2
# #
# @dec_func
# @dec_func2
# def mul_2():
#     print("MUL2")
#     return 'Hello' * 2
# # #
# print("MUL2",mul_2)
# rs = mul_2()
# print(rs)


# # # # Passing Parameters to Function which is using decorator
# def dec_func(func):
#     def inner_func_with_args(x, y):
#         print("INNNER",x, y)
#         # addition of square
#         x **= 2  # x = x ** 2
#         y **= 2
#         z = x + y
#         return func(x, y, z)
#     return inner_func_with_args
#
# @dec_func
# def add(x, y, z):
#     print("ADD",x, y, z)
#     return x + y + z
# #

# add = dec_func(add)
# rs = add(3, 4)
# print(rs)

# # # Passing more params while calling the function
# def dec_func(func):
#     def inner_func_with_args(x,y,z):
#         print("INNER",x,y,z)
#         # addition of square
#         x **= 2  # x = x ** 2
#         y = (y + z) ** 2
#         return func(x, y)
#     return inner_func_with_args
#
# @dec_func
# def add(x, y): # add = dec_func(add)
#     print("ADD", x, y)
#     return x + y
# #
#
# # add = dec_func(add)
# print(add)
# rs = add(3,4,5)
# print(rs)

#
# # # # # Passing arguments to decorator
# import time
#
# def dec_mkr(p, q, r):
#     print("MKR",p,q,r)
#     def dec_func(func):
#         print("DEC",func)
#         def inner_func_with_args(a, b):
#             print("INR",a,b)
#             # addition of square
#             a **= 2
#             b **= 2
#             z = p + q + r
#             w = a + b
#             print(z, w)
#             time.sleep(5)
#             return func(z, w)
#         return inner_func_with_args
#     return dec_func
# # #
# #
# @dec_mkr(10, 15, 20)
# def mul(i, j):
#     time.sleep(3)
#     print("MUL", i, j)
#     return i * j
# # #
# #
# rs = mul(3, 4)
# time.sleep(2)
# print(rs)