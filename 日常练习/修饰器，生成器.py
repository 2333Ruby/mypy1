'''装饰器@，生成器 yeild，next'''

# ye = (i for i in range(10))
# # print(next(ye))
# #
# #
# # def yield_test():
# #     print('start')
# #     yield 1
# #     print('end')
# #     yield 2
# #
# #
# # obj = yield_test()
# # print(next(obj))
# print(next(obj))


import time


def timer(func):     # 定义一个名为 timer() 的装饰器函数，它接受一个参数 func这个 func 就是即将要被修饰的函数
    def wrapper(*args, **kwargs):  # 在 timer() 函数内部，定义一个名为 wrapper() 的闭包函数
        start_time = time.time()  # 在调用 wrapper() 函数时，它会根据传入的参数来调用被修饰的函数 func，并在函数执行前后记录时间
        res = func(*args, **kwargs)
        stop_time = time.time()
        print('run time is %s' % (stop_time - start_time))
        return res  # 同时输出函数执行时间。最后，它将 func 函数的返回值返回

    return wrapper


@timer  # 使用装饰器语法来对函数进行装饰，在函数定义前加上 @timer 这样的语句
def index():
    time.sleep(1)
    print('Welcome to the index page')
    return 200
index()
# 调用 index() 函数时，会自动将其转换成 timer(index)() 这样的形式，将 index 函数作为参数传递给 timer() 函数，并将返回值再次作为函数调用。由于 timer() 函数返回了一个闭包函数
# wrapper()，所以最终的函数调用结果就是执行了闭包函数 wrapper()
'''

from types import MethodType


class Student(object):
    pass


def set_name(self, name):
    self.name = name


s1 = Student()
s2 = Student()
# 方法绑定到s1实例的set_name_func 属性上
s1.set_name_func = MethodType(set_name, s1)
# 调用方法
s1.set_name_func('s1')
print(s1.name)

s2.set_name_func('s2')  # 会报错,因为set_name方法在实例间不共享
print(s2.name)

'''output:
s1
AttributeError: 'Student'
object
has
no
attribute
'set_name_func'
'''
from types import MethodType


class Student(object):
    pass


def set_name(cls, name):
    cls.name = name


s1 = Student()
s2 = Student()
s3 = Student()
# 将方法绑定到类上,此时方法为类方法,操作的属性也变成类属性
Student.set_name_func = MethodType(set_name, Student)
# s1,s2均可调用set_name_func方法,说明此时方法为类方法
s1.set_name_func('s1')
s2.set_name_func('s2')

# s3有name属性,且值为2,说明此时属性为类属性
print(s1.name)
print(s2.name)
print(s3.name)

# output:
# 2
# 2
# 2
'''