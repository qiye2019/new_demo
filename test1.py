''' 一些简单的python基础题目'''

'''字典求key value'''
info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '地球亚洲中国北京'}
# for key,value in info.items():
# print(key,value)

'''z针对列表内字典的值对列表进行排序(列表的sort方法的用法)'''
li = [{'a': '23'}, {'a': '25'}]


def takeSecond(li):
    s = li['a']
    return int(s)


li.sort(key=takeSecond)
# print(li)

'''列表去重（保证原来顺序）'''
li1 = [13, 77, 23, 89, 77, 12, 11]


# 1 set+sort 去重 (保持原顺序)
def lister(L):
    temp = list(set(L))
    temp.sort(key=L.index)
    return temp


# a = lister(li1)
# print(a)

# 2 利用索引去重 list.index(n)
new_li = []
for index, num in enumerate(li1):
    if li1.index(num) == index:
        new_li.append(num)


# print(new_li)

# 3 for 循环去重
def lister2(L):
    temp = []
    for i in L:
        if i not in temp:
            temp.append(i)
    return temp


# a = lister2(li1)
# print(a)

# 列表推导式去重
def lister3(L):
    temp = []
    [temp.append(i) for i in L if i not in L]
    return temp


# a = lister3(li1)
# print(a)

'''lambda函数'''


# 1
def add(x, y):
    return x + y


add2 = lambda x, y: x + y
# print(add(1,2))

# 2
import time

time.sleep = lambda x: None
time.sleep(10)

# 3 和高阶函数共用
li2 = [('a', 1), ('b', 2), ('c', 3)]
f = list(map(lambda x: x[0], li2))
# print(f)  # ['a', 'b', 'c']

'''高阶函数'''
'''map函数和reduce函数 映射和累积
map函数在python3中结果返回的是迭代器
'''
from functools import reduce


# 计算积
def square(x, y):
    return x * y


b1 = reduce(square, [3, 6, 9])  # 结果 162
b2 = reduce(lambda x, y: x * y, [3, 6, 9])  # 结果 162
b3 = map(lambda x: x ** 2, [3, 6, 9])  # 结果是 [9, 36, 81]
# print(b1,b2,list(b3))

'''sorted函数'''
a = [5, 7, 6, 3, 4, 1, 2]
b = sorted(a)
# sorted 函数返回一个新的函数 ，id不同 不改变原来的列表
# print(a,b) # 结果 [5, 7, 6, 3, 4, 1, 2] [1, 2, 3, 4, 5, 6, 7]

'''sort和sorted对比
sorted是python内置方法 可以对所有可迭代对象进行排序  不改变原对象，返回新对象
sort是列表的一个方法 无返回值，改变原列表
'''
# 根据列表内元组第一个元素顺序对列表进行排序
random = [(2, 2), (3, 4), (4, 1), (1, 3), (4, 4)]


def takeFirst(L):
    return L[0]


# print(sorted(random,key=takeFirst)) # 需要接收可迭代对象
# print(random)
random.sort(key=takeFirst)
# print(random)

# 按年龄升序
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
v = sorted(students, key=lambda s: s[2])  # 默认升序 reverse = False
print(v)

'''反转list.reverse()方法和reversed()函数（同上sorted()函数）'''
alist = [123, 'xyz', 'zara', 'abc', 'xyz']
aalist = [1, 2, 4, 6]

blist = reversed(alist)
alist.reverse()

bblist = reversed(aalist)
aalist.reverse()

# print(list(blist),alist)
# print(list(bblist),aalist)
# 结果[123, 'xyz', 'zara', 'abc', 'xyz'] ['xyz', 'abc', 'zara', 'xyz', 123]
# [1, 2, 4, 6] [6, 4, 2, 1]

'''拆包
需要拆的数据的个数要与变量的个数相同，否则程序会异常'''

# 列表拆包
my_list = [1, 3.14, 'qq', True]
num, pi, my_str, my_bool = my_list
print(my_bool)

# 字典拆包
my_dict = {"name": "老王", "age": 19}
ret1, ret2 = my_dict
# 得到的是key  字典是无序的
print(ret1, ret2)  # name age

'''引用传递'''


# 函数参数的传递是引用传递 不是值传递
def foo(arg):
    arg = 2
    print(arg)  # 2


a = 1
foo(a)
print(a)  # 1

''' 单例模式'''


# 装饰器实现

# 类方法实现
class Singleton(object):
    def __init__(self):
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        pass


a = Singleton()
a.instance()


# new方法实现
class Singleton(object):
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        pass


a = Singleton()
a.__new__()
