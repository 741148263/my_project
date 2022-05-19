# 十进制转2进制
import sys
print(bin(10))

# 十进制转八进制
print(oct(10))

# 十进制转十六禁止
print(hex(10))

# 十进制转ASCII
print(chr(65))

# ASCII转十进制
print(ord("A"))

# 执⾏字符串表⽰的代码
s = "print('hello world')"
r = compile(s, "<string>", "exec")
print(r)
print(eval(r))

# 动态创建字典
print(dict(zip(["a", "b"], [1, 2])))
print(dict([("a", 1), ("b", 2)]))


# 查看变量所占字节数
a = {"a": 1, "b": 20}
print(sys.getsizeof(a))


# 过滤器：在函数中设定过滤条件，迭代元素，保留返回值为 True的元素
fil = filter(lambda x: x > 10, [1, 11, 2, 45, 7, 6, 13])
print(list(fil))

# 创建冻结集合
print(frozenset([1, 2, 1, 3, 4, 3]))
print(frozenset({1, 2, 3}))

# 判断子列
print(issubclass(int, object))

# 创建迭代器
lst = [1, 3, 4]
for i in iter(lst):
    print(type(i))

# 次幂
print(pow(3, 2, 4))

# 排序
a = [{'name': 'xiaoming', 'age': 18, 'gender': 'male'},
     {'name': 'xiaohong', 'age': 20, 'gender': 'female'}]
print(sorted(a, key=lambda x: x["age"], reverse=False))

# 求和的初始值
a = [1, 3, 4, 5, 1]
print(sum(a))
# 求和的初始值为10
print(sum(a, 10))


# 不⽤else和if实现计算器
from operator import *

def calculator(a, b, k):
    return {
        "+": add,
        "-": sub,
        "*": mul,
        "/": truediv,
        "**": pow
    }[k](a, b)

calculator(1, 2, '+')
calculator(3, 4, '**')

# 求众数
def top1(lst):
    return max(lst, default='列表为空', key=lambda v: lst.count(v))
lst = [1, 3, 3, 2, 1, 1, 2]
r = top1(lst)

# 多表之最
def max_lists(*lst):
    return max(max(*lst, key=lambda v: max(v)))
r = max_lists([1, 2, 3], [6, 7, 8], [4, 5])
print(r)

# 值最大的字典
def max_pairs(dic):
    if len(dic) == 0:
        return dic
    max_val = max(map(lambda v: v[1], dic.items()))
    return [item for item in dic.items() if item[1] == max_val]
r = max_pairs({'a': -10, 'b': 5, 'c': 3, 'd': 5})
print(r)


# 返回字典d前n个最⼤值对应的键
from heapq import nlargest

def topn_dict(d, n):
    return nlargest(n, d, key=lambda k: d[k])
print(topn_dict({'a': 10, 'b': 8, 'c': 9, 'd': 10}, 3)) # ['a', 'd', 'c']

# 命名元组
from collections import namedtuple
# 定义名字为Point的元祖，字段属性有x,y,z
# 使⽤命名元组写出来的代码可读性更好，尤其处理上百上千个属性时作⽤更加凸显
Point = namedtuple('Point', ['x', 'y', 'z'])
lst = [Point(1.5, 2, 3.0), Point(-0.3, -1.0, 2.1), Point(1.3, 2.8, -2.5)]
print(lst[0].y - lst[1].y)


# 重洗数据集
from random import shuffle, randint
lst = [randint(0,50) for _ in range(100)]
print(lst)
shuffle(lst)
print(lst[:5])

print("-"*30)
# chain函数串联a和b，兼顾内存效率同时写法更加优雅
from itertools import chain
a = [1,3,5,0]
b = (2,4,6)
for i in chain(a,b):
    print(i)

print("-"*30)

# 操作函数对象
def f():
    print('i\'m f')

def g():
    print('i\'m g')

[f, g][1]()